import sys
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtGui import QIcon


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.title = "PhysTops for Phonies"
        self.left = 500
        self.top = 100
        self.width = 1000
        self.height = 750
        iconName = "home.png"
        
        self.UiComponents()
        self.InitWindow()
  
    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()
    
    def UiComponents(self):
        #Qrect(how far right, how far down, width, height)
        
        button_1km = QPushButton("One Dimensional Kinematics", self)
        button_1km.setGeometry(QRect(245, 150, 250, 100))
        button_1km.setToolTip("Solve One Dimensional Kinematics Problems")
        button_1km.clicked.connect(self.clicked_1km)
        
        button_2km = QPushButton("Two Dimensional Kinematics", self)
        button_2km.setGeometry(QRect(505, 150, 250, 100))
        button_2km.setToolTip("Solve Two Dimensional Kinematics Problems")
        button_2km.clicked.connect(self.clicked_2km)
        
        button_1p = QPushButton("One Dimensional Momentum", self)
        button_1p.setGeometry(QRect(245, 260, 250, 100))
        button_1p.setToolTip("Solve One Dimensional Momentum Problems")
        button_1p.clicked.connect(self.clicked_1p)
        
        button_2p = QPushButton("Two Dimensional Momentum", self)
        button_2p.setGeometry(QRect(505, 260, 250, 100))
        button_2p.setToolTip("Solve Two Dimensional Momentum Problems")
        button_2p.clicked.connect(self.clicked_2p)
        
        button_bf = QPushButton("Basic Forces", self)
        button_bf.setGeometry(QRect(245, 370, 250, 100))
        button_bf.setToolTip("Solve Basic Force Problems")
        button_bf.clicked.connect(self.clicked_1p)
        
        button_if = QPushButton("Inclined Forces", self)
        button_if.setGeometry(QRect(505, 370, 250, 100))
        button_if.setToolTip("Solve Inclined Forces Problems")
        button_if.clicked.connect(self.clicked_2p)
        
        button_exit = QPushButton("Close Program", self)
        button_exit.setGeometry(QRect(400, 550, 200, 90))
        button_exit.setToolTip("Close the Application")
        button_exit.clicked.connect(self.clicked_exit)
        
        
    def clicked_1km(self):
        print("Hello World")
        
    def clicked_2km(self):
        print("hi")
    
    def clicked_1p(self):
        print("Hello World")
        
    def clicked_2p(self):
        print("hi")
    
    def clicked_bf(self):
        print("Hello World")
        
    def clicked_if(self):
        print("hi")
        
    def clicked_exit(self):
        sys.exit()
        
    
App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
