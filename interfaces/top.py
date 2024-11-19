from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Top(QFrame):
    def __init__(self, placeholder):
        super().__init__(placeholder)
        self.width = 0 # It automatically scales in the Screen
        self.height = 115
        self.setMinimumSize(QSize(self.width, self.height))
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.setStyleSheet("background:rgb(255, 0, 255);")
