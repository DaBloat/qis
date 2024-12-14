from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from utils.widgets import *
from utils.layouts import *
from utils.buttons import *


class Bottom(QFrame):
    def __init__(self, placeholder, recipient):
        super().__init__(placeholder)
        self.scene = recipient
        self.width = 0 # It automatically scales in the Screen
        self.height = 150
        self.setObjectName("bottomFrame")
        self.setMinimumSize(QSize(self.width, self.height))
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.setStyleSheet("""QFrame#bottomFrame{background:rgb(234, 196, 163);}
                              """)

        self.layout = HorizontalOrganizer(self)

        self.blochControl = BlochSphereControl(self, self.scene)
        
        self.gate = GateOperations(self, self.scene)
        
        self.layout.add(self.blochControl)
        self.layout.add(self.gate)
        self.layout.stretch()

