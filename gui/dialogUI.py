# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 150, 60, 16))
        self.label_4.setObjectName("label_4")
        self.saveButton = QtWidgets.QPushButton(Dialog)
        self.saveButton.setGeometry(QtCore.QRect(100, 230, 71, 32))
        self.saveButton.setObjectName("saveButton")
        self.closeButton = QtWidgets.QPushButton(Dialog)
        self.closeButton.setGeometry(QtCore.QRect(222, 230, 81, 32))
        self.closeButton.setObjectName("closeButton")
        self.scanSwitch = QtWidgets.QPushButton(Dialog)
        self.scanSwitch.setGeometry(QtCore.QRect(130, 140, 113, 32))
        self.scanSwitch.setObjectName("scanSwitch")
        self.cameraSwitch = QtWidgets.QPushButton(Dialog)
        self.cameraSwitch.setGeometry(QtCore.QRect(250, 140, 113, 32))
        self.cameraSwitch.setObjectName("cameraSwitch")
        self.scanFilePath = QtWidgets.QTextBrowser(Dialog)
        self.scanFilePath.setGeometry(QtCore.QRect(170, 40, 211, 21))
        self.scanFilePath.setObjectName("scanFilePath")
        self.cameraFilePath = QtWidgets.QTextBrowser(Dialog)
        self.cameraFilePath.setGeometry(QtCore.QRect(170, 70, 211, 21))
        self.cameraFilePath.setObjectName("cameraFilePath")
        self.resultFilePath = QtWidgets.QTextBrowser(Dialog)
        self.resultFilePath.setGeometry(QtCore.QRect(170, 100, 211, 21))
        self.resultFilePath.setObjectName("resultFilePath")
        self.scanFileButton = QtWidgets.QPushButton(Dialog)
        self.scanFileButton.setGeometry(QtCore.QRect(10, 40, 131, 32))
        self.scanFileButton.setObjectName("scanFileButton")
        self.cameraFileButton = QtWidgets.QPushButton(Dialog)
        self.cameraFileButton.setGeometry(QtCore.QRect(10, 70, 131, 32))
        self.cameraFileButton.setObjectName("cameraFileButton")
        self.resultFileButton = QtWidgets.QPushButton(Dialog)
        self.resultFileButton.setGeometry(QtCore.QRect(10, 100, 131, 32))
        self.resultFileButton.setObjectName("resultFileButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "OCR识别软件beta.01版 设置"))
        self.label_4.setText(_translate("Dialog", "默认设备："))
        self.saveButton.setText(_translate("Dialog", "保存"))
        self.closeButton.setText(_translate("Dialog", "关闭"))
        self.scanSwitch.setText(_translate("Dialog", "扫描仪"))
        self.cameraSwitch.setText(_translate("Dialog", "高拍仪"))
        self.scanFileButton.setText(_translate("Dialog", "扫描仪存储路径："))
        self.cameraFileButton.setText(_translate("Dialog", "高拍仪存储路径："))
        self.resultFileButton.setText(_translate("Dialog", "结果存储路径："))

