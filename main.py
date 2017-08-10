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

from detect_image import DetectImage
from check_image import CheckImage
from gui.mainwindowUI import Ui_MainWindow
from gui.dialogUI import Ui_Dialog
import gui.outfile

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
            for f in need_test:
                log = f
                if main_app.begin_run == 1:
                    self._signal.emit("开始检测 %s"%f)
                    im = cv2.imread(f)
                    if im is None:
                        self._signal.emit("读取 %s 错误"%f)
                        continue
                    im = im[:,0:800,:]
                    type = detecter.detect(im)
                    checker = CheckImage(type)
                    res,_,err = checker.check(f)
                    if err==1:
                        self._signal.emit("%s 图片错误 无法识别"%f)
                        log += "识别错误"
                        res = [-1000]
                    else:
                        self._signal.emit("检查 %s 结束 种类为：%d"%(f,type))
                    main_app.count+=1
                    print( main_app.ans)
                    main_app.ans.extend(save_result(res,log))
                    main_app.last_filenames.append(f)
                else:
                    break
            if  main_app.begin_run == 0:
                break

class MainApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainApp, self).__init__()
        self.begin_run = 0
        self.devices = 0
        self.count = 0
        self.ans = []
        self.last_filenames = []
        self.setupUi(self)
        self.settingSaver = SettingApp()
        self.textEdit.setReadOnly(True)
        self.startButton.clicked.connect(self.startButtonAction)
        self.stopButton.clicked.connect(self.stopButtonAction)
        self.settingButton.clicked.connect(self.settingButtonAction)
        self.scanButton.clicked.connect(self.switch_devices)
        self.cameraButton.clicked.connect(self.switch_devices)
        self._update()

    def _update(self):
        with open('setting.yml') as f:
            self.setting = yaml.safe_load(f)
        if self.devices == 0:
            self.scanButton.setStyleSheet("border-image: url(:/new/outer/scan.png)")
            self.cameraButton.setStyleSheet("border-image: url(:/new/outer/camera_black.png)")
            self.path = self.setting['scan']
        else:
            self.scanButton.setStyleSheet("border-image: url(:/new/outer/scan_off.png)")
            self.cameraButton.setStyleSheet("border-image: url(:/new/outer/camera.png)")
            self.path = self.setting['camera']
    
    def switch_devices(self):
        _translate = QtCore.QCoreApplication.translate
        if self.begin_run==1:
            self.begin_run = 0
            self.startButton.setStyleSheet("border-image: url(:/new/outer/start_off.png)")
            self.label.setText(_translate("MainWindow", "开始"))
        if self.devices == 0:
            self.devices =1
            self.logOuter("切换为高拍仪")
        else:
            self.devices =0
            self.logOuter("切换为扫描仪")
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
        self.thread = Runthread()
        self.thread._signal.connect(self.logOuter)
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
        result = pd.DataFrame(self.ans)
        result.to_excel(self.setting['result']+"/结果_%s.xlsx"%time)
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