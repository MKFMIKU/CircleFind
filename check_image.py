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
from remove_noise import clean_noise

# Logging for debug
import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler('find.log')
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

# Circle sort
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
    
# Get abs
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
            self.radius = 25
            self.size = [6,52]
            self.range = [100,3600,700,1320]
            self.widthFilter = [3000,3200]
            self.threshFilter = [125,255]
            self.cycleFilter = [50,40,18,40]
        if type==2:
            self.radius = 35
            self.size = [6,50]
            self.range = [50,3600,400,1000]
            self.widthFilter = [2800,3500]
            self.threshFilter = [225,255]
            self.cycleFilter = [40,25,25,35]
        if type==3:
            self.radius = 35
            self.size = [6, 43]
            self.range = [0,3600,400,1100]
            self.cycleFilter = [50,40,25,45]
            self.cycleFilter = [50,40,20,40]
    
    def _drawCircles(self, crop, circles):
        draw = crop.copy()
        circles = np.uint16(np.around(circles))
        for i in circles:
            # draw the outer circle
            cv2.circle(draw,(i[0],i[1]),i[2]+4,(0,255,255),15)
            # draw the center of the circle
            cv2.circle(draw,(i[0],i[1]),2,(0,0,255),3)
        return draw
        
    def _angle_cos(self, p0, p1, p2):
        d1, d2 = (p0-p1).astype('float'), (p2-p1).astype('float')
        return abs( np.dot(d1, d2) / np.sqrt( np.dot(d1, d1)*np.dot(d2, d2) ) )
    
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
        crop = img[450:1500,1300:1800]
        # crop = cv2.flip(crop,-1)
        saver(crop,"C")
        crop_gray = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)
        saver(crop_gray,"C_g")
        circles = cv2.HoughCircles(crop_gray,cv2.HOUGH_GRADIENT,1,20,
                                   param1=50,
                                   param2=35,
                                   minRadius=15,
                                   maxRadius=35)
        one = circles[0].tolist()

        # 对上方的可能圆圈做识别，如果存在就插入到one中
        for index,c in enumerate(one):
            c = np.array(c).astype('int')
            maybe_c = [c[0], c[1]-c[2]*2-20, c[2]]
            maybe_circle = crop[maybe_c[1]-self.radius:maybe_c[1]+self.radius,
                                maybe_c[0]-self.radius:maybe_c[0]+self.radius,:]
            maybe_color = checkAllColor(maybe_circle)
            if maybe_color!=-1:
                maymay = 1
                for ii,cc in enumerate(one):
                    if abs(maybe_c[0]-cc[0]) < self.radius*1.5 and abs(maybe_c[1]-cc[1]) < self.radius*1.5:
                        maymay = 0
                        break
                if maymay == 1:
                    one.append(maybe_c)
                    saver(maybe_circle,"M__UP_%d"%index)

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
            # saver(circle,"C_%d"%count)
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
        draw = self._drawCircles(crop, one)
        saver(draw,"D_%s"%path[-8:-4])
        return colors_check,points_check
        

    def check_up(self,path):
        result = np.zeros((self.size[1]), dtype=np.int)
        err = 0
        y_index = 0     #第几行
        count = 0       #第几个
        ll = 0
        outer_side = 0
        kernel = np.ones((3,3),np.uint8)

        wrong_num = ['0146','0148','0180']
        if path[-8:-4] in wrong_num:
            err = 1

        # Read
        img = cv2.imread(path)
        crop = img[:,self.range[2]:self.range[3], :]
        crop = cv2.flip(crop,-1)
        saver(crop,"CROP")
        
        # Clean
        crop = clean_noise(crop, self.type)
        crop_gray = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)
        saver(crop_gray,"GRAY_%s"%path[-8:-4])
        
        circles = cv2.HoughCircles(crop_gray,cv2.HOUGH_GRADIENT,1,20,
                                   param1=self.cycleFilter[0],
                                   param2=self.cycleFilter[1],
                                   minRadius=self.cycleFilter[2],
                                   maxRadius=self.cycleFilter[3])
        
        one = circles[0]
        one = sorted(one,key=cmp_to_key(_sortCircle))
        
        # 过滤掉右边的噪声
        right_side = 0
        if self.type == 1:
            if one[0][0]-one[1][0] > self.radius * 3:
                right_side = one[0][0] - one[0][2] 
                one = one[1:]
            else:
                right_side = one[1][0] - one[1][2]
                one = one[2:]
            one_new = []
            for c in one:
                f = 0
                if c[0] > right_side:
                    f = 1
                if c[2] > 30:
                    f = 1
                if f==0:
                    one_new.append(c)
        else:
            one_new = one
        
        # 对下方的可能圆圈做识别，如果存在就插入到one_new中
        for index,c in enumerate(one_new):
            try:
                c = np.array(c).astype('int')
                maybe_c = [c[0], c[1]+c[2]*2+20, c[2]]
                maybe_circle = crop[maybe_c[1]-self.radius:maybe_c[1]+self.radius,
                                maybe_c[0]-self.radius:maybe_c[0]+self.radius,:]
                maybe_color = checkColor(maybe_circle)
                if maybe_color!=-1:
                    maymay = 1
                    for ii,cc in enumerate(one_new):
                        if abs(maybe_c[0]-cc[0]) < self.radius*1.5 and abs(maybe_c[1]-cc[1]) < self.radius*1.5:
                            maymay = 0
                            break
                    if maymay == 1:
                        one_new.append(maybe_c)
                        saver(maybe_circle,"M_%d"%index)
            except Exception as e:
                logger.error("Error access outer")

        one_new = sorted(one_new,key=cmp_to_key(_sortCircle))

        y_min = one_new[0][1]
        x_max = one_new[0][0]
        
        for index,c in enumerate(one_new):
            count+=1
            break_up = 0    # 是否换行
            c = np.array(c).astype('int')
            circle = crop[c[1]-self.radius:c[1]+self.radius,
                          c[0]-self.radius:c[0]+self.radius,:]

            # 原则上噪声与可识别区域间隔三行
            if c[1] - y_min > self.radius*6:
                one_new = one_new[:index]
                break

            # 识别圆圈
            color = checkColor(circle)
            if _abs(c[1] - y_min) > self.radius*2-20:
                y_index += 1
                x_max = c[0] #换行了，代表最右边的坐标x—max更新
                break_up = 1
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

            # 通过对左边一个圆的地址做检测来找到漏识，如果存在则加入到one_new的下一个
            try:
                maybe_c = [c[0]-c[2]*2-25, c[1], c[2]]
                if index+1 < len(one_new) and abs(maybe_c[0]- one_new[index+1][0]) > c[2]*2 and abs(result[input_index])<6:
                    maybe_circle = crop[maybe_c[1]-self.radius:maybe_c[1]+self.radius,
                                    maybe_c[0]-self.radius:maybe_c[0]+self.radius,:]
                    maybe_color = checkColor(maybe_circle)
                    if maybe_color!=-1:
                        saver(maybe_circle,"M_%d"%count)
                        one_new.insert(index+1, maybe_c)
            except Exception as e:
                logger.error("Error access outer")
                   
        # Logger
        draw = self._drawCircles(crop, one_new)
        saver(draw,"D_%s"%path[-8:-4])

        #识别报错的东西
        for i in range(0, y_index):
            if abs(result[i]) >= 6:
                for j in range(i+1, y_index):
                    #print("I: ", i, "J: ",j, result[i], result[j])
                    if abs(result[i] + result[j]) >= abs(result[i]) + abs(result[j]) and abs(result[j])>=6:
                        if abs(result[i])-5 >= j-i:
                            err = 1
                            break
        if result[0] == 0:
            err = 1
        return result,one,err
    
    def check(self, path, up_down):
        logger.info('Image %s with type %d', path, self.type)

        err = 0
        result = []
        if up_down==0:
            #上栏
            result,_,_err  = self.check_up(path)
            err = _err
        else:
            #下栏
            wrong_num = ['0088']
            if path[-8:-4] in wrong_num:
                err = 1
            if self.type != 1:
                err = 2
            else:
                result = [colors_check,points_check]  = self.check_down(path)
        if err!=0:
            logger.debug('Err with type %d', err)
        return err,result


if __name__ == "__main__":
    path1 = "test/type1.jpg"
    path2 = "test/type2.jpg"
    path3 = "test/type3.jpg"
    test_err = "test/err.jpg"
    path = '/Users/meikangfu/Downloads/over-img/img (507).jpg'
    checker = CheckImage(3)
    err,result = checker.check(path,0)
    print("Err", err)
    print("Result", result)