from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from qitems.qubit_items import *

class Button(QPushButton):
    def __init__(self, placeholder, text):
        super().__init__(placeholder)
        self.setText(text)

    def setSize(self, width, height):
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.setMinimumSize(width, height)

class QubitItemButton(QToolButton):
    def __init__(self, placeholder, scene, img, name, x=70,y=60):
        super().__init__(placeholder)
        self.scene = scene
        self.img = img
        self.name = name
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.setFixedSize(x, y)
        self.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.icon = QIcon(self.img)
        self.setIconSize(QSize(40,40))
        self.setIcon(self.icon)
        self.setText(self.name)

class AddBlochButton(QToolButton):
    def __init__(self, placeholder, scene, bloch, img='assets/blochadd.png', name='', x=50, y=40):
        super().__init__(placeholder)
        self.b = bloch
        self.scene = scene
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.setFixedSize(x, y)
        self.icon = QIcon(img)
        self.setIconSize(QSize(30,30))
        self.setIcon(self.icon)
        self.clicked.connect(self.addBlochToTheScene)

    def addBlochToTheScene(self):
        item_in_scene = False
        for item in self.scene.items():
            if item == self.b:
                item_in_scene = True
                break
        if not item_in_scene:
            self.scene.addItem(self.b)
        else:
            pass
    

class RefreshBlochButton(QToolButton):
    def __init__(self, placeholder, scene, bloch, img='assets/blochrefresh.png', name='', x=50, y=40):
        super().__init__(placeholder)
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.b = bloch
        self.scene = scene
        self.setFixedSize(x, y)
        self.icon = QIcon(img)
        self.setIconSize(QSize(30,30))
        self.setIcon(self.icon)
        self.clicked.connect(self.refreshBloch)

    def refreshBloch(self):
        self.b.bloch.clear()
        self.b.bloch.save('appData/bloch1.png')
        self.b.editPixmap(image='appData/bloch1.png')
        self.b.img = 'appData/bloch1.png'

class DeleteBlochButton(QToolButton):
    def __init__(self, placeholder, scene, bloch, img='assets/blochdelete.png', name='', x=50, y=40):
        super().__init__(placeholder)
        self.b = bloch
        self.scene = scene
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.setFixedSize(x, y)
        self.icon = QIcon(img)
        self.setIconSize(QSize(30,30))
        self.setIcon(self.icon)
        self.clicked.connect(self.deleteBloch)

    def deleteBloch(self):
        self.b.bloch.clear()
        self.b.bloch.save('appData/bloch1.png')
        self.b.editPixmap(image='appData/bloch1.png')
        self.b.img = 'appData/bloch1.png'
        self.scene.removeItem(self.b)

class Ket0Button(QubitItemButton):
    def __init__(self, placeholder, scene, img='assets/ket0.png', name='Ket 0'):
        super().__init__(placeholder, scene, img, name)
        self.clicked.connect(self.addKet0ToTheScene)
        self.scene = scene

    def addKet0ToTheScene(self):
        print("Added for Ket0")
        self.ket0 = Ket0(self.scene, self.img)
        self.scene.addItem(self.ket0)

class Ket1Button(QubitItemButton):
    def __init__(self, placeholder, scene, img='assets/ket1.png', name='Ket 1'):
        super().__init__(placeholder, scene, img, name)
        self.scene = scene
        self.clicked.connect(self.addKet1ToTheScene)

    def addKet1ToTheScene(self):
        print("Added for Ket1")
        self.ket1 = Ket1(self.scene, self.img)
        self.scene.addItem(self.ket1)

class SigmaXButton(QubitItemButton):
    def __init__(self, placeholder, scene, img='assets/sigmax.png', name='Sigma X'):
        super().__init__(placeholder, scene, img, name)
        self.clicked.connect(self.addSigmaxToTheScene)

    def addSigmaxToTheScene(self):
        print("Added for Sigma X")
        self.sigmax = SigmaX(self.img)
        self.scene.addItem(self.sigmax)

class SigmaYButton(QubitItemButton):
    def __init__(self, placeholder, scene, img='assets/sigmay.png', name='Sigma Y'):
        super().__init__(placeholder, scene, img, name)
        self.clicked.connect(self.addSigmayToTheScene)

    def addSigmayToTheScene(self):
        print("Added for Sigma Y")
        self.sigmay = SigmaY(self.img)
        self.scene.addItem(self.sigmay)


class SigmaZButton(QubitItemButton):
    def __init__(self, placeholder, scene, img='assets/sigmaz.png', name='Sigma Z'):
        super().__init__(placeholder, scene, img, name)
        self.clicked.connect(self.addSigmazToTheScene)

    def addSigmazToTheScene(self):
        print("Added for Sigma Z")
        self.sigmaz = SigmaZ(self.img)
        self.scene.addItem(self.sigmaz)

class UnitaryButton(QubitItemButton):
    def __init__(self, placeholder, scene, img='assets/unitary.png', name='Unitary'):
        super().__init__(placeholder, scene, img, name)
        self.clicked.connect(self.addUnitaryToTheScene)

    def addUnitaryToTheScene(self):
        print("Added Unitary Gate")
        self.unitary = UnitaryGate(self.img)
        self.scene.addItem(self.unitary)


class HadamardButton(QubitItemButton):
    def __init__(self, placeholder, scene, img='assets/hadamard.png', name='Hadamard'):
        super().__init__(placeholder, scene, img, name)
        self.clicked.connect(self.addHadamardToTheScene)

    def addHadamardToTheScene(self):
        print("Added Hadamard Gate")
        self.unitary = HadamardGate(self.img)
        self.scene.addItem(self.unitary)


class SPhaseButton(QubitItemButton):
    def __init__(self, placeholder, scene, img='assets/SPhase.png', name='S Phase'):
        super().__init__(placeholder, scene, img, name)
        self.clicked.connect(self.addSPhaseToTheScene)

    def addSPhaseToTheScene(self):
        print("Added SPhase Gate")
        self.sphase = SPhase(self.img)
        self.scene.addItem(self.sphase)

class TPhaseButton(QubitItemButton):
    def __init__(self, placeholder, scene, img='assets/TPhase.png', name='T Phase'):
        super().__init__(placeholder, scene, img, name)
        self.clicked.connect(self.addTPhaseToTheScene)

    def addTPhaseToTheScene(self):
        print("Added TPhase Gate")
        self.tphase = TPhase(self.img)
        self.scene.addItem(self.tphase)

        
class RotationXButton(QubitItemButton):
    def __init__(self, placeholder, scene, img='assets/rotationX.png', name='Rotation X'):
        super().__init__(placeholder, scene, img, name)
        self.clicked.connect(self.addrotationXToTheScene)

    def addrotationXToTheScene(self):
        print("Added X Rotation Gate")
        self.rotx = RotationX(self.img)
        self.scene.addItem(self.rotx)

class RotationYButton(QubitItemButton):
    def __init__(self, placeholder, scene, img='assets/rotationY.png', name='Rotation Y'):
        super().__init__(placeholder, scene, img, name)
        self.clicked.connect(self.addrotationYToTheScene)

    def addrotationYToTheScene(self):
        print("Added Y Rotation Gate")
        self.roty = RotationY(self.img)
        self.scene.addItem(self.roty)


class RotationZButton(QubitItemButton):
    def __init__(self, placeholder, scene, img='assets/rotationZ.png', name='Rotation Z'):
        super().__init__(placeholder, scene, img, name)
        self.clicked.connect(self.addrotationZToTheScene)

    def addrotationZToTheScene(self):
        print("Added Z Rotation Gate")
        self.rotz = RotationY(self.img)
        self.scene.addItem(self.rotz)

