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
from check_color import checkColor
from functools import cmp_to_key

path1 = "test/type1.jpg"
path2 = "test/type2.jpg"
path3 = "test/type3.jpg"

def mse(imageA, imageB):
	# the 'Mean Squared Error' between the two images is the
	# sum of the squared difference between the two images;
	# NOTE: the two images must have the same dimension
	err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
	err /= float(imageA.shape[0] * imageA.shape[1])
	
	# return the MSE, the lower the error, the more "similar"
	# the two images are
	return err

class DetectImage:
    def __init__(self):
        self.type = [
                cv2.imread(path1)[0:3400,0:800,:],
                cv2.imread(path2)[0:3400,0:800,:],
                cv2.imread(path3)[0:3400,0:800,:],
        ]
        
    def detect(self,img):
        index = 0
        ssim_min = -1
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        for i in range(len(self.type)):
            d = cv2.cvtColor(self.type[i], cv2.COLOR_BGR2GRAY)
            ssim = compare_psnr(d,img)
            # saver(d,i)
            # print(ssim, index)
            if ssim_min < ssim:
                index = i
                ssim_min = ssim
        return index+1
         
if __name__ == "__main__":
    im = cv2.imread("../img/2017-08-11 (1) 0006.jpg")[0:3400,0:800,:]
    saver(im,"i")
    detecter = DetectImage()
    type = detecter.detect(im)
    print(type)