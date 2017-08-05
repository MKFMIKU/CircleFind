#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 15:02:07 2017

@author: kangfu
"""
import pandas as pd
import yaml

def save_result(res):
    with open('setting.yml') as f:
        setting = yaml.safe_load(f)
    result_path = setting['result']
    ans = []
    for r in res:
        if r > 0:
            ans.append(['红',r])
        elif r<0:
            ans.append(['蓝',r])
    result = pd.DataFrame(ans)
    result.to_excel(result_path+"/结果.xlsx")