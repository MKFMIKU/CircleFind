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
        while True:
            self.setpath = main_app.path
            image_filenames = [self.setpath+'/'+x for x in listdir(self.setpath) if is_image_file(x)]
            need_test = [i for i in  image_filenames if i not in main_app.last_filenames]
            need_test = list(set(need_test))
            # need_test = list(set(image_filenames) ^ set(self.last_filenames))
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
                    type = detecter.detect(im[0:3500,0:800,:])
                    try:
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
                    else:
                        self._signal.emit("检查 %s 结束 种类为：%d"%(f,type))
                        if main_app.up_down == 0:
                            main_app.up_ans.extend(save_result(res,log,0))
                        else:
                            a,b = save_result(res,log,1)
                            main_app.down_ans[0].extend(a)
                            main_app.down_ans[1].extend(b)
                    main_app.last_filenames.append(f)
                else:
                    break
            if  main_app.begin_run == 0:
                break

class MainApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainApp, self).__init__()
        self.pre()
        self.setupUi(self)

        self.settingSaver = SettingApp()
        self.thread = Runthread()
        self.thread._signal.connect(self.logOuter)
        self.textEdit.setReadOnly(True)
        self.startButton.clicked.connect(self.startButtonAction)
        self.stopButton.clicked.connect(self.stopButtonAction)
        self.settingButton.clicked.connect(self.settingButtonAction)
        self.scanButton.clicked.connect(self.switch_devices)
        self.cameraButton.clicked.connect(self.switch_devices)
        self.pushButton.clicked.connect(self.switch_up_down)
        self.pushButton_2.clicked.connect(self.switch_up_down)
        self._update()

    def pre(self):
        self.begin_run = 0
        self.devices = 0    #设备切换
        self.up_down = 0    #上栏或者下栏切换
        self.last_filenames = []
        self.up_ans = []
        self.down_ans = [[],[]]
        with open('setting.yml') as f:
            self.setting = yaml.safe_load(f)

    def _update(self):
        if self.devices == 0:
            self.scanButton.setStyleSheet("border-image: url(:/new/outer/scan.png)")
            self.cameraButton.setStyleSheet("border-image: url(:/new/outer/camera_black.png)")
            self.path = self.setting['scan']
        else:
            self.scanButton.setStyleSheet("border-image: url(:/new/outer/scan_off.png)")
            self.cameraButton.setStyleSheet("border-image: url(:/new/outer/camera.png)")
            self.path = self.setting['camera']

        if self.up_down == 0:
            self.pushButton_2.setStyleSheet("border-image: url(:/new/outer/down_black.png)")
            self.pushButton.setStyleSheet("border-image: url(:/new/outer/up.png)")
        else:
            self.pushButton.setStyleSheet("border-image: url(:/new/outer/up_black.png)")
            self.pushButton_2.setStyleSheet("border-image: url(:/new/outer/down.png)")
    
    def switch_up_down(self):
        _translate = QtCore.QCoreApplication.translate
        if self.begin_run==1:
            self.begin_run = 0
            self.startButton.setStyleSheet("border-image: url(:/new/outer/start_off.png)")
            self.label.setText(_translate("MainWindow", "开始"))

        if self.up_down == 1:
            self.up_down = 0 
            self.logOuter("切换为上栏",1)
        else:
            self.up_down = 1
            self.logOuter("切换为下栏",1)
        self._update()

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
            self.startButton.setStyleSheet("border-image: url(:/new/outer/start_off.png)")
            self.label.setText(_translate("MainWindow", "开始"))
        else:
            self.logOuter("开始\n", 1)
            self.begin_run = 1
            self.thread.start()
            self.startButton.setStyleSheet("border-image: url(:/new/outer/pause.png)")
            self.label.setText(_translate("MainWindow", "暂停"))
            
    def stopButtonAction(self):
        print("Stop")
        self.logOuter("停止\n", 1)
        self.begin_run = 0
        now = datetime.datetime.now()
        time = now.strftime('%Y_%m_%d_%H_%M_%S')
        
        if self.up_down==0:
            result = pd.DataFrame(self.up_ans)
            result.to_excel(self.setting['result']+"/结果_%s.xlsx"%time)
            boldExcel(self.setting['result']+"/结果_%s.xlsx"%time)
        else:
            result_A = pd.DataFrame(self.down_ans[0])
            result_B = pd.DataFrame(self.down_ans[1])
            result_A.to_excel(self.setting['result']+"/下栏结果_%s.xlsx"%time)
            result_B.to_excel(self.setting['result']+"/下栏小点结果_%s.xlsx"%time)
            
            boldExcel(self.setting['result']+"/下栏结果_%s.xlsx"%time)
            boldExcel(self.setting['result']+"/下栏小点结果_%s.xlsx"%time)
            
        self.logOuter("储存结果于 %s\n"%self.setting['result'], 1)

    def settingButtonAction(self):
        print("Setting")
        self.settingSaver.show()
    
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    global main_app
    main_app = MainApp()
    main_app.show()
    sys.exit(app.exec_())