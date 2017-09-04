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
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setEnabled(True)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout.setContentsMargins(24, 24, 24, 24)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.startButton = QtWidgets.QPushButton(self.centralWidget)
        self.startButton.setMinimumSize(QtCore.QSize(50, 50))
        self.startButton.setMaximumSize(QtCore.QSize(50, 50))
        self.startButton.setBaseSize(QtCore.QSize(50, 50))
        self.startButton.setAutoFillBackground(False)
        self.startButton.setStyleSheet("border-image: url(:/new/outer/start.png)")
        self.startButton.setText("")
        self.startButton.setObjectName("startButton")
        self.verticalLayout.addWidget(self.startButton)
        self.label = QtWidgets.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.stopButton = QtWidgets.QPushButton(self.centralWidget)
        self.stopButton.setMinimumSize(QtCore.QSize(50, 50))
        self.stopButton.setMaximumSize(QtCore.QSize(50, 50))
        self.stopButton.setStyleSheet("border-image: url(:/new/outer/stop.png)")
        self.stopButton.setText("")
        self.stopButton.setObjectName("stopButton")
        self.verticalLayout_2.addWidget(self.stopButton)
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton.setStyleSheet("border-image: url(:/new/outer/up.png)")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_3.addWidget(self.pushButton)
        self.label_6 = QtWidgets.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_3.addWidget(self.label_6)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_2.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton_2.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_2.setStyleSheet("border-image: url(:/new/outer/down.png)")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_4.addWidget(self.pushButton_2)
        self.label_7 = QtWidgets.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_4.addWidget(self.label_7)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.scanButton = QtWidgets.QPushButton(self.centralWidget)
        self.scanButton.setMinimumSize(QtCore.QSize(50, 50))
        self.scanButton.setMaximumSize(QtCore.QSize(50, 50))
        self.scanButton.setStyleSheet("border-image: url(:/new/outer/scan.png)")
        self.scanButton.setText("")
        self.scanButton.setObjectName("scanButton")
        self.verticalLayout_5.addWidget(self.scanButton)
        self.label_3 = QtWidgets.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_5.addWidget(self.label_3)
        self.horizontalLayout.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_6.setSpacing(6)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.cameraButton = QtWidgets.QPushButton(self.centralWidget)
        self.cameraButton.setMinimumSize(QtCore.QSize(50, 50))
        self.cameraButton.setMaximumSize(QtCore.QSize(50, 50))
        self.cameraButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.cameraButton.setStyleSheet("border-image: url(:/new/outer/camera.png)")
        self.cameraButton.setText("")
        self.cameraButton.setObjectName("cameraButton")
        self.verticalLayout_6.addWidget(self.cameraButton)
        self.label_4 = QtWidgets.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_6.addWidget(self.label_4)
        self.horizontalLayout.addLayout(self.verticalLayout_6)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_7.setSpacing(6)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.settingButton = QtWidgets.QPushButton(self.centralWidget)
        self.settingButton.setMinimumSize(QtCore.QSize(50, 50))
        self.settingButton.setMaximumSize(QtCore.QSize(50, 50))
        self.settingButton.setStyleSheet("border-image: url(:/new/outer/set.png)")
        self.settingButton.setText("")
        self.settingButton.setObjectName("settingButton")
        self.verticalLayout_7.addWidget(self.settingButton)
        self.label_5 = QtWidgets.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_7.addWidget(self.label_5)
        self.horizontalLayout.addLayout(self.verticalLayout_7)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setStyleSheet("color: blue")
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 1, 0, 1, 1)
        self.clearLog = QtWidgets.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setUnderline(True)
        self.clearLog.setFont(font)
        self.clearLog.setStyleSheet("color: blue")
        self.clearLog.setObjectName("clearLog")
        self.gridLayout.addWidget(self.clearLog, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        self.startButton.clicked.connect(MainWindow.startButton)
        self.stopButton.clicked.connect(MainWindow.stopButton)
        self.settingButton.clicked.connect(MainWindow.settingButton)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "OCR识别软件beta.01版"))
        self.label.setText(_translate("MainWindow", "开始"))
        self.label_2.setText(_translate("MainWindow", "停止"))
        self.label_6.setText(_translate("MainWindow", "上栏"))
        self.label_7.setText(_translate("MainWindow", "下栏"))
        self.label_3.setText(_translate("MainWindow", "扫描仪"))
        self.label_4.setText(_translate("MainWindow", "高拍仪"))
        self.label_5.setText(_translate("MainWindow", "设置"))
        self.clearLog.setText(_translate("MainWindow", "清空记录"))

