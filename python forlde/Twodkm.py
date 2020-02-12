# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 's2.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import math
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow2(object):
    def setup(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 400)
        MainWindow.setStyleSheet("background-color: rgb(52, 96, 148);")


        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.calc_button = QtWidgets.QPushButton(self.centralwidget)
        self.calc_button.setGeometry(QtCore.QRect(365, 280, 160, 50))
        self.calc_button.setObjectName("solveButton1dk")
        self.calc_button.setStyleSheet("background-color: rgb(213, 126, 0);")
        self.calc_button.clicked.connect(self.calculate)
        
        self.label_inform = QtWidgets.QLabel(self.centralwidget)
        self.label_inform.setGeometry(QtCore.QRect(10, 10, 580, 50))
        self.label_inform.setObjectName("label")
        self.label_inform.setWordWrap(True)
        self.label_inform.setStyleSheet("background-color: rgb(213, 126, 0);")
        
        self.label_answer = QtWidgets.QLabel(self.centralwidget)
        self.label_answer.setGeometry(QtCore.QRect(10, 240, 160, 50))
        self.label_answer.setObjectName("label")
        self.label_answer.setWordWrap(True)
        self.label_answer.setStyleSheet("background-color: rgb(213, 126, 0);")
        
        self.label_vf = QtWidgets.QLabel(self.centralwidget)
        self.label_vf.setGeometry(QtCore.QRect(10, 65, 90, 30))
        self.label_vf.setObjectName("label")
        self.label_vf.setWordWrap(True)
        self.label_vf.setStyleSheet("background-color: rgb(213, 126, 0);")
        
        self.label_vi = QtWidgets.QLabel(self.centralwidget)
        self.label_vi.setGeometry(QtCore.QRect(10, 100, 90, 30))
        self.label_vi.setObjectName("label")
        self.label_vi.setWordWrap(True)
        self.label_vi.setStyleSheet("background-color: rgb(213, 126, 0);")
        
        self.label_alpha = QtWidgets.QLabel(self.centralwidget)
        self.label_alpha.setGeometry(QtCore.QRect(10, 135, 90, 30))
        self.label_alpha.setObjectName("label")
        self.label_alpha.setWordWrap(True)
        self.label_alpha.setStyleSheet("background-color: rgb(213, 126, 0);")
        
        self.label_theta = QtWidgets.QLabel(self.centralwidget)
        self.label_theta.setGeometry(QtCore.QRect(10, 170, 90, 30))
        self.label_theta.setObjectName("label")
        self.label_theta.setWordWrap(True)
        self.label_theta.setStyleSheet("background-color: rgb(213, 126, 0);")
        
        self.label_dx = QtWidgets.QLabel(self.centralwidget)
        self.label_dx.setGeometry(QtCore.QRect(270, 65, 90, 30))
        self.label_dx.setObjectName("label")
        self.label_dx.setWordWrap(True)
        self.label_dx.setStyleSheet("background-color: rgb(213, 126, 0);")
        
        self.label_ay = QtWidgets.QLabel(self.centralwidget)
        self.label_ay.setGeometry(QtCore.QRect(270, 100, 90, 30))
        self.label_ay.setObjectName("label")
        self.label_ay.setWordWrap(True)
        self.label_ay.setStyleSheet("background-color: rgb(213, 126, 0);")
        
        self.label_dy = QtWidgets.QLabel(self.centralwidget)
        self.label_dy.setGeometry(QtCore.QRect(270, 135, 90, 30))
        self.label_dy.setObjectName("label")
        self.label_dy.setWordWrap(True)
        self.label_dy.setStyleSheet("background-color: rgb(213, 126, 0);")
        
        self.label_t = QtWidgets.QLabel(self.centralwidget)
        self.label_t.setGeometry(QtCore.QRect(10, 205, 90, 30))
        self.label_t.setObjectName("label")
        self.label_t.setWordWrap(True)
        self.label_t.setStyleSheet("background-color: rgb(213, 126, 0);")
        
        self.label_u = QtWidgets.QLabel(self.centralwidget)
        self.label_u.setGeometry(QtCore.QRect(270, 170, 90, 30))
        self.label_u.setObjectName("label")
        self.label_u.setWordWrap(True)
        self.label_u.setStyleSheet("background-color: rgb(213, 126, 0);")
        #Creating LineEdits for the Gui
        
        self.lineEdit_vf = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_vf.setGeometry(QtCore.QRect(105, 65, 160, 30))
        self.lineEdit_vf.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.lineEdit_vf.setObjectName("lineEdit_vf")
        self.lineEdit_vf.setPlaceholderText("meters/second")
        self.lineEdit_vi = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_vi.setGeometry(QtCore.QRect(105, 100, 160, 30))
        self.lineEdit_vi.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.lineEdit_vi.setObjectName("lineEdit_vi")
        self.lineEdit_vi.setPlaceholderText("meters/second")
        self.lineEdit_alpha = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_alpha.setGeometry(QtCore.QRect(105, 135, 160, 30))
        self.lineEdit_alpha.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.lineEdit_alpha.setObjectName("lineEdit_alpha")
        self.lineEdit_alpha.setPlaceholderText("degrees")
        self.lineEdit_theta = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_theta.setGeometry(QtCore.QRect(105, 170, 160, 30))
        self.lineEdit_theta.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.lineEdit_theta.setObjectName("lineEdit_theta")
        self.lineEdit_theta.setPlaceholderText("degrees")
        self.lineEdit_dx = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_dx.setGeometry(QtCore.QRect(365, 65, 160, 30))
        self.lineEdit_dx.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.lineEdit_dx.setObjectName("lineEdit_dx")
        self.lineEdit_dx.setPlaceholderText("meters")
        self.lineEdit_ay = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_ay.setGeometry(QtCore.QRect(365, 100, 160, 30))
        self.lineEdit_ay.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.lineEdit_ay.setObjectName("lineEdit_ay")
        self.lineEdit_ay.setPlaceholderText("meters/second^2")
        self.lineEdit_dy = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_dy.setGeometry(QtCore.QRect(365, 135, 160, 30))
        self.lineEdit_dy.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.lineEdit_dy.setObjectName("lineEdit_dy")
        self.lineEdit_dy.setPlaceholderText("meters")
        self.lineEdit_u = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_u.setGeometry(QtCore.QRect(365, 170, 160, 30))
        self.lineEdit_u.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.lineEdit_u.setObjectName("lineEdit_u")
        self.lineEdit_u.setPlaceholderText("dx, Vf, t, dy")
        self.lineEditt = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditt.setGeometry(QtCore.QRect(105, 205, 160, 30))
        self.lineEditt.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.lineEditt.setObjectName("lineEditt")
        self.lineEditt.setPlaceholderText("seconds")
                
        
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Solve 2D Kinematics"))
        
        self.calc_button.setStatusTip(_translate("MainWindow", "1D Kinematics"))
        self.calc_button.setText(_translate("MainWindow", "One Dimensional\n"
"Kinematics"))
        self.calc_button.setShortcut(_translate("MainWindow", "1"))
        
        self.label_inform.setText(_translate("MainWindow", "In order to solve a 2D Kinematics problem, many different combinations of variables can be utilized to generate a specific value,"
        " therefore for the sake of simplicity, this program assumes horizontal acceleration is at zero at all times. It is also assumed that acceleration is constant."))
        self.label_vf.setText(_translate("MainWindow", "Final Velocity"))
        self.label_vi.setText(_translate("MainWindow", "Initial Velocity"))
        self.label_alpha.setText(_translate("MainWindow", "alpha"))
        self.label_theta.setText(_translate("MainWindow", "theta"))
        self.label_t.setText(_translate("MainWindow", "Time"))
        self.label_dx.setText(_translate("MainWindow", "Delta X"))
        self.label_ay.setText(_translate("MainWindow", "Acceleration (Y)"))
        self.label_dy.setText(_translate("MainWindow", "Delta Y"))
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
        t = self.lineEditt.text()
        if number(t):
            t = float(t)    
        theta = self.lineEdit_theta.text()
        if number(theta):
            theta = float(theta)
        alpha = self.lineEdit_alpha.text()
        if number(alpha):
            alpha = float(alpha)
        Vi = self.lineEdit_vi.text()
        if number(Vi):
            Vi = float(Vi)
        Vf = self.lineEdit_vi.text()
        if number(Vf):
            Vf = float(Vf)
        dx = self.lineEdit_dx.text()
        if number(dx):
            dx = float(dx)
        ay = self.lineEdit_ay.text()
        if number(ay):
            ay = float(ay)
        dy = self.lineEdit_dy.text()
        if number(dy):
            dy = float(dy)
        unknown = self.lineEdit_u.text()
        yo = ['dx', 'Vf', 't', 'dy']
        geez = "You don't quite have the facilites for that mate"
        wow = True
        while wow:
            if unknown not in yo:
                self.label_answer.setText("Answer" + geez)
                wow = False
            if unknown == 't':
                if (type(Vi) == float and type(theta) == float and type(dx) == float):
                    t = dx/(Vi * math.cos(theta))
                    self.label_answer.setText("Answer" + str(t))
                    wow = False
                elif (type(Vi) == float and type(dy) == float and type(theta) == float and type(ay) == float):
                    t1 = (-1*Vi + math.sqrt((Vi*math.sin(theta))**2 - 4*(ay/2)*(-dy)))/ay
                    t2 = (-1*Vi - math.sqrt((Vi*math.sin(theta))**2 - 4*(ay/2)*(-dy)))/ay
                    if (t1 > 0 and t2 < 0):
                        t = t1
                    elif (t1 < 0 and t2 > 0):
                        t = t2
                    elif t1 == t2:
                        t = t1
                    self.label_answer.setText("Answer" + str(t))
                    wow = False
                else:
                    self.label_answer.setText("Answer" + geez)
                    wow = False
            if unknown == 'dy':
                if (type(Vi) == float and type(theta) and type(t) == float and type(ay)): 
                    dy = Vi * math.sin(theta) * t + (ay * t**2)/2
                    self.label_answer.setText("Answer" + str(dy))
                    wow = False
                else:
                    self.label_answer.setText("Answer" + geez)
                    wow = False
            if unknown == 'dx':
                if (type(Vi) == float and type(t) and type(theta) == float): 
                    dx = t * Vi * math.cos(theta)
                    self.label_answer.setText("Answer" + str(dx))
                    wow = False
                else:
                    self.label_answer.setText("Answer" + geez)
                    wow = False
            if unknown == 'Vf':
                if (type(Vi) == float and type(theta)== float and type(alpha) == float): 
                    Vf = Vi * math.cos(theta) * math.cos(alpha)
                    self.label_answer.setText("Answer" + str(Vf))
                    wow = False
                else:
                    self.label_answer.setText("Answer" + geez)
                    wow = False
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow2()
    ui.setup(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
