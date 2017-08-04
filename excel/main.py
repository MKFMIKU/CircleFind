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
    