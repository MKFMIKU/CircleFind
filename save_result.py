#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 15:02:07 2017

@author: kangfu
"""
import pandas as pd
import yaml
import abs

def save_result(res,count):
    with open('setting.yml') as f:
        setting = yaml.safe_load(f)
    result_path = setting['result']
    f = 1
    ans = []
    for r in res:
        c = []
        if r > 0:
            c = ['红',abs(r)]
        elif r<0:
            c = ['蓝',abs(r)]  
        ans.append(c)
    ans = pd.DataFrame(ans)
    ans.to_excel(result_path+"/结果_%d.xlsx"%count)