from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import qutip as qp
from qutip_qip.operations import *
import numpy as np

class QubitItem(QGraphicsPixmapItem):
    def __init__(self, img):
        super().__init__()
        self.img = img
        self.editPixmap(self.img)
        self.setAcceptHoverEvents(True)
        self.setFlag(QGraphicsPixmapItem.ItemIsSelectable)
        self.pen = QPen(QColor("black"))
        self.pen.setWidth(2)

 
    def paint(self, painter, option, widget=None):
        super().paint(painter, option, widget)
        painter.setPen(self.pen)
        painter.setRenderHints(painter.Antialiasing)
        path = QPainterPath()
        painter.drawEllipse(self.boundingRect())
        
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

    def mousePressEvent(self, event):
        self.pen = QPen(QColor("red"))

    def mouseReleaseEvent(self, event):
        self.pen = QPen(QColor("black"))


    def mousePos(self, event):
        orig_position = event.lastScenePos()
        updated_position = event.scenePos()
        original = self.scenePos()
        updated_cursorX = updated_position.x() - orig_position.x() + original.x()
        updated_cursorY = updated_position.y() - orig_position.y() + original.y()
        self.setPos(QPointF(updated_cursorX, updated_cursorY))
        
        # Selected is always at the top 
        if self.collidingItems() != 0:
            for i in self.collidingItems():
                i.setZValue(-1)
                self.setZValue(1)

class Bloch(QGraphicsPixmapItem):
    def __init__(self,scene, img='assets/bloch_sphere.png'):
        super().__init__()
        self.scene = scene
        self.name = 'BlochSphere'
        self.qnum = 1
        self.editPixmap(img)
        self.bloch = qp.Bloch(figsize=[4,4])
        self.bloch.font_size = 12
        self.states_stack = []
        self.output_stack = []

    def bloch_plot(self, qitem):
        try:
            if (len(self.output_stack) == 0 and qitem.qnum == 2) or qitem.qnum == 2:
                self.output_stack = []
                self.states_stack = []
                self.output_stack.append(qp.Qobj(qitem.matrix))
                self.states_stack.append(qitem.name)
                self.scene.removeItem(qitem)
            elif len(self.output_stack) != 0:
                current = qitem.matrix @ qp.Qobj(self.output_stack[-1])
                self.output_stack.append(current)
                self.states_stack.append(qitem.name)
                self.scene.removeItem(qitem)
            self.bloch.clear()
            self.bloch.add_states(qp.Qobj(self.output_stack[-1]))
            self.bloch.save('appData/bloch1.png')
            self.editPixmap(image='appData/bloch1.png')
            self.img = 'appData/bloch1.png'
            print(self.states_stack)
            print(len(self.output_stack))
        except:
            print("BRUH")


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

    def mousePressEvent(self, event):
        pass

    def mousePos(self, event):
        orig_position = event.lastScenePos()
        updated_position = event.scenePos()
        original = self.scenePos()
        updated_cursorX = updated_position.x() - orig_position.x() + original.x()
        updated_cursorY = updated_position.y() - orig_position.y() + original.y()
        self.setPos(QPointF(updated_cursorX, updated_cursorY))

    def mouseReleaseEvent(self, event):
        pass

    def mouseMoveEvent(self, event):
        self.mousePos(event)


class Ket0(QubitItem):
    def __init__(self, img='assets/ket0.png'):
        super().__init__(img)
        self.name = "Ket0"
        self.qnum = 2
        self.matrix = np.array([[1],[0]])

    def mouseMoveEvent(self, event):
        self.mousePos(event)

    def mouseReleaseEvent(self, event):
        self.pen = QPen(QColor("black"))
        if len(self.collidingItems()) == 1 and self.qnum != self.collidingItems()[0].qnum and self.collidingItems()[0].qnum == 1:
            print(self.collidingItems()[0].name)
            self.collidingItems()[0].bloch.clear()
            self.collidingItems()[0].bloch.add_states(qp.Qobj(self.matrix))
            self.collidingItems()[0].bloch.save('appData/bloch1.png')
            self.collidingItems()[0].editPixmap(image='appData/bloch1.png')
            self.collidingItems()[0].img = 'appData/bloch1.png'
            self.collidingItems()[0].bloch_plot(self)
        else:
            pass


class Ket1(QubitItem):
    def __init__(self, img='assets/ket1.png'):
        super().__init__(img)
        self.name = "Ket1"
        self.qnum = 2
        self.matrix = np.array([[0],[1]])

    def mouseMoveEvent(self, event):
        self.mousePos(event)

    def mouseReleaseEvent(self, event):
        self.pen = QPen(QColor("black"))
        if len(self.collidingItems()) == 1 and self.qnum != self.collidingItems()[0].qnum and self.collidingItems()[0].qnum == 1:
            print(self.collidingItems()[0].name)
            self.collidingItems()[0].bloch.clear()
            self.collidingItems()[0].bloch.add_states(qp.Qobj(self.matrix))
            self.collidingItems()[0].bloch.save('appData/bloch1.png')
            self.collidingItems()[0].editPixmap(image='appData/bloch1.png')
            self.collidingItems()[0].img = 'appData/bloch1.png'
            self.collidingItems()[0].bloch_plot(self)
        else:
            pass


class SigmaX(QubitItem):
    def __init__(self, img='assets/sigmax.png'):
        super().__init__(img)
        self.name = 'SigmaX'
        self.qnum = 3
        self.matrix = X(0).get_compact_qobj()

    def mouseMoveEvent(self, event):
        self.mousePos(event)

    def mouseReleaseEvent(self, event):        
        self.pen = QPen(QColor("black"))
        if len(self.collidingItems()) == 1 and self.collidingItems()[0].qnum == 1:
            self.collidingItems()[0].bloch_plot(self)


class SigmaY(QubitItem):
    def __init__(self, img='assets/sigmay.png'):
        super().__init__(img)
        self.name = 'SigmaY'
        self.qnum = 3
        self.matrix = Y(0).get_compact_qobj()

    def mouseMoveEvent(self, event):
        self.mousePos(event)

    def mouseReleaseEvent(self, event):
        self.pen = QPen(QColor("black"))
        if len(self.collidingItems()) == 1 and self.collidingItems()[0].qnum == 1:
            self.collidingItems()[0].bloch_plot(self)


class SigmaZ(QubitItem):
    def __init__(self, img='assets/sigmaz.png'):
        super().__init__(img)
        self.name = 'SigmaZ'
        self.qnum = 3
        self.matrix = Z(0).get_compact_qobj()

    def mouseMoveEvent(self, event):
        self.mousePos(event)

    def mouseReleaseEvent(self, event):
        self.pen = QPen(QColor("black"))
        if len(self.collidingItems()) == 1 and self.collidingItems()[0].qnum == 1:
            self.collidingItems()[0].bloch_plot(self)


class UnitaryGate(QubitItem):
    def __init__(self, img='assets/addMatrix.png'):
        super().__init__(img)
        self.name = 'Unitary Gate'
        self.qnum = 3

    def mouseMoveEvent(self, event):
        self.mousePos(event)

    def mouseReleaseEvent(self, event):
        self.pen = QPen(QColor("black"))
        if len(self.collidingItems()) == 1 and self.collidingItems()[0].qnum == 1:
            self.collidingItems()[0].bloch_plot(self)


class HadamardGate(QubitItem):
    def __init__(self, img='assets/hadamard.png'):
        super().__init__(img)
        self.name = 'Hadamard Gate'
        self.qnum = 3
        self.matrix = H(0).get_compact_qobj()

    def mouseMoveEvent(self, event):
        self.mousePos(event)

    def mouseReleaseEvent(self, event):
        self.pen = QPen(QColor("black"))
        if len(self.collidingItems()) == 1 and self.collidingItems()[0].qnum == 1:
            self.collidingItems()[0].bloch_plot(self)

class SPhase(QubitItem):
    def __init__(self, img='assets/SPhase.png'):
        super().__init__(img)
        self.name = 'S Phase'
        self.qnum = 3
        self.matrix = S(0).get_compact_qobj()

    def mouseMoveEvent(self, event):
        self.mousePos(event)

    def mouseReleaseEvent(self, event):
        self.pen = QPen(QColor("black"))
        if len(self.collidingItems()) == 1 and self.collidingItems()[0].qnum == 1:
            self.collidingItems()[0].bloch_plot(self)


class TPhase(QubitItem):
    def __init__(self, img='assets/TPhase.png'):
        super().__init__(img)
        self.name = 'T Phase'
        self.qnum = 3
        self.matrix = T(0).get_compact_qobj()

    def mouseMoveEvent(self, event):
        self.mousePos(event)

    def mouseReleaseEvent(self, event):
        self.pen = QPen(QColor("black"))
        if len(self.collidingItems()) == 1 and self.collidingItems()[0].qnum == 1:
            self.collidingItems()[0].bloch_plot(self)

class RotationX(QubitItem):
    def __init__(self, img='assets/rotationX.png'):
        super().__init__(img)
        self.name = 'X Rotation'
        self.qnum = 3
        self.matrix = RX(0, np.pi/2).get_compact_qobj()

    def mouseMoveEvent(self, event):
        self.mousePos(event)

    def mouseReleaseEvent(self, event):
        self.pen = QPen(QColor("black"))
        if len(self.collidingItems()) == 1 and self.collidingItems()[0].qnum == 1:
            self.collidingItems()[0].bloch_plot(self)


class RotationY(QubitItem):
    def __init__(self, img='assets/rotationY.png'):
        super().__init__(img)
        self.name = 'Y Rotation'
        self.qnum = 3
        self.matrix = RY(0, np.pi/2).get_compact_qobj()


    def mouseMoveEvent(self, event):
        self.mousePos(event)

    def mouseReleaseEvent(self, event):
        self.pen = QPen(QColor("black"))
        if len(self.collidingItems()) == 1 and self.collidingItems()[0].qnum == 1:
            self.collidingItems()[0].bloch_plot(self)


class RotationZ(QubitItem):
    def __init__(self, img='assets/rotationYZpng'):
        super().__init__(img)
        self.name = 'Z Rotation'
        self.qnum = 3
        self.matrix = RZ(0, np.pi/2).get_compact_qobj()


    def mouseMoveEvent(self, event):
        self.mousePos(event)

    def mouseReleaseEvent(self, event):
        self.pen = QPen(QColor("black"))
        if len(self.collidingItems()) == 1 and self.collidingItems()[0].qnum == 1:
            self.collidingItems()[0].bloch_plot(self)
