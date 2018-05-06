#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 20:09:44 2017

@author: kangfu
"""

import cv2
import numpy as np

def saver (var, TAG):
    cv2.imwrite("outer/test_%s.png"%TAG, var)

def is_image_file(filename):
    return any(filename.endswith(extension) for extension in [".png", ".jpg", ".jpeg"])

def show(im):
    cv2.imshow('show', im)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
