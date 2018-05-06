#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  5 15:40:46 2017

@author: kangfu
"""
import cv2
import math
import numpy as np
from skimage.measure import compare_ssim,compare_psnr
from utils import saver
from check_color import checkColor, checkGreen
from functools import cmp_to_key

path1 = "test/type1.jpg"
path2 = "test/type2.jpg"
path3 = "test/type3.jpg"


class DetectImage:
    def __init__(self):
        self.type = [
                cv2.imread(path1, 0)[0:3400,1200:2400],
                cv2.imread(path2, 0)[0:3400,1200:2400],
                cv2.imread(path3, 0)[0:3400,1200:2400],
        ]
        self.orb = cv2.AKAZE_create()
        self.bf = cv2.BFMatcher(cv2.NORM_HAMMING)
        
    def detect(self,f):
        img = cv2.imread(f)
        if img.shape[1] < 1600:
            im_crop = img[2800:,1100:]
            im_crop = checkGreen(im_crop)
            if im_crop.mean() > 50:
                return 5
            else:
                return 4
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        _,img = cv2.threshold(img, 127,255,cv2.THRESH_BINARY_INV)
        # saver(img[0:3400,1600:2400],"I")
        # print(img[0:3400,1600:2400].mean())
        if img[0:3400,1600:2400].mean() >= 10:
            return 2
        if img[0:3400,200:600].mean() >= 4:
            return 3
        return 1
                     
if __name__ == "__main__":
    detecter = DetectImage()
    type = detecter.detect('/Users/meikangfu/Downloads/over-img/img (524).jpg')
    print(type)