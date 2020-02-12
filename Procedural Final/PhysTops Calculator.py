# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sir.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
#from s2 import *
from Onedkm import *
from Twodkm import *
from Bfnet import *
from Ifnet import *
#from OnedM import *
from CircMot import *
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog, QWidget, QLabel, QInputDialog, QLineEdit, QMessageBox, QGridLayout, QFrame, QFileDialog
from PyQt5.QtGui import QIcon

class Ui_MainWindow(object):
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 750)
        MainWindow.setStyleSheet("background-color: rgb(52, 96, 148);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.label_main = QtWidgets.QLabel(self.centralwidget)
        self.label_main.setGeometry(QtCore.QRect(245, 50, 510, 90))
        self.label_main.setObjectName("label")
        self.label_main.setWordWrap(True)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_main.setFont(font)
        self.label_main.setAlignment(QtCore.Qt.AlignCenter)
        self.label_main.setStyleSheet("background-color: rgb(213, 126, 0);")
        
        self.solveButton1dk = QtWidgets.QPushButton(self.centralwidget)
        self.solveButton1dk.setGeometry(QtCore.QRect(245, 150, 250, 100))
        self.solveButton1dk.setObjectName("solveButton1dk")
        self.solveButton1dk.setStyleSheet("background-color: rgb(213, 126, 0);")
        self.solveButton1dk.clicked.connect(self.Main1)
        
        
        self.solveButton2dk = QtWidgets.QPushButton(self.centralwidget)
        self.solveButton2dk.setGeometry(QtCore.QRect(505, 150, 250, 100))
        self.solveButton2dk.setObjectName("solveButton1dk")
        self.solveButton2dk.setStyleSheet("background-color: rgb(213, 126, 0);")
        self.solveButton2dk.clicked.connect(self.Main2)
        
        self.solveButtonbfnet = QtWidgets.QPushButton(self.centralwidget)
        self.solveButtonbfnet.setGeometry(QtCore.QRect(245, 260, 250, 100))
        self.solveButtonbfnet.setObjectName("solveButton1dk")
        self.solveButtonbfnet.setStyleSheet("background-color: rgb(213, 126, 0);")
        self.solveButtonbfnet.clicked.connect(self.Main3)
        
        self.solveButtonifnet = QtWidgets.QPushButton(self.centralwidget)
        self.solveButtonifnet.setGeometry(QtCore.QRect(505, 260, 250, 100))
        self.solveButtonifnet.setObjectName("solveButton1dk")
        self.solveButtonifnet.setStyleSheet("background-color: rgb(213, 126, 0);")
        self.solveButtonifnet.clicked.connect(self.Main4)
        
        self.solveButton2dm = QtWidgets.QPushButton(self.centralwidget)
        self.solveButton2dm.setGeometry(QtCore.QRect(245, 370, 250, 100))
        self.solveButton2dm.setObjectName("solveButton1dk")
        self.solveButton2dm.setStyleSheet("background-color: rgb(213, 126, 0);")
        self.solveButton2dm.clicked.connect(self.Main6)
        
        self.exitButton = QtWidgets.QPushButton(self.centralwidget)
        self.exitButton.setGeometry(QtCore.QRect(505, 370, 250, 100))
        self.exitButton.setObjectName("solveButton1dk")
        self.exitButton.setStyleSheet("background-color: rgb(213, 126, 0);")
        self.exitButton.clicked.connect(self.clicked_exit)
        
        MainWindow.setCentralWidget(self.centralwidget)
      
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
       
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Phystops for Phonies"))
        
        self.label_main.setText(_translate("MainWindow", "PhysTops for the Illiterate"))
        self.solveButton1dk.setStatusTip(_translate("MainWindow", "1D Kinematics"))
        self.solveButton1dk.setText(_translate("MainWindow", "One Dimensional\n"
"Kinematics"))
        self.solveButton1dk.setShortcut(_translate("MainWindow", "1"))
        
        self.solveButton2dk.setStatusTip(_translate("MainWindow", "2D Kinematics"))
        self.solveButton2dk.setText(_translate("MainWindow", "Two Dimensional\n"
"Kinematics"))
        self.solveButton2dk.setShortcut(_translate("MainWindow", "2"))
        
        self.solveButtonbfnet.setStatusTip(_translate("MainWindow", "Basic Forces"))
        self.solveButtonbfnet.setText(_translate("MainWindow", "Basic Forces"))
        self.solveButtonbfnet.setShortcut(_translate("MainWindow", "3"))
        
        self.solveButtonifnet.setStatusTip(_translate("MainWindow", "Inclined Forces"))
        self.solveButtonifnet.setText(_translate("MainWindow", "Inclined Forces"))
        self.solveButtonifnet.setShortcut(_translate("MainWindow", "3"))
                
        self.solveButton2dm.setStatusTip(_translate("MainWindow", "Circular Motion"))
        self.solveButton2dm.setText(_translate("MainWindow", "Circular Motion"))
        self.solveButton2dm.setShortcut(_translate("MainWindow", "3"))
        
        self.exitButton.setStatusTip(_translate("MainWindow", "Close Application"))
        self.exitButton.setText(_translate("MainWindow", "Close Application"))
        self.exitButton.setShortcut(_translate("MainWindow", "3"))
        
    def Main1(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow1()
        self.ui.setup(self.window)
        self.window.show()
    
    def Main2(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow2()
        self.ui.setup(self.window)
        self.window.show()
    
    def Main3(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow3()
        self.ui.setup(self.window)
        self.window.show()
    
    def Main4(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow4()
        self.ui.setup(self.window)
        self.window.show()
    
    def Main5(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow5()
        self.ui.setup(self.window)
        self.window.show()
    
    def Main6(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow6()
        self.ui.setup(self.window)
        self.window.show()
        
    def clicked_exit(self):
        sys.exit()   
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
