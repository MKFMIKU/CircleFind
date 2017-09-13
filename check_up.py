#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 16:02:39 2017

@author: kangfu
"""
import cv2
import math
import numpy as np
from utils import saver
from check_color import checkRed,checkBlue,checkGreen,checkColor,checkAllColor
from functools import cmp_to_key
from remove_noise import clean_noise

