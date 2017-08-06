#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  5 15:40:46 2017

@author: kangfu
"""
import cv2
import math
import numpy as np
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
                cv2.imread(path1)[:,0:800,:],
                cv2.imread(path2)[:,0:800,:],
                cv2.imread(path3)[:,0:800,:],
                ]
        
    def detect(self,img):
        index = 0
        psnr_min = 10000
        for i in range(len(self.type)):
            psnr = mse(self.type[i],img)
            if psnr < psnr_min:
                index = i
                psnr_min = psnr
        return index+1
           
         
if __name__ == "__main__":
    im = cv2.imread("test/test1.jpg")[:,0:800,:]
    detecter = DetectImage()
    type = detecter.detect(im)
    print(type)