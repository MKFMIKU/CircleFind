#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 20:03:40 2017

@author: kangfu
"""

import cv2
import numpy as np
from utils import saver
from skimage.measure import compare_ssim,compare_psnr

path1 = "test/c1.png"
path2 = "test/c2.png"
path3 = "test/c3.png"

im_demo = [
    cv2.imread(path1, 0),
    cv2.imread(path2, 0),
    cv2.imread(path3, 0),
]

def checkCircle(im,radius):
    im_g = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    # print(circles)
    h_im,w_im = im_g.shape
    # cv2.circle(im_g, (h_im//2,w_im//2), radius+4, (255,255,255), -1)
    im_edges = cv2.Canny(im_g,100,200)

    saver(im_edges,"e")
    mask = cv2.imread("test/circle_mask.png",0)
    mask = cv2.resize(mask, (h_im,w_im))
    _, mask = cv2.threshold(mask,127,255,cv2.THRESH_BINARY)
    # cv2.circle(mask, (h_im//2,w_im//2), radius-2, 255, thickness=-1)
    saver(mask,"m")
    # saver(im_edges,"e")
    diff = cv2.bitwise_and(im_edges, im_edges, mask=mask)
    saver(diff,"d")
    # print(diff.mean())
    if diff.mean() > 8:
        return 1
    return 0
    # print(diff.mean())
    # print(im_g.mean())
    # _, im_g = cv2.threshold(im_g,127,255,cv2.THRESH_BINARY_INV)
    # for index, demo in enumerate(im_demo):
    #     demo_r = cv2.resize(demo, (h_im,w_im))
    #     demo_edges = cv2.Canny(demo_r,100,200)
    #     saver(demo_edges,"DIFF_%d"%index)
    #     psnr = compare_psnr(im_edges,demo_edges)
    #     print(psnr)
    #     cv2.circle(demo_r, (h_im//2,w_im//2), radius-5, (255,255,255), thickness=-1)
    #     _, demo_r = cv2.threshold(demo_r,127,255,cv2.THRESH_BINARY_INV)
    #     circle_diff = demo_r-im_g
    #     saver(circle_diff,"DIFF_%d"%index)
    #     print(circle_diff.mean())

if __name__ == "__main__":
    im = cv2.imread("outer/test_17.png")
    print(checkCircle(im,25))