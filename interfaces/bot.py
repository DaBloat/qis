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
        self.height = 130
        self.setObjectName("bottomFrame")
        self.setMinimumSize(QSize(self.width, self.height))
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.setStyleSheet("QFrame#bottomFrame{background:rgb(234, 196, 163);}")

        self.layout = HorizontalOrganizer(self)

        self.vertlayout = VerticalOrganizer(self)
        
        self.bloch = Button(self, 'Bloch Sphere')
        self.bloch.clicked.connect(self.blochClicked)

        self.matrix = Button(self, 'State Vectors')
        self.matrix.clicked.connect(self.vectorClicked)



        self.scrollarea = ScrollArea(self, self.scene, "AlwaysOff", "AlwaysOn")

        self.rampart = QWidget()
        
        self.bloch_types = QFrame(self.rampart)
        self.scroll_bloch_items = HorizontalOrganizer(self.bloch_types)
        self.bloch_sph = BlochButton(self, self.scene)
        self.scroll_bloch_items.add(self.bloch_sph)
        self.scroll_bloch_items.stretch()

        self.vector_types = QFrame(self.rampart)
        self.scroll_vector_items = HorizontalOrganizer(self.vector_types)
        self.ket0 = Ket0Button(self, self.scene)
        self.ket1 = Ket1Button(self, self.scene)
        self.sigmax = SigmaXButton(self, self.scene)
        self.sigmay = SigmaYButton(self, self.scene)
        self.sigmaz = SigmaZButton(self, self.scene)
        self.addm = AddOwnMatrixButton(self, self.scene)
        self.vector_types.hide()

        for buttons in [self.ket0, self.ket1, self.sigmax, self.sigmay, self.sigmaz, self.addm]:
            self.scroll_vector_items.add(buttons)

        self.scroll_vector_items.stretch()

        self.scrollarea.setWidget(self.rampart)
        
    
        self.history = HistoryBlock(self)

        self.output_matr = OutputMatrix(self)
        for i in [self.bloch, self.matrix]:
            i.setSize(100,0)
            self.vertlayout.add(i)

        self.layout.add(self.vertlayout)
        self.layout.add(self.scrollarea)
        self.layout.add(self.history)
        self.layout.add(self.output_matr)
        self.layout.stretch()

    def blochClicked(self):
        self.bloch_types.show()
        self.vector_types.hide()


    def vectorClicked(self):
        self.bloch_types.hide()
        self.vector_types.show()

