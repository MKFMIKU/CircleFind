#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 15:02:07 2017

@author: kangfu
"""
import numpy as np
import types

def save_result(res,log,t):
    if t==1:
        ans_a = [[0,log]]
        ans_b = [[0,log]]
        
        count = 0
        if type(res[0]) == type(-1000):
             ans_a.append(["图片无法识别"])
             ans_b.append(["图片无法识别"])
        else:
            for i in res[0]:
                count+=1
                r = [count]
                for j in i:
                    if j==-1:
                        r.append('')
                    else:
                        r.append(j)
                ans_a.append(r)
            
            count = 0
            for i in res[1]:
                count+=1
                r = [count]
                for j in i:
                    if j==-1:
                        r.append('')
                    else:
                        r.append(j)
                ans_b.append(r)
        ans_a.append([""])
        ans_b.append([""])
        return ans_a,ans_b
    elif t==0:
        ans = [[0,log]]
        count = 0
        for r in res:
            count+=1
            c = []
            if r > 0:
                c = [count,'红',abs(r)]
            elif r<0:
                c = [count,'蓝',abs(r)]
            if r == -1000:
                c = ['该图片系统无法识别']
            if r!=0:
                ans.append(c)
        ans.append([""])
        return ans
    elif t==2:
        ans = [[0,log]]
        count = 0
        if type(res[0]) == type(-1000):
            ans.append(["图片无法识别"])
        else:
            for i in res:
                count+=1
                r = [count]
                for j in i:
                    if j==-1:
                        r.append('')
                    else:
                        r.append(j)
                ans.append(r)
        
        ans.append([""])
        return ans