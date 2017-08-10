#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 15:02:07 2017

@author: kangfu
"""

def save_result(res,count):
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
            c.append(count)
            f=0
        if r!=0:
            ans.append(c)
    return ans