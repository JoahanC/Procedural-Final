# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 's2.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import math
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow4(object):
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
        
        self.label_inform = QtWidgets.QLabel(self.centralwidget)
        self.label_inform.setGeometry(QtCore.QRect(10, 10, 580, 50))
        self.label_inform.setObjectName("label")
        self.label_inform.setWordWrap(True)
        self.label_inform.setStyleSheet("background-color: rgb(213, 126, 0);")
        
        self.label_answer = QtWidgets.QLabel(self.centralwidget)
        self.label_answer.setGeometry(QtCore.QRect(270, 170, 255, 100))
        self.label_answer.setObjectName("label")
        self.label_answer.setWordWrap(True)
        self.label_answer.setStyleSheet("background-color: rgb(213, 126, 0);")

        self.label_dir = QtWidgets.QLabel(self.centralwidget)
        self.label_dir.setGeometry(QtCore.QRect(10, 65, 90, 30))
        self.label_dir.setObjectName("label")
        self.label_dir.setWordWrap(True)
        self.label_dir.setStyleSheet("background-color: rgb(213, 126, 0);")
        
        #self.label_col = QtWidgets.QLabel(self.centralwidget)
        #self.label_col.setGeometry(QtCore.QRect(10, 100, 90, 30))
        #self.label_col.setObjectName("label")
        #self.label_col.setWordWrap(True)
        #self.label_col.setStyleSheet("background-color: rgb(213, 126, 0);")
        
        self.label_fext = QtWidgets.QLabel(self.centralwidget)
        self.label_fext.setGeometry(QtCore.QRect(10, 100, 90, 30))
        self.label_fext.setObjectName("label")
        self.label_fext.setWordWrap(True)
        self.label_fext.setStyleSheet("background-color: rgb(213, 126, 0);")
        
        self.label_fn = QtWidgets.QLabel(self.centralwidget)
        self.label_fn.setGeometry(QtCore.QRect(10, 135, 90, 30))
        self.label_fn.setObjectName("label")
        self.label_fn.setWordWrap(True)
        self.label_fn.setStyleSheet("background-color: rgb(213, 126, 0);")
        
        self.label_fg = QtWidgets.QLabel(self.centralwidget)
        self.label_fg.setGeometry(QtCore.QRect(10, 170, 90, 30))
        self.label_fg.setObjectName("label")
        self.label_fg.setWordWrap(True)
        self.label_fg.setStyleSheet("background-color: rgb(213, 126, 0);")
        
        self.label_theta = QtWidgets.QLabel(self.centralwidget)
        self.label_theta.setGeometry(QtCore.QRect(10, 205, 90, 30))
        self.label_theta.setObjectName("label")
        self.label_theta.setWordWrap(True)
        self.label_theta.setStyleSheet("background-color: rgb(213, 126, 0);")
        
        self.label_m = QtWidgets.QLabel(self.centralwidget)
        self.label_m.setGeometry(QtCore.QRect(270, 65, 90, 30))
        self.label_m.setObjectName("label")
        self.label_m.setWordWrap(True)
        self.label_m.setStyleSheet("background-color: rgb(213, 126, 0);")
        
        self.label_aval = QtWidgets.QLabel(self.centralwidget)
        self.label_aval.setGeometry(QtCore.QRect(270, 100, 90, 30))
        self.label_aval.setObjectName("label")
        self.label_aval.setWordWrap(True)
        self.label_aval.setStyleSheet("background-color: rgb(213, 126, 0);")
        
        self.label_u = QtWidgets.QLabel(self.centralwidget)
        self.label_u.setGeometry(QtCore.QRect(270, 135, 90, 30))
        self.label_u.setObjectName("label")
        self.label_u.setWordWrap(True)
        self.label_u.setStyleSheet("background-color: rgb(213, 126, 0);")
        
        self.lineEdit_dir = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_dir.setGeometry(QtCore.QRect(105, 65, 160, 30))
        self.lineEdit_dir.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.lineEdit_dir.setObjectName("lineEdit_dir")
        self.lineEdit_dir.setPlaceholderText("up, down, none")
        #self.lineEdit_col = QtWidgets.QLineEdit(self.centralwidget)
        #self.lineEdit_col.setGeometry(QtCore.QRect(105, 100, 160, 30))
        #self.lineEdit_col.setStyleSheet("background-color: rgb(255, 170, 127);")
        #self.lineEdit_col.setObjectName("lineEdit_col")
        #self.lineEdit_dir.setPlaceholderText("up, down, none")
        self.lineEdit_fext = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_fext.setGeometry(QtCore.QRect(105, 100, 160, 30))
        self.lineEdit_fext.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.lineEdit_fext.setObjectName("lineEdit_fext")
        self.lineEdit_fext.setPlaceholderText("newtons")
        self.lineEdit_fn = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_fn.setGeometry(QtCore.QRect(105, 135, 160, 30))
        self.lineEdit_fn.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.lineEdit_fn.setObjectName("lineEdit_fn")
        self.lineEdit_fn.setPlaceholderText("newtons")
        self.lineEdit_fg = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_fg.setGeometry(QtCore.QRect(105, 170, 160, 30))
        self.lineEdit_fg.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.lineEdit_fg.setObjectName("lineEdit_fg")
        self.lineEdit_fg.setPlaceholderText("newtons")
        self.lineEdit_theta = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_theta.setGeometry(QtCore.QRect(105, 205, 160, 30))
        self.lineEdit_theta.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.lineEdit_theta.setObjectName("lineEdit_theta")
        self.lineEdit_theta.setPlaceholderText("degrees")
        self.lineEdit_m = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_m.setGeometry(QtCore.QRect(365, 65, 160, 30))
        self.lineEdit_m.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.lineEdit_m.setObjectName("lineEdit_m")
        self.lineEdit_m.setPlaceholderText("kilograms")
        self.lineEdit_u = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_u.setGeometry(QtCore.QRect(365, 135, 160, 30))
        self.lineEdit_u.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.lineEdit_u.setObjectName("lineEdit_u")
        self.lineEdit_u.setPlaceholderText("m,F,Fg,theta,N")
        self.lineEdit_aval = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_aval.setGeometry(QtCore.QRect(365, 100, 160, 30))
        self.lineEdit_aval.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.lineEdit_aval.setObjectName("lineEdit_aval")
        self.lineEdit_aval.setPlaceholderText("meters/second^2")
        
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Solve Inclined Forces"))
        
        self.calc_button.setStatusTip(_translate("MainWindow", "Calculate"))
        self.calc_button.setText(_translate("MainWindow", "Calculate"))
        self.calc_button.setShortcut(_translate("MainWindow", "="))
        
        self.label_inform.setText(_translate("MainWindow", "Inclined Force problems take the principles of basic force problems and apply them to a 2D plane, in which x and y components,"
        " can be resolved to find the total components of net force and acceleration."))
        self.label_dir.setText(_translate("MainWindow", "Direction of A"))
        #self.label_col.setText(_translate("MainWindow", "Collision Type"))
        self.label_fext.setText(_translate("MainWindow", "External Force"))
        self.label_fn.setText(_translate("MainWindow", "Force(Normal)"))
        self.label_fg.setText(_translate("MainWindow", "Force(Gravity)"))
        self.label_theta.setText(_translate("MainWindow", "theta"))
        self.label_m.setText(_translate("MainWindow", "Mass"))
        self.label_aval.setText(_translate("MainWindow", "Acceleration"))
        self.label_u.setText(_translate("MainWindow", "Unknown"))
        self.label_answer.setText(_translate("MainWindow", "Answer"))
        
    def calculate(self):
        print("Hello World")
        
        def number(s):
            try:
                float(s)
                return True
            except ValueError:
                return False
        hmmm = ['up', 'down', '0', 'none', 'None']
        geez = "You don't quite have the facilites for that mate"
        cat = True
        let = ["m,F,Fg,theta,N"]
        while cat:
            accelerating = self.lineEdit_dir.text()
            if accelerating in hmmm:
                break
            else:
                accelerating = self.lineEdit_col.text()
                break
        if (accelerating == '0' or accelerating == 'none'):
            F = self.lineEdit_fext.text()
            if number(F):
                F = float(F)    
            N = self.lineEdit_fn.text()
            if number(N):
                N = float(N)
            Fg = self.lineEdit_fg.text()
            if number(Fg):
                Fg = float(Fg)
            theta = self.lineEdit_theta.text()
            if number(theta):
                theta = float(theta)
            m = self.lineEdit_m.text()
            if number(m):
                m = float(m)
            unknown = self.lineEdit_u.text()
            wow = True
            while wow:
                if unknown == 'F':
                    if (type(m) == float and type(theta) == float): 
                        F = m * 9.8 * math.sin(theta)
                        self.label_answer.setText("Answer:" + str(F))
                        wow = False
                    elif (type(N) == float and type(theta) == float):
                        F = N * math.tan(theta)
                        self.label_answer.setText("Answer:" + str(F))
                        wow = False
                    else:
                        self.label_answer.setText("Answer:" + geez)
                        wow = False
                if unknown == 'N':
                    if (type(m) == float and type(theta) == float): 
                        N = m * 9.8 * math.cos(theta)
                        self.label_answer.setText("Answer:" + str(N))
                        wow = False
                    elif (type(F) == float and type(theta) == float):
                        N = F * math.cos(theta)/math.sin(theta)
                        self.label_answer.setText("Answer:" + str(N))
                        wow = False
                    else:
                        self.label_answer.setText("Answer:" + geez)
                        wow = False
                if unknown == 'Fg':
                    if (type(m) == float): 
                        Fg = m * 9.8
                        self.label_answer.setText("Answer:" + str(Fg))
                        wow = False
                    elif (type(F) == float and type(theta) == float):
                        Fg = F/math.sin(theta)
                        self.label_answer.setText("Answer:" + str(Fg))
                        wow = False
                    elif (type(N) == float and type(theta) == float):
                        Fg= N/math.cos(theta)
                        self.label_answer.setText("Answer:" + str(Fg))
                        wow = False
                    else:
                        self.label_answer.setText("Answer:" + geez)
                        wow = False
                if unknown == 'theta':
                    if (type(N) == float and type(m)): 
                        theta = np.arccos(N/(m * 9.8)) 
                        self.label_answer.setText("Answer:" + str(theta))
                        wow = False
                    elif (type(F) == float and type(N) == float):
                        theta = np.arctan(F/N)
                        self.label_answer.setText("Answer:" + str(theta))
                        wow = False
                    elif (type(F) == float and type(m) == float):
                        theta = np.arcsin(F/m*9.8)
                        self.label_answer.setText("Answer:" + str(theta))
                        wow = False
                    else:
                        self.label_answer.setText("Answer:" + geez)
                        wow = False
                if unknown == 'm':
                    if (type(N) == float and type(theta) == float): 
                        m = N/(9.8 * math.cos(theta))
                        self.label_answer.setText("Answer:" + str(m))
                        wow = False
                    elif (type(F) == float and type(theta) == float):
                        m = F/(9.8 * math.sin(theta))
                        self.label_answer.setText("Answer:" + str(m))
                        wow = False
                    else:
                        self.label_answer.setText("Answer:" + geez)
                        wow = False
        
        if accelerating == 'up':
            F = self.lineEdit_fext.text()
            if number(F):
                F = float(F)    
            N = self.lineEdit_fn.text()
            if number(N):
                N = float(N)
            Fg = self.lineEdit_fg.text()
            if number(Fg):
                Fg = float(Fg)
            theta = self.lineEdit_theta.text()
            if number(theta):
                theta = float(theta)
            m = self.lineEdit_m.text()
            if number(m):
                m = float(m)
            a = self.lineEdit_aval.text()
            if number(a):
                a = float(a)
            unknown = self.lineEdit_u.text()
            wow = True
            while wow:
                if unknown == 'F':
                    if (type(m) == float and type(theta) == float and type(a) == float): 
                        F = m*a - m * 9.8 * math.sin(theta)
                        self.label_answer.setText("Answer:" + str(F))
                        wow = False
                    elif (type(N) == float and type(theta) == float and type(a) == float and type(N) == float):
                        F = N * math.tan(theta) - m*a
                        self.label_answer.setText("Answer:" + str(F))
                        wow = False
                    else:
                        self.label_answer.setText("Answer:" + geez)
                        wow = False
                if unknown == 'N':
                    if (type(m) == float and type(theta) == float): 
                        N = m * 9.8 * math.cos(theta)
                        self.label_answer.setText("Answer:" + str(N))
                        wow = False
                    elif (type(F) == float and type(theta) == float and type(a) == float and type(m) == float):
                        N = ((F + m*a)/math.sin(theta)) * math.cos(theta)
                        self.label_answer.setText("Answer:" + str(N))
                        wow = False
                    else:
                        self.label_answer.setText("Answer:" + geez)
                        wow = False
                if unknown == 'Fg':
                    if (type(m) == float and type(F) == float and type(theta) == float and type(a) == float):
                        Fg = (F + m*a)/math.sin(theta)
                        self.label_answer.setText("Answer:" + str(Fg))
                        wow = False
                    elif (type(N) == float and type(theta) == float):
                        Fg = N/math.cos(theta)
                        self.label_answer.setText("Answer:" + str(Fg))
                        wow = False
                    else:
                        self.label_answer.setText("Answer:" + geez)
                        wow = False
                if unknown == 'theta':
                    if (type(N) == float and type(m)): 
                        theta = np.arccos(N/(m * 9.8)) 
                        self.label_answer.setText("Answer:" + str(theta))
                        wow = False
                    elif (type(F) == float and type(N) == float and type(m) == float and type(a) == float):
                        theta = np.arctan((m*a+F)/N)
                        self.label_answer.setText("Answer:" + str(theta))
                        wow = False
                    else:
                        self.label_answer.setText("Answer:" + geez)
                        wow = False
                if unknown == 'm':
                    if (type(N) == float and type(theta) == float): 
                        m = N/(9.8 * math.cos(theta))
                        self.label_answer.setText("Answer:" + str(m))
                        wow = False
                    elif (type(F) == float and type(theta) == float):
                        m = F/(9.8*math.sin(theta) - a)
                        self.label_answer.setText("Answer:" + str(m))
                        wow = False
                    else:
                        self.label_answer.setText("Answer:" + geez)
                        wow = False
        if accelerating == 'down':
            F = self.lineEdit_fext.text()
            if number(F):
                F = float(F)    
            N = self.lineEdit_fn.text()
            if number(N):
                N = float(N)
            Fg = self.lineEdit_fg.text()
            if number(Fg):
                Fg = float(Fg)
            theta = self.lineEdit_theta.text()
            if number(theta):
                theta = float(theta)
            m = self.lineEdit_m.text()
            if number(m):
                m = float(m)
            a = self.lineEdit_aval.text()
            if number(a):
                a = float(a)
            unknown = self.lineEdit_u.text()
            wow = True
            while wow:
                if unknown == 'F':
                    if (type(m) == float and type(theta) == float and type(a) == float): 
                        F = m*a + m * 9.8 * math.sin(theta)
                        self.label_answer.setText("Answer:" + str(F))
                        wow = False
                    elif (type(N) == float and type(theta) == float and type(a) == float and type(N) == float):
                        F = N * math.tan(theta) + m*a
                        self.label_answer.setText("Answer:" + str(F))
                        wow = False
                    else:
                        self.label_answer.setText("Answer:" + geez)
                        wow = False
                if unknown == 'N':
                    if (type(m) == float and type(theta) == float): 
                        N = m * 9.8 * math.cos(theta)
                        self.label_answer.setText("Answer:" + str(N))
                        wow = False
                    elif (type(F) == float and type(theta) == float and type(a) == float and type(m) == float):
                        N = ((F - m*a)/math.sin(theta)) * math.cos(theta)
                        self.label_answer.setText("Answer:" + str(N))
                        wow = False
                    else:
                        self.label_answer.setText("Answer:" + geez)
                        wow = False
                if unknown == 'Fg':
                    if (type(m) == float and type(F) == float and type(theta) == float and type(a) == float):
                        Fg = (F - m*a)/math.sin(theta)
                        self.label_answer.setText("Answer:" + str(Fg))
                        wow = False
                    elif (type(N) == float and type(theta) == float):
                        Fg = N/math.cos(theta)
                        self.label_answer.setText("Answer:" + str(Fg))
                        wow = False
                    else:
                        self.label_answer.setText("Answer:" + geez)
                        wow = False
                if unknown == 'theta':
                    if (type(N) == float and type(m)): 
                        theta = np.arccos(N/(m * 9.8)) 
                        self.label_answer.setText("Answer:" + str(theta))
                        wow = False
                    elif (type(F) == float and type(N) == float and type(m) == float and type(a) == float):
                        theta = np.arctan((m*a-F)/N)
                        self.label_answer.setText("Answer:" + str(theta))
                        wow = False
                    else:
                        self.label_answer.setText("Answer:" + geez)
                        wow = False
                if unknown == 'm':
                    if (type(N) == float and type(theta) == float): 
                        m = N/(9.8 * math.cos(theta))
                        self.label_answer.setText("Answer:" + str(m))
                        wow = False
                    elif (type(F) == float and type(theta) == float):
                        m = F/(9.8*math.sin(theta)+ a)
                        self.label_answer.setText("Answer:" + str(m))
                        wow = False
                    else:
                        self.label_answer.setText("Answer:" + geez)
                        wow = False

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow4()
    ui.setup(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
