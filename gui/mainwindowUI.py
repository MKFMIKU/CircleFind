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
        MainWindow.resize(800, 600)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setEnabled(True)
        self.centralWidget.setObjectName("centralWidget")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(45, 80, 50, 24))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(140, 80, 50, 24))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralWidget)
        self.label_3.setGeometry(QtCore.QRect(530, 80, 80, 24))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralWidget)
        self.label_4.setGeometry(QtCore.QRect(620, 80, 80, 24))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralWidget)
        self.label_5.setGeometry(QtCore.QRect(695, 80, 80, 24))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.textEdit = QtWidgets.QTextEdit(self.centralWidget)
        self.textEdit.setGeometry(QtCore.QRect(20, 110, 760, 460))
        self.textEdit.setObjectName("textEdit")
        self.upButton = QtWidgets.QPushButton(self.centralWidget)
        self.upButton.setGeometry(QtCore.QRect(250, 20, 50, 50))
        self.upButton.setStyleSheet("border-image: url(:/new/outer/up.png)")
        self.upButton.setText("")
        self.upButton.setObjectName("upButton")
        self.downButton = QtWidgets.QPushButton(self.centralWidget)
        self.downButton.setGeometry(QtCore.QRect(330, 20, 50, 50))
        self.downButton.setStyleSheet("border-image: url(:/new/outer/down_black.png)")
        self.downButton.setText("")
        self.downButton.setObjectName("downButton")
        self.label_6 = QtWidgets.QLabel(self.centralWidget)
        self.label_6.setGeometry(QtCore.QRect(250, 80, 50, 24))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralWidget)
        self.label_7.setGeometry(QtCore.QRect(335, 80, 50, 24))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.cameraButton = QtWidgets.QPushButton(self.centralWidget)
        self.cameraButton.setGeometry(QtCore.QRect(620, 20, 50, 50))
        self.cameraButton.setStyleSheet("border-image: url(:/new/outer/camera.png)")
        self.cameraButton.setText("")
        self.cameraButton.setObjectName("cameraButton")
        self.scanButton = QtWidgets.QPushButton(self.centralWidget)
        self.scanButton.setGeometry(QtCore.QRect(530, 20, 50, 50))
        self.scanButton.setStyleSheet("border-image: url(:/new/outer/scan.png)")
        self.scanButton.setText("")
        self.scanButton.setObjectName("scanButton")
        self.stopButton = QtWidgets.QPushButton(self.centralWidget)
        self.stopButton.setGeometry(QtCore.QRect(130, 20, 50, 50))
        self.stopButton.setStyleSheet("border-image: url(:/new/outer/stop_off.png)")
        self.stopButton.setText("")
        self.stopButton.setObjectName("stopButton")
        self.startButton = QtWidgets.QPushButton(self.centralWidget)
        self.startButton.setGeometry(QtCore.QRect(40, 20, 50, 50))
        self.startButton.setAutoFillBackground(False)
        self.startButton.setStyleSheet("border-image: url(:/new/outer/start_off.png)")
        self.startButton.setText("")
        self.startButton.setObjectName("startButton")
        self.settingButton = QtWidgets.QPushButton(self.centralWidget)
        self.settingButton.setGeometry(QtCore.QRect(690, 20, 50, 50))
        self.settingButton.setStyleSheet("border-image: url(:/new/outer/set.png)")
        self.settingButton.setText("")
        self.settingButton.setObjectName("settingButton")
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
        self.label_6.setText(_translate("MainWindow", "上栏"))
        self.label_7.setText(_translate("MainWindow", "下栏"))

