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
    lower_red_one = np.array([150, 50, 46])
    upper_red_one = np.array([180, 255, 255])
    
    lower_red_two = np.array([0, 50, 46])
    upper_red_two = np.array([10, 255, 255])
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask_red = cv2.inRange(img_hsv, lower_red_one, upper_red_one)
    mask_red += cv2.inRange(img_hsv, lower_red_two, upper_red_two)
    return mask_red

def checkBlue(img):
    lower_blue = np.array([100,43,46])
    upper_blue = np.array([124,255,255])
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask_blue = cv2.inRange(img_hsv, lower_blue, upper_blue)
    return mask_blue

def checkGreen(img):
    lower_green = np.array([35,43,46])
    upper_green = np.array([99,255,255])
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask_green = cv2.inRange(img_hsv, lower_green, upper_green)
    return mask_green

def checkColor(img):
    blue_rate = checkBlue(img).mean()
    red_rate = checkRed(img).mean()
    if red_rate < 30 and blue_rate < 30:
    	return -1
    if red_rate>blue_rate:
        return 1
    else:
        return 2

def checkAllColor(img):
    blue_rate = checkBlue(img).mean()
    red_rate = checkRed(img).mean()
    green_rate = checkGreen(img).mean()
    if blue_rate>red_rate and blue_rate>green_rate:
        return 2
    if red_rate>blue_rate and red_rate>green_rate:
        return 1
    if green_rate>blue_rate and green_rate>red_rate:
        return 3
    return -1

if __name__ == "__main__":
    path = "outer/test_C_22.png"
    img = cv2.imread(path)
    r = checkGreen(img)

    print("Green: ", r.mean())
    saver(r,"GREEN")

    print("Blue: ", checkBlue(img).mean())

    saver(checkBlue(img),"Blue")
    
    print("Green", checkGreen(img).mean())
    saver(checkRed(img),"Red")