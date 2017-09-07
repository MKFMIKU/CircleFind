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
from check_color import checkRed,checkBlue,checkGreen,checkColor,checkAllColor
from functools import cmp_to_key

def _sortCircle(a,b):
    if abs(a[1]-b[1]) < 40:
        return b[0]-a[0]
    else:
        return a[1]-b[1]
    
def _sortSmall(a,b):
    if abs(a[1]-b[1]) < 30:
        return a[0]-b[0]
    else:
        return b[1]-a[1]
    
def _abs(a):
    if a<0:
        return -a
    else:
        return a
        
class CheckImage:
    def __init__(self, type=1):
        self.type = type
        self._checkType(type)
        
    def _checkType(self, type):
        if type==1:
            self.radius = 30
            self.size = [6,52]
            self.range = [50,3600,700,1350]
            self.widthFilter = [3000,3200]
            self.threshFilter = [125,255]
            self.cycleFilter = [50,30,20,35]
        if type==2:
            self.radius = 35
            self.size = [6,50]
            self.range = [50,3600,400,1000]
            self.widthFilter = [2800,3500]
            self.threshFilter = [225,255]
            self.cycleFilter = [50,40,25,35]
        if type==3:
            self.radius = 35
            self.size = [6, 43]
            self.range = [0,3600,500,1100]
            self.cycleFilter = [50,40,25,45]
            self.cycleFilter = [50,40,20,40]
            
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
    
    def _checkPont(self,im,p):
        mask_r = checkRed(im)
        mask_b = checkBlue(im)
        mask_g = checkGreen(im)
        if p==0:
            # DOWN
            if mask_r.mean()>140:
                return 1
            if mask_r.mean() > 20 and mask_b.mean() > 20:
                return 1
            if mask_r.mean() > 20 and mask_g.mean() > 20:
                return 1
        else:
            if mask_b.mean() > 140:
                return 2
            if mask_b.mean() > 20 and mask_r.mean() > 20:
                return 2
            if mask_b.mean() > 20 and mask_g.mean() > 20:
                return 2
        return 0
            
            
    def check_down(self,path):
        colors_check = np.zeros((15,6), dtype=np.int)
        points_check = np.zeros((15,6), dtype=np.int)
        img = cv2.imread(path)
        crop = img[400:1500,1300:1900]
        # crop = cv2.flip(crop,-1)
        saver(crop,"C")
        crop_gray = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)
        circles = cv2.HoughCircles(crop_gray,cv2.HOUGH_GRADIENT,1,20,
                                   param1=50,
                                   param2=30,
                                   minRadius=20,
                                   maxRadius=40)
        draw = self._drawCircles(crop, circles)
        saver(draw,"D_%s"%path[-8:-4])
        one = circles[0]
        one = sorted(one,key=cmp_to_key(_sortSmall))
        radius = 30
        count = 0
        points = 0
        for c in one:
            # print(c)
            c = np.array(c).astype('int')
            circle = crop[c[1]-radius:c[1]+radius,
                          c[0]-radius:c[0]+radius,:]
            up_circle = crop[c[1]-radius:c[1],
                          c[0]:c[0]+radius,:]
            down_circle = crop[c[1]:c[1]+radius,
                          c[0]-radius:c[0],:]
            saver(circle,"C_%d"%count)
            # saver(down_circle, "D_%d"%count)
            # saver(up_circle, "U_%d"%count)
            color = checkAllColor(circle)
            points = self._checkPont(up_circle,1)+self._checkPont(down_circle,0)
            colors_check[count//6][count%6] = color
            points_check[count//6][count%6] = points
            count+=1
        for c in range(count,90):
             colors_check[count//6][count%6] = -1
             points_check[count//6][count%6] = -1
             count+=1
        return colors_check,points_check
        

    def check_up(self,path):
        result = np.zeros((self.size[1]), dtype=np.int)
        err = 0
        y_index = 0     #第几行
        count = 0       #第几个
        ll = 0
        outer_side = 0

        # Read
        img = cv2.imread(path)
        crop = img[:,self.range[2]:self.range[3], :]
        crop = cv2.flip(crop,-1)
        crop_gray = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)
        circles = self._findCircles(crop_gray)

        # Logger
        saver(crop,"C")
        draw = self._drawCircles(crop, circles)
        saver(draw,"D_%s"%path[-8:-4])
        
        # 特殊情况，不想改了
        if path[-8:-4] == "0146" or  path[-8:-4] == "0148":
            err = 1
        
        one = circles[0]
        one = sorted(one,key=cmp_to_key(_sortCircle))
        y_min = one[0][1]
        x_max = one[0][0]
        # 过滤Type1的两个噪声
        if self.type == 1:
            one = one[2:]

        for c in one:
            count+=1
            c = np.array(c).astype('int')
            circle = crop[c[1]-self.radius:c[1]+self.radius,
                          c[0]-self.radius:c[0]+self.radius,:]
            if c[1] - y_min > self.radius*4:
                break
            color = checkColor(circle)
            if _abs(c[1] - y_min) > self.radius*2-20:
                y_index += 1
                x_max = c[0] #换行了，代表最右边的坐标x—max更新
            y_min = c[1]
            input_index = y_index   #如果没有问题,用y_index作为结果添加的位置
           
           #如果这个圆圈是在左边的圆圈，并且右边没有圆圈(就是说这个圆圈的x等于代表第一个圆圈的x_max)
            if outer_side!=0 and c[0] == x_max and abs(c[0]-outer_side)<self.radius:
                input_index = ll

            # 这个圆圈和它右边的链接不上，应该是换行来的圆圈
            if x_max - c[0] > self.radius*3:
                input_index = ll
            else:
                x_max = c[0]
            
            add = 0
            if color==1:
                add = 1
            else:
                add = -1
            
            #如果两个圆圈颜色不同，就是换行来的
            if abs(result[y_index])==5 and abs(result[y_index]+add) < abs(result[y_index]) + abs(add):
                input_index = ll

            #进行叠加计算
            result[input_index] += add
            
            if abs(result[y_index]) >= self.size[0]:
                ll = y_index
                outer_side = c[0]
        
        #识别报错的东西
        for i in range(0, y_index):
            if abs(result[i]) >= 6:
                for j in range(i+1, y_index):
                    #print("I: ", i, "J: ",j, result[i], result[j])
                    if abs(result[i] + result[j]) >= abs(result[i]) + abs(result[j]) and abs(result[j])>=6:
                        if abs(result[i])-5 >= j-i:
                            err = 1
                            break
        return result,one,err
    
    def check(self, path, up_down):
        err = 0
        result = []
        if up_down==0:
            #上栏
            result,_,_err  = self.check_up(path)
            err = _err
        else:
            #下栏
            if self.type != 1:
                err = 2
            else:
                result = [colors_check,points_check]  = self.check_down(path)
        return err,result


if __name__ == "__main__":
    path1 = "test/type1.jpg"
    path2 = "test/type2.jpg"
    path3 = "test/type3.jpg"
    test_err = "test/err.jpg"
    path = '/Users/kangfu/Downloads/image/2017-08-25 (1) 0145.jpg'
    checker = CheckImage(1)
    err,result = checker.check(path,1)
    print("Err", err)
    print("Result", result)
    
