#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 16:02:39 2017

@author: kangfu
"""
import cv2
import math
import numpy as np
from utils import saver
from check_color import checkColor
from functools import cmp_to_key

def _sortCircle(a,b):
    if abs(a[1]-b[1]) > 40:
        return a[1]-b[1]
    else:
        return b[0]-a[0]
    
def _abs(a):
    if a<0:
        return -a
    else:
        return a
        
class CheckImage:
    def __init__(self, type=1):
        self._checkType(type)
        
    def _checkType(self, type):
        if type==1:
            self.radius = 30
            self.size = [6,52]
            self.range = [400,3500,850,1300]
            self.widthFilter = [3000,3200]
            self.threshFilter = [125,255]
            self.cycleFilter = [50,40,20,40]
        if type==2:
            self.radius = 35
            self.size = [6,50]
            self.range = [50,3500,350,900]
            self.widthFilter = [2800,3500]
            self.threshFilter = [225,255]
            self.cycleFilter = [50,40,20,40]
        if type==3:
            self.radius = 35
            self.size = [6, 43]
            self.range = [00,3600,550,1100]
            self.cycleFilter = [50,40,25,45]
            self.cycleFilter = [50,40,20,40]
    
    def _drawCircles(self, crop, circles):
        draw = crop.copy()
        circles = np.uint16(np.around(circles))
        for i in circles[0,:]:
            # draw the outer circle
            cv2.circle(draw,(i[0],i[1]),i[2]+4,(0,255,0),2)
            # draw the center of the circle
            cv2.circle(draw,(i[0],i[1]),2,(0,0,255),3)
        return draw
        
    def _angle_cos(self, p0, p1, p2):
        d1, d2 = (p0-p1).astype('float'), (p2-p1).astype('float')
        return abs( np.dot(d1, d2) / np.sqrt( np.dot(d1, d1)*np.dot(d2, d2) ) )
    
    def _checkSquare(self, cnt):
        cnt_len = cv2.arcLength(cnt, True)
        cnt = cv2.approxPolyDP(cnt, 0.02*cnt_len, True)
        if len(cnt) == 4 and cv2.contourArea(cnt) > 1000 and cv2.isContourConvex(cnt):
            cnt = cnt.reshape(-1, 2)
            max_cos = np.max([self._angle_cos( cnt[i], cnt[(i+1) % 4], cnt[(i+2) % 4] ) for i in range(4)])
            if max_cos < 0.1:
                w = cnt[1][1]-cnt[0][1]
                if w>self.widthFilter[0] and w<self.widthFilter[1]:
                    self.square = cnt
                    return True
        return False
    
    def _findCircles(self, thresh):
        circles = cv2.HoughCircles(thresh,cv2.HOUGH_GRADIENT,1,20,
                                   param1=self.cycleFilter[0],
                                   param2=self.cycleFilter[1],
                                   minRadius=self.cycleFilter[2],
                                   maxRadius=self.cycleFilter[3])
        return circles
    
    def _findLastCircle(self, circles):
        last_w = 0
        last_h = 10000
        for circle in circles[0]:
            if circle[0]>last_w:
                last_w = circle[0]
            if circle[1]<last_h:
                last_h = circle[1]
        return [last_w,last_h]
            
    def check(self, path):
        result = np.zeros((self.size[1]), dtype=np.int)
        img = cv2.imread(path)
        crop = img[self.range[0]:self.range[1],
                   self.range[2]:self.range[3], :]
        crop = cv2.flip(crop,-1)
        crop_gray = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)
        # Find corner by circle
        circles = self._findCircles(crop_gray)
        draw = self._drawCircles(crop, circles)
        # corner = self._findLastCircle(circles)
        y_index = 0
        one = circles[0]
        one = sorted(one,key=cmp_to_key(_sortCircle))
        
        y_max = circles[0][0][1]
        count = 0
        ll = 0
        x_min = circles[0][0][0]
        for c in one:
            c = np.array(c).astype('uint16')
            circle = crop[c[1]-self.radius:c[1]+self.radius,
                          c[0]-self.radius:c[0]+self.radius,:]
            count+=1
            if _abs(c[1] - y_max) > self.radius*2-20:
                y_index += 1
                x_min = c[0]
            y_max = int(c[1])
            input_index = y_index
            
            if c[0] == x_min and c[0] < circles[0][0][0]-(self.size[0]-1)*self.radius*2:
                input_index = ll            
            if x_min - c[0] > self.radius*3:
                input_index = ll
            else:
                x_min = c[0]
            if checkColor(circle):
                result[input_index] += 1
            else:
                result[input_index] += -1
            if result[y_index] >= self.size[0]:
                ll = y_index
        err = 0
        for i in range(0, y_index-2):
            if result[i]+result[i+2] > 12:
                err = 1
                break
        return result,circles,err

if __name__ == "__main__":
    path1 = "test/type1.jpg"
    path2 = "test/type2.jpg"
    path3 = "test/type3.jpg"
    checker = CheckImage(3)
    res,circles = checker.check(path3)
    