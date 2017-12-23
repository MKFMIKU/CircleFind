# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 23:23:27 2017

@author: QH
"""

import cv2
import math
import numpy as np
from os import listdir
from os.path import join
import os
from utils import is_image_file

def on_mouse(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        sbox = [x, y]
        boxes.append(sbox)
             # print count
             # print sbox

    elif event == cv2.EVENT_LBUTTONUP:
        ebox = [x, y]
        boxes.append(ebox)
        print(boxes)
        print("W: {} H:{}".format(boxes[-1][1]-boxes[-2][1], boxes[-1][0]-boxes[-2][0]))
        crop = im[boxes[-2][1]:boxes[-1][1],boxes[-2][0]:boxes[-1][0]]
        
        cv2.imshow('crop',crop)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        


path =  '../img_test/'

image_filenames = [path+x for x in listdir(path) if is_image_file(x)]
count = 0
for img in image_filenames:
    im = cv2.imread(img)
    im = im[195:1215, 765:1185]
    cv2.imwrite('out/im_%d.png'%count, im)
    count += 1