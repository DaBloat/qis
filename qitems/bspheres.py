from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class BlochSphere(QGraphicsPixmapItem):
    def __init__(self):
        super().__init__()
        self.name = "BlochSphere"
        self.pix = QPixmap('assets/bloch_sphere.png')
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

    def hoverEnterEvent(self, event):
        pass
        
    def hoverLeaveEvent(self, event):
        pass

    def mousePressEvent(self, event):
        pass

    def mouseMoveEvent(self, event):
        orig_position = event.lastScenePos()
        updated_position = event.scenePos()
        original = self.scenePos()
        updated_cursorX = updated_position.x() - orig_position.x() + original.x()
        updated_cursorY = updated_position.y() - orig_position.y() + original.y()
        self.setPos(QPointF(updated_cursorX, updated_cursorY))
        """
        if len(self.collidingItems()) != 0:
            self.setBrush(Qt.black)
        else:
            self.setBrush(Qt.red)
        """
    def mouseReleaseEvent(self, event):
        pass
        """
        if len(self.collidingItems()) != 0:
            self.collidingItems()[0].setBrush(Qt.blue)
            self.scene.removeItem(self)
        """

class BlochButton(QToolButton):
    def __init__(self, placeholder, scene,x=100,y=75):
        super().__init__(placeholder)
        self.scene = scene
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.setFixedSize(x, y)
        self.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.icon = QIcon('assets/bloch_sphere.png')
        self.setIconSize(QSize(50,50))
        self.setIcon(self.icon)
        self.setText('Bloch Sphere')
        self.clicked.connect(self.addBlochToTheScene)

    def addBlochToTheScene(self):
        print("Just to know it works")
        self.b = BlochSphere()
        self.scene.addItem(self.b)
