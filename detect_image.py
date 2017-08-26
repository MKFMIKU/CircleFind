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
                cv2.imread(path1),
                cv2.imread(path2),
                cv2.imread(path3),
        ]
        
    def detect(self,f):
        img = cv2.cvtColor(cv2.imread(f), cv2.COLOR_BGR2GRAY)
        im_u = img[0:3400,400:1000]
        im_d = img[0:3400,1200:2400]
        index = 0
        mse_min = -1
        for i in range(len(self.type)):
            u = cv2.cvtColor(self.type[i][0:3400,400:1000,:], cv2.COLOR_BGR2GRAY)
            d = cv2.cvtColor(self.type[i][0:3400,1200:2400,:], cv2.COLOR_BGR2GRAY)
            mse = compare_psnr(u,im_u) + compare_psnr(d,im_d)
            # saver(d,'d_%d'%i)
            # saver(u,'u_%d'%i)
            print(mse, index)
            if mse_min < mse:
                index = i
                mse_min = mse
        return index+1
         
if __name__ == "__main__":
    detecter = DetectImage()
    type = detecter.detect('/Users/kangfu/Downloads/image/2017-08-25 (1) 0058.jpg')
    print(type)