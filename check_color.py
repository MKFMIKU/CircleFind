#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 20:03:40 2017

@author: kangfu
"""
import cv2
import numpy as np
from utils import saver

def checkRed(img):
    lower_red = np.array([160, 100, 100])
    upper_red = np.array([180, 255, 255])
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask_red = cv2.inRange(img_hsv, lower_red, upper_red)
    return mask_red.mean()

def checkBlue(img):
    lower_blue = np.array([100,150,0])
    upper_blue = np.array([140,255,255])
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask_blue = cv2.inRange(img_hsv, lower_blue, upper_blue)
    return mask_blue.mean()

def checkColor(img):
    blue_rate = checkBlue(img)
    red_rate = checkRed(img)
    if red_rate>blue_rate:
        return 1
    else:
        return 0
    
if __name__ == "__main__":
    path = "test/test_11.png"
    img = cv2.imread(path)
    if checkColor(img)==1:
        print("Red Cycle")
    else:
        print("Blue Cycle")