# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 's2.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import math
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow5(object):
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
        self.label_answer.setGeometry(QtCore.QRect(350, 187, 80, 50))
        self.label_answer.setObjectName("label")
        self.label_answer.setWordWrap(True)
        self.label_answer.setStyleSheet("background-color: rgb(213, 126, 0);")
        
        self.label_answer2 = QtWidgets.QLabel(self.centralwidget)
        self.label_answer2.setGeometry(QtCore.QRect(350, 237, 80, 50))
        self.label_answer2.setObjectName("label")
        self.label_answer2.setWordWrap(True)
        self.label_answer2.setStyleSheet("background-color: rgb(213, 126, 0);")
        
        self.label_m1 = QtWidgets.QLabel(self.centralwidget)
        self.label_m1.setGeometry(QtCore.QRect(10, 65, 80, 30))
        self.label_m1.setObjectName("label")
        self.label_m1.setWordWrap(True)
        self.label_m1.setStyleSheet("background-color: rgb(213, 126, 0);")
        
        self.label_m2 = QtWidgets.QLabel(self.centralwidget)
        self.label_m2.setGeometry(QtCore.QRect(10, 100, 80, 30))
        self.label_m2.setObjectName("label")
        self.label_m2.setWordWrap(True)
        self.label_m2.setStyleSheet("background-color: rgb(213, 126, 0);")
        
        self.label_v1i = QtWidgets.QLabel(self.centralwidget)
        self.label_v1i.setGeometry(QtCore.QRect(10, 135, 80, 30))
        self.label_v1i.setObjectName("label")
        self.label_v1i.setWordWrap(True)
        self.label_v1i.setStyleSheet("background-color: rgb(213, 126, 0);")
        
        self.label_v2i = QtWidgets.QLabel(self.centralwidget)
        self.label_v2i.setGeometry(QtCore.QRect(10, 170, 80, 30))
        self.label_v2i.setObjectName("label")
        self.label_v2i.setWordWrap(True)
        self.label_v2i.setStyleSheet("background-color: rgb(213, 126, 0);")
        
        self.label_vf = QtWidgets.QLabel(self.centralwidget)
        self.label_vf.setGeometry(QtCore.QRect(10, 205, 80, 30))
        self.label_vf.setObjectName("label")
        self.label_vf.setWordWrap(True)
        self.label_vf.setStyleSheet("background-color: rgb(213, 126, 0);")
        
        self.label_u = QtWidgets.QLabel(self.centralwidget)
        self.label_u.setGeometry(QtCore.QRect(10, 240, 80, 30))
        self.label_u.setObjectName("label")
        self.label_u.setWordWrap(True)
        self.label_u.setStyleSheet("background-color: rgb(213, 126, 0);")
        
        self.lineEdit_ieve = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_ieve.setGeometry(QtCore.QRect(95, 205, 161, 31))
        self.lineEdit_ieve.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.lineEdit_ieve.setObjectName("lineEdit_ieve")
        self.lineEdit_ieve.setPlaceholderText("IE, E")
        self.lineEdit_m1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_m1.setGeometry(QtCore.QRect(95, 65, 161, 31))
        self.lineEdit_m1.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.lineEdit_m1.setObjectName("lineEdit_m1")
        self.lineEdit_m1.setPlaceholderText("kilograms")
        self.lineEdit_m2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_m2.setGeometry(QtCore.QRect(95, 100, 161, 31))
        self.lineEdit_m2.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.lineEdit_m2.setObjectName("lineEdit_m2")
        self.lineEdit_m2.setPlaceholderText("kilograms")
        self.lineEdit_vi1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_vi1.setGeometry(QtCore.QRect(95, 135, 161, 31))
        self.lineEdit_vi1.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.lineEdit_vi1.setObjectName("lineEdit_vi1")
        self.lineEdit_vi1.setPlaceholderText("meters/second")
        self.lineEdit_vi2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_vi2.setGeometry(QtCore.QRect(95, 170, 161, 31))
        self.lineEdit_vi2.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.lineEdit_vi2.setObjectName("lineEdit_vi2")
        self.lineEdit_vi2.setPlaceholderText("meters/second")
        self.lineEdit_vfe = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_vfe.setGeometry(QtCore.QRect(95, 170, 161, 31))
        self.lineEdit_vfe.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.lineEdit_vfe.setObjectName("lineEdit_vi2")
        self.lineEdit_vfe.setPlaceholderText("meters/second")
        self.lineEdit_u = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_u.setGeometry(QtCore.QRect(95, 240, 161, 31))
        self.lineEdit_u.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.lineEdit_u.setObjectName("lineEdit_u")
        self.lineEdit_u.setPlaceholderText("m1,m2,V1,V2,V3,Vo1,Vo2")        
        
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Solve 1D Momentum"))
        
        self.calc_button.setStatusTip(_translate("MainWindow", "Calculate"))
        self.calc_button.setText(_translate("MainWindow", "Calculate"))
        self.calc_button.setShortcut(_translate("MainWindow", "="))
        
        self.label_inform.setText(_translate("MainWindow", "By establishing a system of masses with their respective velocities, including the type of collision allows for 1D,"
        " Momentum problems to be calculated with respect to the energy within the system. These problems are very similar to 1D Kinematics Problems."))
        self.label_m1.setText(_translate("MainWindow", "Mass_1"))
        self.label_m2.setText(_translate("MainWindow", "Mass_2"))
        self.label_v1i.setText(_translate("MainWindow", "Initial Velocity(m1)"))
        self.label_v2i.setText(_translate("MainWindow", "Initial Velocity(m2)"))
        self.label_vf.setText(_translate("MainWindow", "Final Velocity"))
        self.label_u.setText(_translate("MainWindow", "Unknown"))
        self.label_answer.setText(_translate("MainWindow", "Answer"))
        self.label_answer2.setText(_translate("MainWindow", "Answer2"))

    def calculate(self):
        print("Hello World")
        
        def KE(m, v):
            return (m * v**2)/2
        def number(s):
            try:
                float(s)
                return True
            except ValueError:
                return False
        hmmm = ['IE', 'E']
        geez = "We don't have the facilities for that mate"
        cat = True
        let = ['m1','m2','V1','V2','V3','Vo1','Vo2']
        while cat:
            IEvE = self.lineEdit_ieve.text()
            if IEvE in hmmm:
                break
            else:
                self.label_answer.setText("Answer:" + geez)
                break
        if IEvE == 'IE':
            m1 = self.lineEdit_m1.text()
            if number(m1):
                m1 = float(m1)    
            m2 = self.lineEdit_m2.text()
            if number(m2):
                m2 = float(m2)
            V1 = self.lineEdit_vi1.text()
            if number(V1):
                V1 = float(V1)
            V2 = self.lineEdit_vi2.text()
            if number(V2):
                V2 = float(V2)
            V3 = self.lineEdit_vfe.text()
            if number(V3):
                V3 = float(V3)
            unknown = self.lineEdit_u.text()
            wow = True
            while wow:
                if unknown not in let:
                    self.label_answer.setText("Answer:" + geez)
                    wow = False
                if unknown == 'V3':
                    if (type(m1) == float and type(m2) == float and type(V1) == float and type(V2) == float): 
                        V3 = (m1*V1 + m2*V2)/(m1 + m2)
                        self.label_answer.setText("Answer:" + str(V3))
                        wow = False
                    else:
                        self.label_answer.setText("Answer:" + geez)
                        wow = False
                if unknown == 'V1':
                    if (type(m1) == float and type(m2) == float and type(V1) == float and type(V3) == float): 
                        V1 = (V3 * (m1 + m2) - m2*V2)/m1
                        self.label_answer.setText("Answer:" + str(V1))
                        wow = False
                    else:
                        self.label_answer.setText("Answer:" + geez)
                        wow = False
                if unknown == 'V2':
                    if (type(m1) == float and type(m2) == float and type(V1) == float and type(V3) == float): 
                        V2= (V3 * (m1 + m2) - m1*V1)/m2
                        self.label_answer.setText("Answer:" + str(V2))
                        wow = False
                    else:
                        self.label_answer.setText("Answer:" + geez)
                        wow = False
                if unknown == 'm1':
                    if (type(V2) == float and type(m2) == float and type(V1) == float and type(V3) == float): 
                        m1 = (m2*(V3 - V2))/(V1 - V3) 
                        self.label_answer.setText("Answer:" + str(m1))
                        wow = False
                    else:
                        self.label_answer.setText("Answer:" + geez)
                        wow = False
                if unknown == 'm2':
                    if (type(m1) == float and type(m2) == float and type(V1) == float and type(V3) == float): 
                        m2 = (m1*(V3 - V1))/(V2 - V3) 
                        self.label_answer.setText("Answer:" + str(m2))
                        wow = False
                    else:
                        self.label_answer.setText("Answer:" + geez)
                        wow = False
        if IEvE == 'E':
            m1 = self.lineEdit_m1.text()
            if number(m1):
                m1 = float(m1)    
            m2 = self.lineEdit_m2.text()
            if number(m2):
                m2 = float(m2)
            Vo1 = self.lineEdit_vi1.text()
            if number(Vo1):
                Vo1 = float(Vo1)
            Vo2 = self.lineEdit_vi2.text()
            if number(Vo2):
                Vo2 = float(Vo2)
            V1 = self.lineEdit_vf1.text()
            if number(V1):
                V1 = float(V1)
            V2 = self.lineEdit_vf2.text()
            if number(V2):
                V2 = float(V2)
            unknown = self.lineEdit_u.text()
            wow = True
            while wow:
                if unknown not in let:
                    self.label_answer.setText("Answer:" + geez)
                    wow = False
                if unknown == 'm1':
                    if (type(Vo1) == float and type(m2) == float and type(Vo2) == float and type(V2) == float and type(V1) == float): 
                        m1 = (m2*(V2 - Vo2))/(Vo1-V1)
                        self.label_answer.setText("Answer:" + str(m1))
                        wow = False
                    else:
                        self.label_answer.setText("Answer:" + geez)
                        wow = False
                if unknown == 'm2':
                    if (type(Vo1) == float and type(m1) == float and type(Vo2) == float and type(V2) == float and type(V1) == float): 
                        m2 = (m1*(V1 - Vo1))/(Vo2-V2)
                        self.label_answer.setText("Answer:" + str(m2))
                        wow = False
                    else:
                        self.label_answer.setText("Answer:" + geez)
                        wow = False
                if unknown == 'Vo1':
                    if (type(m2) == float and type(m1) == float and type(Vo2) == float and type(V2) == float and type(V1) == float): 
                        Vo1 = (m1*V1 + m2*V2 - m2*Vo2)/m1
                        self.label_answer.setText("Answer:" + str(Vo1))
                        wow = False
                    else:
                        self.label_answer.setText("Answer:" + geez)
                        wow = False
                if unknown == 'Vo2':
                    if (type(m2) == float and type(m1) == float and type(Vo1) == float and type(V2) == float and type(V1) == float): 
                        Vo2 = (m1*V1 + m2*V2 - m1*Vo1)/m2
                        self.label_answer.setText("Answer:" + str(Vo2))
                        wow = False
                    else:
                        self.label_answer.setText("Answer:" + geez)
                        wow = False
                if unknown == 'V1':
                    if (type(m2) == float and type(m1) == float and type(Vo1) == float and type(V2) == float and type(Vo2) == float): 
                        V1 = (m1*Vo1 + m2*Vo2 - m2*Vo2)/m1
                        self.label_answer.setText("Answer:" + str(V1))
                        wow = False
                    else:
                        self.label_answer.setText("Answer:" + geez)
                        wow = False
                if unknown == 'V2':
                    if (type(m2) == float and type(m1) == float and type(Vo1) == float and type(V1) == float and type(Vo2) == float): 
                        V2 = (m1*Vo1 + m2*Vo2 - m1*Vo1)/m2
                        self.label_answer.setText("Answer:" + str(V2))
                        wow = False
                    else:
                        self.label_answer.setText("Answer:" + geez)
                        wow = False
            if (KE(m1, Vo1) + KE(m2, Vo2) == KE(m1, V1) + KE(m2, V2)):
                self.label_answer.setText("The collision is perfectly elastic")
            else:
                self.label_answer.setText("This collision is NOT perfectly elastic")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow5()
    ui.setup(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
