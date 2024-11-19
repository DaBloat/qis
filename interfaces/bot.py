from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Bottom(QFrame):
    def __init__(self, placeholder, recipient):
        super().__init__(placeholder)
        self.scene = recipient
        self.width = 0 # It automatically scales in the Screen
        self.height = 130
        self.setMinimumSize(QSize(self.width, self.height))
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.setStyleSheet("background: rgb(170, 0, 0);")
