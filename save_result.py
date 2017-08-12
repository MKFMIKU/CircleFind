#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 15:02:07 2017

@author: kangfu
"""
import numpy as np

def save_result(res,log,t):
    if t==1:
        res[0][0] = np.append(res[0][0], [log])
        res[1][0] = np.append(res[1][0], [log])
        return res   
    f = 1
    ans = []
    for r in res:
        c = []
        if r > 0:
            c = ['红',abs(r)]
        elif r<0:
            c = ['蓝',abs(r)]
            if r == -1000:
                c = ['该图片系统无法识别']
        else:
            pass
        if r!=0 and f==1:
            c.append(log)
            f=0
        if r!=0:
            ans.append(c)
    return ans