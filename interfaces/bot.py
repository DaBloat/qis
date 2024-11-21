from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Bottom(QFrame):
    def __init__(self, placeholder, recipient):
        super().__init__(placeholder)
        self.scene = recipient
        self.width = 0 # It automatically scales in the Screen
        self.height = 130
        self.setObjectName("bottomFrame")
        self.setMinimumSize(QSize(self.width, self.height))
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.setStyleSheet("QFrame#bottomFrame{background:rgb(234, 196, 163);}")

        self.layout = QHBoxLayout(self)

        self.vertlayout = QVBoxLayout(self)
        
        self.button1 = QPushButton('qubit')
        self.button2 = QPushButton('operators')
        self.button3 = QPushButton('functions')
        self.button4 = QPushButton('gates')

        for i in [self.button1,self.button2, self.button3, self.button4]:
            self.vertlayout.addWidget(i)

        self.layout.addLayout(self.vertlayout)

        self.scrollarea = QScrollArea(self)
        self.scrollarea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollarea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.layout.addWidget(self.scrollarea)

