# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 's2.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import math
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow3(object):
    def setup(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 400)
        MainWindow.setStyleSheet("background-color: rgb(52, 96, 148);")

        

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        
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
        
        self.label_f = QtWidgets.QLabel(self.centralwidget)
        self.label_f.setGeometry(QtCore.QRect(10, 65, 90, 30))
        self.label_f.setObjectName("label")
        self.label_f.setWordWrap(True)
        self.label_f.setStyleSheet("background-color: rgb(213, 126, 0);")
        
        self.label_m = QtWidgets.QLabel(self.centralwidget)
        self.label_m.setGeometry(QtCore.QRect(10, 100, 90, 30))
        self.label_m.setObjectName("label")
        self.label_m.setWordWrap(True)
        self.label_m.setStyleSheet("background-color: rgb(213, 126, 0);")
        
        self.label_a = QtWidgets.QLabel(self.centralwidget)
        self.label_a.setGeometry(QtCore.QRect(10, 135, 90, 30))
        self.label_a.setObjectName("label")
        self.label_a.setWordWrap(True)
        self.label_a.setStyleSheet("background-color: rgb(213, 126, 0);")
        
        self.label_fg = QtWidgets.QLabel(self.centralwidget)
        self.label_fg.setGeometry(QtCore.QRect(10, 170, 90, 30))
        self.label_fg.setObjectName("label")
        self.label_fg.setWordWrap(True)
        self.label_fg.setStyleSheet("background-color: rgb(213, 126, 0);")
        
        self.label_n = QtWidgets.QLabel(self.centralwidget)
        self.label_n.setGeometry(QtCore.QRect(10, 205, 90, 30))
        self.label_n.setObjectName("label")
        self.label_n.setWordWrap(True)
        self.label_n.setStyleSheet("background-color: rgb(213, 126, 0);")
        
        self.label_u = QtWidgets.QLabel(self.centralwidget)
        self.label_u.setGeometry(QtCore.QRect(10, 240, 90, 30))
        self.label_u.setObjectName("label")
        self.label_u.setWordWrap(True)
        self.label_u.setStyleSheet("background-color: rgb(213, 126, 0);")
        
        self.label_answer = QtWidgets.QLabel(self.centralwidget)
        self.label_answer.setGeometry(QtCore.QRect(270, 65, 320, 100))
        self.label_answer.setObjectName("label")
        self.label_answer.setWordWrap(True)
        self.label_answer.setStyleSheet("background-color: rgb(213, 126, 0);")
        
        self.lineEditf = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditf.setGeometry(QtCore.QRect(105, 65, 160, 30))
        self.lineEditf.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.lineEditf.setObjectName("lineEditf")
        self.lineEditf.setPlaceholderText("newtons")
        self.lineEdit_m = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_m.setGeometry(QtCore.QRect(105, 100, 160, 30))
        self.lineEdit_m.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.lineEdit_m.setObjectName("lineEdit_m")
        self.lineEdit_m.setPlaceholderText("kilograms")
        self.lineEdit_a = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_a.setGeometry(QtCore.QRect(105, 135, 160, 30))
        self.lineEdit_a.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.lineEdit_a.setObjectName("lineEdit_a")
        self.lineEdit_a.setPlaceholderText("meters/second^2")
        self.lineEdit_fg = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_fg.setGeometry(QtCore.QRect(105, 170, 160, 30))
        self.lineEdit_fg.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.lineEdit_fg.setObjectName("lineEdit_fg")
        self.lineEdit_fg.setPlaceholderText("newtons")
        self.lineEdit_n = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_n.setGeometry(QtCore.QRect(105, 205, 160, 30))
        self.lineEdit_n.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.lineEdit_n.setObjectName("lineEdit_n")
        self.lineEdit_n.setPlaceholderText("newtons")
        self.lineEdit_u = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_u.setGeometry(QtCore.QRect(105, 240, 160, 30))
        self.lineEdit_u.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.lineEdit_u.setObjectName("lineEdit_u")
        self.lineEdit_u.setPlaceholderText("F, m, a, Fg, N")
        
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Solve Basic Forces"))
        
        self.calc_button.setStatusTip(_translate("MainWindow", "Calculate"))
        self.calc_button.setText(_translate("MainWindow", "Calculate"))
        self.calc_button.setShortcut(_translate("MainWindow", "="))
        
        self.label_inform.setText(_translate("MainWindow", "Basic Force problems involve a 1D plane in which an object is acted on by standard forces. External force providing acceleration,"
        " given the mass is provided, Normal Force, and Gravitational Force form the basis for more complex force problems"))
        self.label_f.setText(_translate("MainWindow", "Force"))
        self.label_m.setText(_translate("MainWindow", "Mass"))
        self.label_a.setText(_translate("MainWindow", "Acceleration"))
        self.label_fg.setText(_translate("MainWindow", "Force(Gravity)"))
        self.label_n.setText(_translate("MainWindow", "Force(Normal)"))
        self.label_u.setText(_translate("MainWindow", "Unknown"))
        self.label_answer.setText(_translate("MainWindow", "Answer"))

        
    def calculate(self):
        print("Hello")

        def number(s):
            try:
                float(s)
                return True
            except ValueError:
                return False
        bruh = ['F', 'm', 'a', 'Fg', 'N']
        F = self.lineEditf.text()
        if number(F):
            F = float(F) 
        m = self.lineEdit_m.text()
        if number(m):
            m = float(m) 
        a = self.lineEdit_a.text()
        if number(a):
            a = float(a) 
        Fg = self.lineEdit_fg.text()
        if number(Fg):
            Fg = float(Fg)
        N = self.lineEdit_n.text()
        if number(N):
            N = float(N) 
        unknown = self.lineEdit_u.text()
        wow = True
        geez = "You don't quite have the facilites for that mate"
        while wow:
            if unknown not in bruh:
                print("We don't have the facilities for that mate")
                self.label_answer.setText("Answer" + geez)
                wow = False
            if unknown == 'F':
                if (type(m) == float and type(a) == float):
                    F = m*a
                    self.label_answer.setText("Answer" + str(F))
                    wow = False
                elif (type(N) == float and type(a) == float):
                    F = (N*a)/9.8
                    self.label_answer.setText("Answer" + str(F))
                    wow = False
                else:
                    print("You don't quite have the facilites for that mate")
                    self.label_answer.setText("Answer" + geez)
                    wow = False
            if unknown == 'm':
                if (type(N) == float):
                    m = N/9.8
                    self.label_answer.setText("Answer" + str(m))
                    wow = False
                elif (type(F) == float and type(a) == float):
                    m = F/a
                    self.label_answer.setText("Answer" + str(m))
                    wow = False
                else:
                    print("You don't quite have the facilites for that mate")
                    self.label_answer.setText("Answer" + geez)
                    wow = False
            if unknown == 'a':
                if (type(m) == float and type(F) == float):
                    a = F/m
                    self.label_answer.setText("Answer" + str(a))
                    wow = False
                elif (type(N) == float and type(a) == float):
                    a = (F*9.8)/N
                    self.label_answer.setText("Answer" + str(a))
                    wow = False
                else:
                    print("You don't quite have the facilites for that mate")
                    self.label_answer.setText("Answer" + geez)
                    wow = False
            if unknown == 'Fg':
                if (type(m) == float and type(a) == float):
                    Fg = m*9.81
                    self.label_answer.setText("Answer" + str(Fg))
                    wow = False
                elif (type(N) == float):
                    Fg = -1*N
                    self.label_answer.setText("Answer" + str(Fg))
                    wow = False
                else:
                    print("You don't quite have the facilites for that mate")
                    self.label_answer.setText("Answer" + geez)
                    wow = False
            if unknown == 'N':
                if (type(m) == float):
                    N = m*9.81
                    self.label_answer.setText("Answer" + str(N))
                    wow = False
                elif (type(F) == float, type(a) == float):
                    N = F*9.8/a
                    self.label_answer.setText("Answer" + str(N))
                    wow = False
                else:
                    print("You don't quite have the facilites for that mate")
                    self.label_answer.setText("Answer" + geez)
                    wow = False

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow3()
    ui.setup(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
