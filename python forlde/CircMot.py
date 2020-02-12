# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 's2.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import math
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow6(object):
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
        
        self.label_acp = QtWidgets.QLabel(self.centralwidget)
        self.label_acp.setGeometry(QtCore.QRect(10, 135, 90, 30))
        self.label_acp.setObjectName("label")
        self.label_acp.setWordWrap(True)
        self.label_acp.setStyleSheet("background-color: rgb(213, 126, 0);")
        
        self.label_v = QtWidgets.QLabel(self.centralwidget)
        self.label_v.setGeometry(QtCore.QRect(10, 170, 90, 30))
        self.label_v.setObjectName("label")
        self.label_v.setWordWrap(True)
        self.label_v.setStyleSheet("background-color: rgb(213, 126, 0);")
        
        self.label_r = QtWidgets.QLabel(self.centralwidget)
        self.label_r.setGeometry(QtCore.QRect(10, 205, 90, 30))
        self.label_r.setObjectName("label")
        self.label_r.setWordWrap(True)
        self.label_r.setStyleSheet("background-color: rgb(213, 126, 0);")
        
        self.label_u = QtWidgets.QLabel(self.centralwidget)
        self.label_u.setGeometry(QtCore.QRect(10, 240, 90, 30))
        self.label_u.setObjectName("label")
        self.label_u.setWordWrap(True)
        self.label_u.setStyleSheet("background-color: rgb(213, 126, 0);")
        
        self.label_answer = QtWidgets.QLabel(self.centralwidget)
        self.label_answer.setGeometry(QtCore.QRect(330, 147, 150, 50))
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
        self.lineEdit_v = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_v.setGeometry(QtCore.QRect(105, 170, 160, 30))
        self.lineEdit_v.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.lineEdit_v.setObjectName("lineEdit_v")
        self.lineEdit_v.setPlaceholderText("meters/second")
        self.lineEdit_r = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_r.setGeometry(QtCore.QRect(105, 205, 160, 30))
        self.lineEdit_r.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.lineEdit_r.setObjectName("lineEdit_r")
        self.lineEdit_r.setPlaceholderText("meters")
        self.lineEdit_u = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_u.setGeometry(QtCore.QRect(105, 240, 160, 30))
        self.lineEdit_u.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.lineEdit_u.setObjectName("lineEdit_u")
        self.lineEdit_u.setPlaceholderText("V, Fc, m, r,ac")
        
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Solve Circular Motion"))
        
        self.calc_button.setStatusTip(_translate("MainWindow", "Calculate"))
        self.calc_button.setText(_translate("MainWindow", "Calculate"))
        self.calc_button.setShortcut(_translate("MainWindow", "="))
        
        self.label_inform.setText(_translate("MainWindow", "Circular Motion problems involve the movement of an object around a fixed point in which its acceleration always faces inwards, causing its velocity to stay constant."
        " Due to this quirk, force calculations differ from standard 1D and 2D problems, leading to an alterate definition of acceleration, involving velocity and radius."))
        self.label_f.setText(_translate("MainWindow", "Force(Circular)"))
        self.label_m.setText(_translate("MainWindow", "Mass"))
        self.label_acp.setText(_translate("MainWindow", "Acceleration"))
        self.label_v.setText(_translate("MainWindow", "Velocity"))
        self.label_r.setText(_translate("MainWindow", "Radius"))
        self.label_u.setText(_translate("MainWindow", "Unknown"))
        self.label_answer.setText(_translate("MainWindow", "Answer"))
        
    def calculate(self):
        name = float(self.lineEditf.text())
        person = float(self.lineEdit_m.text())
        print("Hello")
        print(name+person)
        
        def number(s):
            try:
                float(s)
                return True
            except ValueError:
                return False
        V = self.lineEdit_v.text()
        if number(V):
            V = float(V)    
        Fc = self.lineEditf.text()
        if number(Fc):
            Fc = float(Fc)
        m = self.lineEdit_m.text()
        if number(m):
            m = float(m)
        r = self.lineEdit_r.text()
        if number(r):
            r = float(r)
        ac = self.lineEdit_a.text()
        if number(ac):
            ac = float(ac)
        bruh = ['V', 'Fc', 'm', 'r','ac']
        unknown = self.lineEdit_u.text()
        wow = True
        geez = "You don't quite have the facilites for that mate"
        while wow:
            if unknown not in bruh:
                self.label_answer.setText("Answer:" + geez)
                wow = False
            if unknown == 'V':
                if (type(Fc) == float and type(r) == float and type(m) == float): 
                    V = math.sqrt(Fc*r/m)
                    self.label_answer.setText("Answer:" + str(V))
                    wow = False
                else:
                    self.label_answer.setText("Answer:" + geez)
            if unknown == 'm':
                if (type(Fc) == float and type(r) == float and type(V) == float): 
                    m = Fc*r/(V**2)
                    self.label_answer.setText("Answer:" + str(m))
                    wow = False
                elif (type(ac) == float and type(Fc) == float): 
                    m = Fc/ac
                    self.label_answer.setText("Answer:" + str(m))
                    wow = False
                else:
                    self.label_answer.setText("Answer:" + geez)
            if unknown == 'Fc':
                if (type(m) == float and type(r) == float and type(V) == float): 
                    Fc = V**2 * m/r
                    self.label_answer.setText("Answer:" + str(Fc))
                    wow = False
                elif (type(ac) == float and type(m) == float): 
                    Fc = m * ac
                    self.label_answer.setText("Answer:" + str(Fc))
                    wow = False
                else:
                    self.label_answer.setText("Answer:" + geez)
            if unknown == 'r':
                if (type(Fc) == float and type(V) == float and type(m) == float): 
                    r = (m * V**2)/Fc
                    self.label_answer.setText("Answer:" + str(r))
                    wow = False
                else:
                    self.label_answer.setText("Answer:" + geez)
            if unknown == 'ac':
                if (type(r) == float and type(V) == float): 
                    ac = (V**2)/r
                    self.label_answer.setText("Answer:" + str(ac))
                    wow = False
                elif (type(Fc) == float and type(m) == float): 
                    ac = (V**2)/r
                    self.label_answer.setText("Answer:" + str(ac))
                    wow = False
                else:
                    self.label_answer.setText("Answer:" + geez)
            


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow6()
    ui.setup(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
