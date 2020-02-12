# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 's2.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import math
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow1(object):
    def setup(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 400)
        MainWindow.setStyleSheet("background-color: rgb(52, 96, 148);")


        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.calc_button = QtWidgets.QPushButton(self.centralwidget)
        self.calc_button.setGeometry(QtCore.QRect(225, 300, 150, 50))
        self.calc_button.setObjectName("solveButton1dk")
        self.calc_button.setStyleSheet("background-color: rgb(213, 126, 0);")
        self.calc_button.clicked.connect(self.calculate)
        
        #Creating Labels for the Gui
        self.label_inform = QtWidgets.QLabel(self.centralwidget)
        self.label_inform.setGeometry(QtCore.QRect(10, 10, 580, 50))
        self.label_inform.setObjectName("label")
        self.label_inform.setWordWrap(True)
        self.label_inform.setStyleSheet("background-color: rgb(213, 126, 0);")
        
        self.label_dx = QtWidgets.QLabel(self.centralwidget)
        self.label_dx.setGeometry(QtCore.QRect(10, 65, 80, 30))
        self.label_dx.setObjectName("label")
        self.label_dx.setWordWrap(True)
        self.label_dx.setStyleSheet("background-color: rgb(213, 126, 0);")
        
        self.label_vi = QtWidgets.QLabel(self.centralwidget)
        self.label_vi.setGeometry(QtCore.QRect(10, 100, 80, 30))
        self.label_vi.setObjectName("label")
        self.label_vi.setWordWrap(True)
        self.label_vi.setStyleSheet("background-color: rgb(213, 126, 0);")
        
        self.label_vf = QtWidgets.QLabel(self.centralwidget)
        self.label_vf.setGeometry(QtCore.QRect(10, 135, 80, 30))
        self.label_vf.setObjectName("label")
        self.label_vf.setWordWrap(True)
        self.label_vf.setStyleSheet("background-color: rgb(213, 126, 0);")
        
        self.label_a = QtWidgets.QLabel(self.centralwidget)
        self.label_a.setGeometry(QtCore.QRect(10, 170, 80, 30))
        self.label_a.setObjectName("label")
        self.label_a.setWordWrap(True)
        self.label_a.setStyleSheet("background-color: rgb(213, 126, 0);")
        
        self.label_t = QtWidgets.QLabel(self.centralwidget)
        self.label_t.setGeometry(QtCore.QRect(10, 205, 80, 30))
        self.label_t.setObjectName("label")
        self.label_t.setWordWrap(True)
        self.label_t.setStyleSheet("background-color: rgb(213, 126, 0);")
        
        self.label_u = QtWidgets.QLabel(self.centralwidget)
        self.label_u.setGeometry(QtCore.QRect(10, 240, 80, 30))
        self.label_u.setObjectName("label")
        self.label_u.setWordWrap(True)
        self.label_u.setStyleSheet("background-color: rgb(213, 126, 0);")
        
        self.label_as = QtWidgets.QLabel(self.centralwidget)
        self.label_as.setGeometry(QtCore.QRect(270, 65, 150, 100))
        self.label_as.setObjectName("label")
        self.label_as.setWordWrap(True)
        self.label_as.setStyleSheet("background-color: rgb(213, 126, 0);")
        #Creating LineEdits for the Gui
        
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(95, 65, 170, 31))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setPlaceholderText("meters")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(95, 100, 170, 31))
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setPlaceholderText("meters/second")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(95, 135, 170, 31))
        self.lineEdit_3.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setPlaceholderText("meters/second")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(95, 170, 170, 31))
        self.lineEdit_4.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_4.setPlaceholderText("meters/second^2")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(95, 205, 170, 31))
        self.lineEdit_5.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_5.setPlaceholderText("seconds")
        self.lineEdit_u = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_u.setGeometry(QtCore.QRect(95, 240, 170, 31))
        self.lineEdit_u.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.lineEdit_u.setObjectName("lineEdit_u")
        self.lineEdit_u.setPlaceholderText("Vi, Vf, a, t, dx")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Solve 1D Kinematics"))
        
        self.calc_button.setStatusTip(_translate("MainWindow", "1D Kinematics"))
        self.calc_button.setText(_translate("MainWindow", "One Dimensional\n"
"Kinematics"))
        self.calc_button.setShortcut(_translate("MainWindow", "1"))
        
        self.label_inform.setText(_translate("MainWindow", "In order to solve a 1D Kinematics problem, three of the five variables"
        " listed must be present to calculate a missing one. The program will alert you if a specific combination does not yield feasible calculations. Acceleration is assumed to be constant."))
        self.label_dx.setText(_translate("MainWindow", "Delta X"))
        self.label_vi.setText(_translate("MainWindow", "Initial Velocity"))
        self.label_vf.setText(_translate("MainWindow", "Final Velocity"))
        self.label_a.setText(_translate("MainWindow", "Acceleration"))
        self.label_t.setText(_translate("MainWindow", "Time"))
        self.label_u.setText(_translate("MainWindow", "Unknown"))
        self.label_as.setText(_translate("MainWindow", "Answer"))
        
        
    def calculate(self):
        print("Hello")
        
        def number(s):
            try:
                float(s)
                return True
            except ValueError:
                return False
        dx = self.lineEdit.text()
        if number(dx):
            dx = float(dx)    
        t = self.lineEdit_5.text()
        if number(t):
            t = float(t)
        Vi = self.lineEdit_2.text()
        if number(Vi):
            Vi = float(Vi)
        Vf = self.lineEdit_3.text()
        if number(Vf):
            Vf = float(Vf)
        a = self.lineEdit_4.text()
        if number(a):
            a = float(a)
        bruh = ['Vi', 'Vf', 'a', 't', 'dx']
        unknown = self.lineEdit_u.text()
        wow = True
        geez = "You don't quite have the facilites for that mate"
        while wow:
            if unknown not in bruh:
                print("We don't have the facilities for that mate")
                self.label_as.setText("Answer:" + geez)
                wow = False
            if unknown == 'dx':
                if (type(Vi) == float and type(a) == float and type(t) == float): 
                    dx = Vi*t + (a*t**2)/2
                    self.label_as.setText("Answer:" + str(dx))
                    wow = False
                elif (type(Vf) == float and type(a) == float and type(t) == float): 
                    dx = Vf*t - (a*t**2)/2
                    self.label_as.setText("Answer:" + str(dx))
                    wow = False
                elif (type(Vi) == float and type(a) == float and type(Vf) == float):
                    dx = (Vf**2 - Vi**2)/(2*a)
                    self.label_as.setText("Answer:" + str(dx))
                    wow = False
                else:
                    print("You don't quite have the facilites for that mate")
                    self.label_as.setText("Answer:" + geez)
                    wow = False
            if unknown == 'Vi':
                if (type(a) == float and type(t) == float and type(Vf) == float): 
                    Vi = Vf - a*t
                    self.label_as.setText("Answer:" + str(Vi))
                    wow = False
                elif (type(t) == float and type(a) == float and type(dx) == float):
                    Vi = (2*dx - a*t**2)/(2*t)
                    self.label_as.setText("Answer:" + str(Vi))
                    wow = False
                elif (type(dx) == float and type(a) == float and type(Vf) == float):
                    Vi = math.sqrt(Vf**2-(2*a*dx))
                    self.label_as.setText("Answer:" + str(Vi))
                    wow = False
                else:
                    print("You don't quite have the facilites for that mate")
                    self.label_as.setText("Answer:" + geez)
                    wow = False
            if unknown == 'Vf':
                if (type(a) == float and type(t) == float and type(Vi) == float): 
                    Vf = Vi + a*t
                    self.label_as.setText("Answer:" + str(Vf))
                    wow = False
                elif (type(dx) == float and type(a) == float and type(Vi) == float):
                    Vf = math.sqrt(Vf**2+(2*a*dx))
                    self.label_as.setText("Answer:" + str(Vf))
                    wow = False
                else:
                    print("You don't quite have the facilites for that mate")
                    self.label_as.setText("Answer:" + geez)
                    wow = False
            if unknown == 'a':
                if (type(Vi) == float and type(Vf) == float and type(t) == float): 
                    a = (Vf - Vi)/t
                    self.label_as.setText("Answer:" + str(a))
                    wow = False
                elif (type(Vi) == float and type(dx) == float and type(Vf) == float):
                    a = (Vf**2 - Vi**2)/(2*dx)
                    self.label_as.setText("Answer:" + str(a))
                    wow = False
                elif (type(dx) == float and type(t) == float and type(Vi) == float):
                    a = (2*(dx - Vi * t))/(t**2)
                    self.label_as.setText("Answer:" + str(a))
                    wow = False
                else:
                    print("You don't quite have the facilites for that mate")
                    self.label_as.setText("Answer:" + geez)
                    wow = False
            if unknown == 't':
                if (type(Vi) == float and type(Vf) == float and type(a) == float): 
                    t = (Vf - Vi)/a
                    self.label_as.setText("Answer:" + str(t))
                    wow = False
                elif (type(Vi) == float and type(dx) == float and type(Vf) == float):
                    t1 = (-1*Vi + math.sqrt((Vi)**2 - 4*(a/2)*(-dx)))/a
                    t2 = (-1*Vi - math.sqrt((Vi)**2 - 4*(a/2)*(-dx)))/a
                    if (t1 > 0 and t2 < 0):
                        t = t1
                    elif (t1 < 0 and t2 > 0):
                        t = t2
                    elif t1 == t2:
                        t = t1
                    self.label_as.setText("Answer:" + str(t))
                    wow = False
                else:
                    print("You don't quite have the facilites for that mate")
                    self.label_as.setText("Answer:" + geez)
                    wow = False
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow1()
    ui.setup(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
