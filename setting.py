from PyQt5 import QtWidgets, QtGui, QtCore
import yaml
from gui.dialogUI import Ui_Dialog

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