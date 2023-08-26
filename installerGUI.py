from PyQt5.QtWidgets import *
from PyQt5 import uic
import installer

class MainWindow(QMainWindow):
    __selectedProgram = []
    __programList = []
    def __init__(self, title):
        super(MainWindow, self).__init__()
        
        #load ui file
        uic.loadUi("mainwindow.ui", self)
        self.setWindowTitle(title)
        
        #define Widgets
        self.installButton = self.findChild(QPushButton, "InstallButton")
        self.tableWidget = self.findChild(QTableWidget, "tableWidget") 
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
        return
    
    def findProgram(self):
        programName = self.lineEdit.text()
        
        i, programList =0, []
        self.tableWidget.setRowCount(0)
        for item in self.__programList:
            if (programName in item[0]):
                self.tableWidget.setRowCount(i + 1)
                programName = QTableWidgetItem(item[0])
                self.tableWidget.setItem(i, 0, programName)
                version = QTableWidgetItem(item[1])
                self.tableWidget.setItem(i, 1, version)
                source = QTableWidgetItem(item[3])
                self.tableWidget.setItem(i, 2, source)
            
        
                
    def printList(self):
        self.tableWidget.setRowCount(0)
        for index, program in enumerate(self.__programList):
            self.tableWidget.setRowCount(index + 1)
            programName = QTableWidgetItem(program[0])
            self.tableWidget.setItem(index, 0, programName)
            version = QTableWidgetItem(program[1])
            self.tableWidget.setItem(index, 1, version)
            bucket = QTableWidgetItem(program[2])
            self.tableWidget.setItem(index, 2, bucket)
             
    def install(self):
        for program in self.__selectedProgram:
            if not installer.scoopInstall(program):
                print("program has already been installed!")
        
    def exit(self):
        self.close()