# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(525, 402)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setEnabled(True)
        self.centralWidget.setObjectName("centralWidget")
        self.startButton = QtWidgets.QPushButton(self.centralWidget)
        self.startButton.setGeometry(QtCore.QRect(30, 20, 40, 40))
        self.startButton.setAutoFillBackground(False)
        self.startButton.setStyleSheet("border-image: url(:/new/outer/start.png)")
        self.startButton.setText("")
        self.startButton.setObjectName("startButton")
        self.stopButton = QtWidgets.QPushButton(self.centralWidget)
        self.stopButton.setGeometry(QtCore.QRect(90, 20, 40, 40))
        self.stopButton.setStyleSheet("border-image: url(:/new/outer/stop.png)")
        self.stopButton.setText("")
        self.stopButton.setObjectName("stopButton")
        self.scanButton = QtWidgets.QPushButton(self.centralWidget)
        self.scanButton.setGeometry(QtCore.QRect(310, 20, 40, 40))
        self.scanButton.setStyleSheet("border-image: url(:/new/outer/scan.png)")
        self.scanButton.setText("")
        self.scanButton.setObjectName("scanButton")
        self.cameraButton = QtWidgets.QPushButton(self.centralWidget)
        self.cameraButton.setGeometry(QtCore.QRect(380, 20, 40, 40))
        self.cameraButton.setStyleSheet("border-image: url(:/new/outer/camera.png)")
        self.cameraButton.setText("")
        self.cameraButton.setObjectName("cameraButton")
        self.settingButton = QtWidgets.QPushButton(self.centralWidget)
        self.settingButton.setGeometry(QtCore.QRect(440, 20, 40, 40))
        self.settingButton.setStyleSheet("border-image: url(:/new/outer/set.png)")
        self.settingButton.setText("")
        self.settingButton.setObjectName("settingButton")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralWidget)
        self.textBrowser.setGeometry(QtCore.QRect(30, 100, 451, 231))
        self.textBrowser.setObjectName("textBrowser")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(40, 70, 31, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(100, 70, 31, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralWidget)
        self.label_3.setGeometry(QtCore.QRect(310, 70, 41, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralWidget)
        self.label_4.setGeometry(QtCore.QRect(380, 70, 60, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralWidget)
        self.label_5.setGeometry(QtCore.QRect(440, 70, 31, 16))
        self.label_5.setObjectName("label_5")
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "OCR识别软件beta.01版"))
        self.label.setText(_translate("MainWindow", "开始"))
        self.label_2.setText(_translate("MainWindow", "停止"))
        self.label_3.setText(_translate("MainWindow", "扫描仪"))
        self.label_4.setText(_translate("MainWindow", "高拍仪"))
        self.label_5.setText(_translate("MainWindow", "设置"))

