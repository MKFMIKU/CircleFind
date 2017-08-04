#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 15:02:07 2017

@author: kangfu
"""

from PyQt5 import QtWidgets, QtGui
import sys
import yaml

from gui.mainwindowUI import Ui_MainWindow
from gui.dialogUI import Ui_Dialog
import gui.outfile

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
        
        self.setting = SettingApp()
        self.startButton.clicked.connect(self.startButtonAction)
        self.stopButton.clicked.connect(self.stopButtonAction)
        self.settingButton.clicked.connect(self.settingButtonAction)
        
    def startButtonAction(self):
        print("Start")
        
    def stopButtonAction(self):
        print("Stop")
        
    def settingButtonAction(self):
        print("Setting")
        self.setting.show()
    
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_app = MainApp()
    main_app.show()
    sys.exit(app.exec_())