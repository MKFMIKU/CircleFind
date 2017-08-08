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
import cv2
from save_result import save_result

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
        self.flag = 1
        self._signal.emit("开始\n");
        self.setpath = main_app.setting['scan']
        self.respath = main_app.setting['result']
        
        detecter = DetectImage()   
        count = 0
        last_filenames = []
        self.ans = []
        while True:
            image_filenames = [self.setpath+'/'+x for x in listdir(self.setpath) if is_image_file(x)]
            need_test = list(set(image_filenames) ^ set(last_filenames))
            if self.flag == 0:
                self._signal.emit("停止\n")
                result = pd.DataFrame(self.ans)
                result.to_excel(self.respath+"/结果.xlsx")
                break;
            if len(need_test)==0:
                continue
            for f in need_test:
                im = cv2.imread(f)
                if im is None:
                    continue
                im = im[:,0:800,:]
                type = detecter.detect(im)
                print(type)
                if type==1:
                    continue
                checker = CheckImage(type)
                res,_ = checker.check(f)
                count+=1
                self.ans.extend(save_result(res,count))
                log = "scanf %s for type %d \n"%(f,type)
                last_filenames.append(f)
                self._signal.emit(log)
                
    def stop(self):
        self.flag = 0
        
class SettingApp(QtWidgets.QMainWindow, Ui_Dialog):
    def __init__(self):
        super(SettingApp, self).__init__()
        self.setupUi(self)
        self.scanFileButton.clicked.connect(self.scanFileChoose)
        self.cameraFileButton.clicked.connect(self.cameraFileChoose)
        self.resultFileButton.clicked.connect(self.resultFileChoose)
        self.closeButton.clicked.connect(self.closeAction)
        self.saveButton.clicked.connect(self.saveAction)
        self.scanFile = ""
        self.cameraFile = ""
        self.resultFile = ""
    
    def init_ui(self):
        self.scanFilePath.setText(self.scanFile)
        self.cameraFilePath.setText(self.cameraFile)
        self.resultFilePath.setText(self.resultFile)
        
    def showEvent(self, event):
        with open('setting.yml') as f:
            self.setting = yaml.safe_load(f)
            self.scanFile = self.setting['scan']
            self.cameraFile = self.setting['camera']
            self.resultFile = self.setting['result']
            self.init_ui()
            
    def saveAction(self):
        data = dict(
            scan = self.scanFile,
            camera = self.cameraFile,
            result = self.resultFile
        )
        with open('setting.yml', 'w') as outfile:
            yaml.dump(data, outfile, default_flow_style=False)
        self.close()
        
    def closeAction(self):
        self.close()
        
    def scanFileChoose(self):
        self.scanFile = QtWidgets.QFileDialog.getExistingDirectory()
        self.scanFilePath.setText(self.scanFile)
        
    def cameraFileChoose(self):
        self.cameraFile = QtWidgets.QFileDialog.getExistingDirectory()
        self.cameraFilePath.setText(self.cameraFile)
        
    def resultFileChoose(self):
        self.resultFile = QtWidgets.QFileDialog.getExistingDirectory()
        self.resultFilePath.setText(self.resultFile)
        

class MainApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainApp, self).__init__()
        self.setupUi(self)
        
        self.settingSaver = SettingApp()
        self.startButton.clicked.connect(self.startButtonAction)
        self.stopButton.clicked.connect(self.stopButtonAction)
        self.settingButton.clicked.connect(self.settingButtonAction)
        with open('setting.yml') as f:
            self.setting = yaml.safe_load(f)
    
    def logOuter(self, text):
        """Append text to the QTextEdit."""
        # Maybe QTextEdit.append() works as well, but this is how I do it:
        cursor = self.textBrowser.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        cursor.insertText(text)
        self.textBrowser.setTextCursor(cursor)
        self.textBrowser.ensureCursorVisible()
        
    def startButtonAction(self):
        print("Start")
        self.thread = Runthread()
        self.thread._signal.connect(self.logOuter)
        self.thread.start()
        
    def stopButtonAction(self):
        print("Stop")
        self.thread.stop()
        
    def settingButtonAction(self):
        print("Setting")
        self.settingSaver.show()
    
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    global main_app
    main_app = MainApp()
    main_app.show()
    sys.exit(app.exec_())