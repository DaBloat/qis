from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from utils.buttons import *
from utils.layouts import *
from qitems.qubit_items import *

class TitleCard(QFrame):
    def __init__(self, placeholder, title, description):
        super().__init__(placeholder)
        self.setObjectName('titleCard')
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        self.setMinimumSize(150,0)
        self.setStyleSheet("""QFrame#titleCard{background: rgb(255,255,255);
                                    border-style:solid;
                                    border-width: 2px;
                                    border-radius: 15px;}""")

        self.title_layout = QVBoxLayout(self)
        self.title = QLabel(title)
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setStyleSheet('font: 87 48pt "Arial Black";')


        self.description = QLabel(description)
        self.description.setStyleSheet('font-size: 7.5pt')
        self.description.setAlignment(Qt.AlignCenter)
        
        for labels in [self.title, self.description]:
            self.title_layout.addWidget(labels)

class ScrollArea(QScrollArea):
    def __init__(self, placeholder, vertOpt, horiOpt):
        super().__init__(placeholder)
        self.opt = {'AlwaysOn':Qt.ScrollBarAlwaysOn, 
                    "AlwaysOff":Qt.ScrollBarAlwaysOff}
        self.setVerticalScrollBarPolicy(self.opt[vertOpt])
        self.setHorizontalScrollBarPolicy(self.opt[horiOpt])
        self.setWidgetResizable(True)
        self.setAlignment(Qt.AlignCenter)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

class BlochSphereControl(QFrame):
    def __init__(self, placeholder, scene):
        super().__init__(placeholder)
        self.scene = scene        
        self.sphere = Bloch(self.scene)
        self.setObjectName('BlochSphereControl')
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        self.setMinimumSize(50,0)
        self.setStyleSheet("""QFrame#BlochSphereControl{background: rgb(255,255,255);
                                    border-radius: 15px;}""")

        self.controlButtons = VerticalOrganizer(self)
        self.addBloch = AddBlochButton(self, self.scene, self.sphere)
        self.refreshBloch = RefreshBlochButton(self, self.scene, self.sphere)
        self.deleteBloch = DeleteBlochButton(self, self.scene, self.sphere)

        for button in [self.addBloch, self.refreshBloch, self.deleteBloch]:
            self.controlButtons.add(button)
        
    

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
        self.sphase = SPhaseButton(self, self.scene)
        self.tphase = TPhaseButton(self, self.scene)
        self.rotx = RotationXButton(self, self.scene)
        self.roty = RotationYButton(self, self.scene)
        self.rotz = RotationZButton(self, self.scene)
        
        self.butt = HorizontalOrganizer(self.scrollFrame)
        for button in [self.ket0, self.ket1, self.sigmax, self.sigmay, self.sigmaz, self.unitary, self.hadamard, self.sphase, self.tphase, self.rotx, self.roty, self.rotz]:
            self.butt.add(button)
        self.butt.stretch() 
        
