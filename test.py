#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 20:47:02 2017

@author: kangfu
"""
import cv2
import math
import numpy as np
import matplotlib.pyplot as plt
from utils import saver
from check_color import checkColor

im = cv2.imread('outer/test_62_.png')

img_hsv = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)

lower_red = np.array([160, 100, 100])
upper_red = np.array([180, 255, 255])

lower_blue = np.array([100,150,0])
upper_blue = np.array([140,255,255])

mask_red = cv2.inRange(img_hsv.copy(), lower_red, upper_red)
mask_blue = cv2.inRange(img_hsv, lower_blue, upper_blue)