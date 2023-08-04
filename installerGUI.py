from PyQt5.QtWidgets import *
from PyQt5.QtCore import QSize
from PyQt5 import uic
import installer

class MainWindow(QMainWindow):
    __installModule = []
    def __init__(self, title):
        super(MainWindow, self).__init__()
        
        #load ui file
        uic.loadUi("mainwindow.ui", self)
        self.setWindowTitle(title)
        
        #define Widgets
        self.installButton = self.findChild(QPushButton, "InstallButton")
        self.listWidget = self.findChild(QListWidget, "listWidget") 
        self.lineEdit = self.findChild(QLineEdit, "lineEdit")  
        self.actionFindBucket = self.findChild(QAction, "actionFindBucket") 
        self.actionExit = self.findChild(QAction, "actionExit")
        
        #connect signal-slots
        self.installButton.clicked.connect(self.install)
        self.lineEdit.textEdited.connect(self.findProgram)
        self.actionFindBucket.triggered.connect(self.findBucket)
        self.actionExit.triggered.connect(self.exit)
        
        self.show()
        
    def findBucket(self):
        print("findBucket")
    
    def findProgram(self):
        print("findProgram")
        
    def printList(self):
        return
    
    def install(self):
        print("install")
        
    def exit(self):
        self.close()