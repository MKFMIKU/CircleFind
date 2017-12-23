#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 15:02:07 2017

@author: kangfu
"""

from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import *
import sys
import yaml
import re
import datetime
import cv2
from save_result import save_result
from setting import SettingApp
from utils import is_image_file
import urllib.request

from os import listdir
from os.path import join
import os
import pandas as pd
import openpyxl
from detect_image import DetectImage
from check_image import CheckImage
from gui.mainwindowUI import Ui_MainWindow
from gui.dialogUI import Ui_Dialog
import gui.outfile


def boldExcel(path):
    font = openpyxl.styles.Font(name='Times New Roman',bold=True)
    _excel = openpyxl.load_workbook(path)
    for i in _excel['Sheet1']['B']:
        i.font = font
    _excel.save(path)

class Runthread(QtCore.QThread):
    _signal = pyqtSignal(str)
    def __init__(self, parent=None):  
        super(Runthread, self).__init__()

    def __del__(self):
        self.wait()

    def run(self):
        detecter = DetectImage()
        main_app._update()
        while True:
            self.setpath = main_app.path
            '''
            读取目标文件夹下全部文件
            '''
            try:
                image_filenames = [self.setpath+'/'+x for x in listdir(self.setpath) if is_image_file(x)]
                if main_app.up_down == 0:
                    need_test = [i for i in  image_filenames if i not in main_app.last_filenames_up]
                elif main_app.up_down == 1:
                    need_test = [i for i in  image_filenames if i not in main_app.last_filenames_down]
                else:
                    need_test = [i for i in  image_filenames if i not in main_app.last_filenames_card]
                need_test = list(set(need_test))
            except Exception as e:
                self._signal.emit("文件路径错误，无法读取图片", e)
                break


            if len(need_test)==0:
                continue
            need_test.sort()
            for f in need_test:
                log = f
                if main_app.begin_run == 1:
                    self._signal.emit("开始检测 %s"%f)
                    im = cv2.imread(f)
                    if im is None:
                        self._signal.emit("读取 %s 错误"%f)
                        continue
                    try:
                        type = detecter.detect(f)
                        print("总类%d"%type)
                        checker = CheckImage(type)
                        err,res = checker.check(f,main_app.up_down)
                    except Exception as e:
                        print(f)
                        print(e)
                        err = 1
                    if err==1:
                        self._signal.emit("%s 图片错误 无法识别"%f)
                        res = [-1000]
                    elif err==2:
                        self._signal.emit("%s 图片下栏无法识别"%f)
                        res = [-1000]
                    else:
                        self._signal.emit("检查 %s 结束 种类为：%d"%(f,type))
                    if main_app.up_down == 0:
                        main_app.up_ans.extend(save_result(res,log,0))
                        main_app.last_filenames_up.append(f)
                    elif main_app.up_down == 1:
                        a,b = save_result(res,log,1)
                        main_app.down_ans[0].extend(a)
                        main_app.down_ans[1].extend(b)
                        main_app.last_filenames_down.append(f)
                    else:
                        main_app.card_ans.extend(save_result(res,log,2))
                        main_app.last_filenames_card.append(f)
                else:
                    break
            if  main_app.begin_run == 0:
                break

class MainApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainApp, self).__init__()
        self.setupUi(self)  # UI初始化
        self.settingSaver = SettingApp()    # 建立设置窗口
        self.thread = Runthread()   # 建立检查进程
        self.thread._signal.connect(self.logOuter)  # 设置信号槽
        self.startButton.clicked.connect(self.startButtonAction)
        self.stopButton.clicked.connect(self.stopButtonAction)
        self.settingButton.clicked.connect(self.settingButtonAction)
        self.scanButton.clicked.connect(self.switch_devices)
        self.cameraButton.clicked.connect(self.switch_devices)
        self.upButton.clicked.connect(self.switch_Up)
        self.downButton.clicked.connect(self.switch_Down)
        self.cardButton.clicked.connect(self.switch_Card)
        self.clearLog.clicked.connect(self.clearLogger)
        self.pre()  # 初始化各种状态

    def pre(self):
        '''
        初始化各种状态
        begin_run 开始运行
        devices 设备切换（读取图片路径切换）
        up_down 上下栏切换 （图片数组切换）
        last_filenames_up 已经检查的上栏图片文件夹
        last_filenames_down 已经检查的下栏图片文件夹
        last_filenames_card 已经检查的卡片图片文件夹
        up_ans 上栏检查的结果
        down_ans 下栏检查的结果
        card_ans 卡片检查的结果
        setting 从目录中读取上一次的配置文件
        '''
        self.begin_run = 0
        self.devices = 0    #设备切换
        self.up_down = 0    #上栏或者下栏切换
        self.last_filenames_up = []
        self.last_filenames_down = []
        self.last_filenames_card = []
        self.up_ans = []
        self.down_ans = [[],[]]
        self.card_ans = []
        with open('setting.yml') as f:
            self.setting = yaml.safe_load(f)
        # 初始化部分UI状态
        self.textEdit.setReadOnly(True)
    
    def switch_Up(self):
        self.up_down = 0
        self.logOuter("切换为上栏",1)
        self._update()
    
    def switch_Down(self):
        self.up_down = 1
        self.logOuter("切换为下栏",1)
        self._update()
    
    def switch_Card(self):
        self.up_down = 2
        self.logOuter("切换为卡片",1)
        self._update()

    def _update(self):
        '''
        更新按钮的样式
        '''
        if self.devices == 0:
            self.scanButton.setStyleSheet("border-image: url(:/new/outer/scan.png)")
            self.cameraButton.setStyleSheet("border-image: url(:/new/outer/camera_black.png)")
            self.path = self.setting['scan']
        else:
            self.scanButton.setStyleSheet("border-image: url(:/new/outer/scan_off.png)")
            self.cameraButton.setStyleSheet("border-image: url(:/new/outer/camera.png)")
            self.path = self.setting['camera']

        if self.up_down == 0:
            self.downButton.setStyleSheet("border-image: url(:/new/outer/down_black.png)")
            self.cardButton.setStyleSheet("border-image: url(:/new/outer/down_black.png)")
            self.upButton.setStyleSheet("border-image: url(:/new/outer/up.png)")
        elif self.up_down == 1:
            self.upButton.setStyleSheet("border-image: url(:/new/outer/up_black.png)")
            self.cardButton.setStyleSheet("border-image: url(:/new/outer/down_black.png)")
            self.downButton.setStyleSheet("border-image: url(:/new/outer/down.png)")
        else:
            self.upButton.setStyleSheet("border-image: url(:/new/outer/up_black.png)")
            self.downButton.setStyleSheet("border-image: url(:/new/outer/down_black.png)")
            self.cardButton.setStyleSheet("border-image: url(:/new/outer/down.png)")
        
    def clearLogger(self):
        self.textEdit.clear()

    def switch_devices(self):
        _translate = QtCore.QCoreApplication.translate
        if self.begin_run==1:
            self.begin_run = 0
            self.startButton.setStyleSheet("border-image: url(:/new/outer/start_off.png)")
            self.label.setText(_translate("MainWindow", "开始"))
        if self.devices == 0:
            self.devices =1
            self.logOuter("切换为高拍仪",1)
        else:
            self.devices =0
            self.logOuter("切换为扫描仪",1)
        self._update()

    def logOuter(self, text, type=0):
        cursor = self.textEdit.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        if re.search(r"错误",text):
            type = 1
        if type==0:
            cursor.insertHtml('<p style="color:black">'+text+'</p><br>')
        else:
            cursor.insertHtml('<p style="color:red">'+text+'</p><br>')
        self.textEdit.ensureCursorVisible()
        
    def startButtonAction(self):
        _translate = QtCore.QCoreApplication.translate
        print("Start")
        self._update()
        self.stopButton.setStyleSheet("border-image: url(:/new/outer/stop.png)")
        if self.begin_run==1:
            self.logOuter("暂停\n", 1)
            self.begin_run = 0
            self.startButton.setStyleSheet("border-image: url(:/new/outer/start.png)")
            self.label.setText(_translate("MainWindow", "开始"))
        else:
            self.logOuter("开始\n", 1)
            self.begin_run = 1
            self.thread.start()
            self.startButton.setStyleSheet("border-image: url(:/new/outer/pause.png)")
            self.label.setText(_translate("MainWindow", "暂停"))
            
    def stopButtonAction(self):
        _translate = QtCore.QCoreApplication.translate
        print("Stop")
        self.logOuter("停止\n", 1)
        self.begin_run = 0
        self.startButton.setStyleSheet("border-image: url(:/new/outer/start.png)")
        self.label.setText(_translate("MainWindow", "开始"))
        now = datetime.datetime.now()
        time = now.strftime('%Y_%m_%d_%H_%M_%S')
        
        try:
            if self.up_down==0:
                result = pd.DataFrame(self.up_ans)
                result.to_excel(self.setting['result']+"/结果_%s.xlsx"%time)
                boldExcel(self.setting['result']+"/结果_%s.xlsx"%time)
            elif self.up_down==1:
                result_A = pd.DataFrame(self.down_ans[0])
                result_B = pd.DataFrame(self.down_ans[1])
                result_A.to_excel(self.setting['result']+"/下栏结果_%s.xlsx"%time)
                result_B.to_excel(self.setting['result']+"/下栏小点结果_%s.xlsx"%time)
                
                boldExcel(self.setting['result']+"/下栏结果_%s.xlsx"%time)
                boldExcel(self.setting['result']+"/下栏小点结果_%s.xlsx"%time)
            elif self.up_down==2:
                result = pd.DataFrame(self.card_ans)
                result.to_excel(self.setting['result']+"/卡片结果_%s.xlsx"%time)

            self.logOuter("储存结果于 %s\n"%self.setting['result'], 1)

        except Exception as e:
                print(e)
                self.logOuter("输出结果路径错误\n", 1)

    def settingButtonAction(self):
        print("Setting")
        self.settingSaver.show()
    
if __name__ == "__main__":
    f = False
    with urllib.request.urlopen('http://mkfweb.coding.me/CircleFind/status') as response:
        html = response.read()
        if html == b'on':
            f = True
    if f == True:
        app = QtWidgets.QApplication(sys.argv)
        global main_app
        main_app = MainApp()
        main_app.show()
        sys.exit(app.exec_())