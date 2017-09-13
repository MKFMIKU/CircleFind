#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 22:18:02 2017

@author: kangfu
"""

import cv2
import math
import numpy as np
from utils import saver
from check_color import checkRed,checkBlue,checkGreen,checkColor,checkAllColor

kernel = np.ones((4,4),np.uint8)

def clean_noise(im, type):
    if type==1:
        green_mask = checkGreen(im)
        x2,y2 = green_mask.shape
        mix_mask = cv2.rectangle(im.copy(), (0, 0), (y2, x2), (255,255,255), -1)
        
        green_mask = cv2.erode(green_mask,kernel,iterations = 1)
        green_mask = cv2.dilate(green_mask,kernel,iterations = 1)
        _,green_mask_I = cv2.threshold(green_mask.copy(),10,255,cv2.THRESH_BINARY_INV)
        _,green_mask = cv2.threshold(green_mask.copy(),10,255,cv2.THRESH_BINARY)
        
        clean = cv2.bitwise_and(im, im.copy(), mask=green_mask_I)
        mix_mask = cv2.bitwise_and(mix_mask, mix_mask.copy(), mask=green_mask)
        clean = cv2.add(clean, mix_mask)
        return clean
    return im
        
if __name__ == "__main__":
    path = './outer/test_CROP.png'
    im = cv2.imread(path)
    cleaned = clean_noise(im, 1)
    saver(cleaned,"G")