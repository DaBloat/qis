from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import qutip as qp
import numpy as np

class QubitItem(QGraphicsPixmapItem):
    def __init__(self, img):
        super().__init__()
        self.img = img
        self.editPixmap(self.img)

    def editPixmap(self, image):
        self.pix = QPixmap(image)
        size = min(self.pix.width(), self.pix.height())

        target = QPixmap(size, size)
        target.fill(Qt.transparent)

        qp = QPainter(target)
        qp.setRenderHints(qp.Antialiasing)
        path = QPainterPath()
        path.addEllipse(0, 0, size, size)
        qp.setClipPath(path)

        sourceRect = QRect(0, 0, size, size)
        sourceRect.moveCenter(self.pix.rect().center())
        qp.drawPixmap(target.rect(), self.pix, sourceRect)
        qp.end()
        self.setPixmap(target)
        self.setAcceptHoverEvents(True)

    def mousePressEvent(self, event):
        pass

    def mousePos(self, event):
        orig_position = event.lastScenePos()
        updated_position = event.scenePos()
        original = self.scenePos()
        updated_cursorX = updated_position.x() - orig_position.x() + original.x()
        updated_cursorY = updated_position.y() - orig_position.y() + original.y()
        self.setPos(QPointF(updated_cursorX, updated_cursorY))

class QubitItemButton(QToolButton):
    def __init__(self, placeholder, scene, img, name, x=100,y=75):
        super().__init__(placeholder)
        self.scene = scene
        self.img = img
        self.name = name
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.setFixedSize(x, y)
        self.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.icon = QIcon(self.img)
        self.setIconSize(QSize(50,50))
        self.setIcon(self.icon)
        self.setText(self.name)


class Bloch(QubitItem):
    def __init__(self, scene, img='assets/bloch_sphere.png'):
        super().__init__(img)
        self.scene = scene
        self.name = 'BlochSphere'
        self.qnum = 1
        self.bloch = qp.Bloch(figsize=[2,2])
        self.bloch.font_size = 10

    def mouseReleaseEvent(self, event):
        if len(self.collidingItems()) == 1 and self.qnum != self.collidingItems()[0].qnum and self.collidingItems()[0].qnum == 2:
            print(self.collidingItems()[0].name)
            self.qOb = qp.Qobj(self.collidingItems()[0].matrix)
            self.bloch.add_states(self.qOb)
            self.bloch.save('appData/bloch1.png')
            self.editPixmap(image='appData/bloch1.png')
            self.img = 'appData/bloch1.png'
            self.scene.removeItem(self.collidingItems()[0])
        else:
            pass
            # self.editPixmap(self.img)

    def mouseMoveEvent(self, event):
        self.mousePos(event)
        if len(self.collidingItems()) != 0:
            print(f'Collided with {self.collidingItems()[0]}')
            if self.qnum != self.collidingItems()[0].qnum and self.collidingItems()[0].qnum == 2:
                self.setToolTip('BRO')
            else:
                self.setToolTip('Nuh Uh!')
        else:
            pass
            # self.editPixmap(self.img)


class BlochButton(QubitItemButton):
    def __init__(self, placeholder, scene, img='assets/bloch_sphere.png', name='Bloch Sphere'):
        super().__init__(placeholder, scene, img, name)
        self.scene = scene
        self.clicked.connect(self.addBlochToTheScene)

    def addBlochToTheScene(self):
        print("Added for Bloch")
        self.b = Bloch(self.scene, self.img)
        self.scene.addItem(self.b)

class Ket0(QubitItem):
    def __init__(self, scene, img='assets/ket0.png'):
        super().__init__(img)
        self.scene = scene
        self.name = "Ket0"
        self.qnum = 2
        self.matrix = np.array([[1],[0]])

    def mouseMoveEvent(self, event):
        self.mousePos(event)

    def mouseReleaseEvent(self, event):
        if len(self.collidingItems()) == 1 and self.qnum != self.collidingItems()[0].qnum and self.collidingItems()[0].qnum == 1:
            print(self.collidingItems()[0].name)
            self.collidingItems()[0].bloch.add_states(qp.Qobj(self.matrix))
            self.collidingItems()[0].bloch.save('appData/bloch1.png')
            self.collidingItems()[0].editPixmap(image='appData/bloch1.png')
            self.collidingItems()[0].img = 'appData/bloch1.png'
            self.scene.removeItem(self)
        else:
            pass


class Ket0Button(QubitItemButton):
    def __init__(self, placeholder, scene, img='assets/ket0.png', name='Ket 0'):
        super().__init__(placeholder, scene, img, name)
        self.clicked.connect(self.addKet0ToTheScene)
        self.scene = scene

    def addKet0ToTheScene(self):
        print("Added for Ket0")
        self.ket0 = Ket0(self.scene, self.img)
        self.scene.addItem(self.ket0)


class Ket1(QubitItem):
    def __init__(self, scene, img='assets/ket1.png'):
        super().__init__(img)
        self.scene = scene
        self.name = "Ket1"
        self.qnum = 2
        self.matrix = np.array([[0],[1]])

    def mouseMoveEvent(self, event):
        self.mousePos(event)

    def mouseReleaseEvent(self, event):
        if len(self.collidingItems()) == 1 and self.qnum != self.collidingItems()[0].qnum and self.collidingItems()[0].qnum == 1:
            print(self.collidingItems()[0].name)
            self.collidingItems()[0].bloch.add_states(qp.Qobj(self.matrix))
            self.collidingItems()[0].bloch.save('appData/bloch1.png')
            self.collidingItems()[0].editPixmap(image='appData/bloch1.png')
            self.collidingItems()[0].img = 'appData/bloch1.png'
            self.scene.removeItem(self)
        else:
            pass

class Ket1Button(QubitItemButton):
    def __init__(self, placeholder, scene, img='assets/ket1.png', name='Ket 1'):
        super().__init__(placeholder, scene, img, name)
        self.scene = scene
        self.clicked.connect(self.addKet1ToTheScene)

    def addKet1ToTheScene(self):
        print("Added for Ket1")
        self.ket1 = Ket1(self.scene, self.img)
        self.scene.addItem(self.ket1)


class SigmaX(QubitItem):
    def __init__(self, img='assets/sigmax.png'):
        super().__init__(img)
        self.name = 'SigmaX'
        self.qnum = 3


class SigmaXButton(QubitItemButton):
    def __init__(self, placeholder, scene, img='assets/sigmax.png', name='Sigma X'):
        super().__init__(placeholder, scene, img, name)
        self.clicked.connect(self.addSigmaxToTheScene)

    def addSigmaxToTheScene(self):
        print("Added for Sigma X")
        self.sigmax = SigmaX(self.img)
        self.scene.addItem(self.sigmax)


class SigmaY(QubitItem):
    def __init__(self, img='assets/sigmay.png'):
        super().__init__(img)
        self.name = 'SigmaY'
        self.qnum = 3



class SigmaYButton(QubitItemButton):
    def __init__(self, placeholder, scene, img='assets/sigmay.png', name='Sigma Y'):
        super().__init__(placeholder, scene, img, name)
        self.clicked.connect(self.addSigmayToTheScene)

    def addSigmayToTheScene(self):
        print("Added for Sigma Y")
        self.sigmay = SigmaY(self.img)
        self.scene.addItem(self.sigmay)

class SigmaZ(QubitItem):
    def __init__(self, img='assets/sigmaz.png'):
        super().__init__(img)
        self.name = 'SigmaZ'
        self.qnum = 3



class SigmaZButton(QubitItemButton):
    def __init__(self, placeholder, scene, img='assets/sigmaz.png', name='Sigma Z'):
        super().__init__(placeholder, scene, img, name)
        self.clicked.connect(self.addSigmazToTheScene)

    def addSigmazToTheScene(self):
        print("Added for Sigma Z")
        self.sigmaz = SigmaZ(self.img)
        self.scene.addItem(self.sigmaz)


class AddMatrix(QubitItem):
    def __init__(self, img='assets/addMatrix.png'):
        super().__init__(img)
        self.name = 'AddedMatrix'
        self.qnum = 3

class AddOwnMatrixButton(QubitItemButton):
    def __init__(self, placeholder, scene, img='assets/addMatrix.png', name='Add Own Matrix'):
        super().__init__(placeholder, scene, img, name)
        self.clicked.connect(self.addMatrixToTheScene)

    def addMatrixToTheScene(self):
        print("Added for Own Matrix")
        self.oMatrix = AddMatrix(self.img)
        self.scene.addItem(self.oMatrix)
