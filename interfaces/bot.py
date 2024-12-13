from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from utils.widgets import *
from utils.layouts import *
from qitems.qubit_items import *


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
        
        self.gate = GateOperations(self, self.scene)
        
        self.layout.add(self.gate)
        self.layout.stretch()


class GateOperations(QFrame):
    def __init__(self, placeholder, scene):
        super().__init__(placeholder)
        self.scene = scene
        self.setObjectName('gateOps')
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        self.setMinimumSize(500,0)
        self.setStyleSheet("""QFrame#gateOps{background: rgb(255,255,255);
                                    border-radius: 15px;}""")

        self.quanButton_layouts = VerticalOrganizer(self)
        self.title = QLabel('Gate Operations')
        self.title.setStyleSheet('font-size: 7.5pt')
        self.title.setAlignment(Qt.AlignLeft)


        self.quanButton_layouts.add(self.title)
        self.scrollWid = QWidget()
        self.scrollFrame = QFrame(self.scrollWid)
        self.scroll = ScrollArea(self, 'AlwaysOff', 'AlwaysOn')
        self.scroll.setWidget(self.scrollFrame)

        self.quanButton_layouts.add(self.scroll)

        self.ket0 = Ket0Button(self, self.scene)
        self.ket1 = Ket1Button(self, self.scene)
        self.sigmax = SigmaXButton(self, self.scene)
        self.sigmay = SigmaYButton(self, self.scene)
        self.sigmaz = SigmaZButton(self, self.scene)
        self.unitary = UnitaryButton(self, self.scene)
        self.hadamard = HadamardButton(self, self.scene)
        
        self.butt = HorizontalOrganizer(self.scrollFrame)
        for i in [self.ket0, self.ket1, self.sigmax, self.sigmay, self.sigmaz, self.unitary, self.hadamard]:
            self.butt.add(i)
        self.butt.stretch() 
