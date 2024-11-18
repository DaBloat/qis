import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Top(QFrame):
    def __init__(self, placeholder):
        super().__init__(placeholder)
        self.width = 0 # It automatically scales in the Screen
        self.height = 50
        self.setMinimumSize(QSize(self.width, self.height))
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.setStyleSheet("background:rgb(255, 0, 255);")

 
class Bottom(QFrame):
    def __init__(self, placeholder, recipient):
        super().__init__(placeholder)
        self.scene = recipient
        self.width = 0 # It automatically scales in the Screen
        self.height = 100
        self.setMinimumSize(QSize(self.width, self.height))
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.setStyleSheet("background: rgb(170, 0, 0);")

        self.button = QPushButton(self)
        self.button.clicked.connect(self.add_item)

        
    def add_item(self):
        item = GrabCollide(50,50,40, self.scene)
        self.scene.addItem(item)

class GrabCollide(QGraphicsEllipseItem):
    def __init__(self,x,y,r, scene):
        super().__init__(0,0,r,r)
        self.name = 'NAME'
        self.scene = scene
        self.setAcceptHoverEvents(True)
        self.setPos(x,y)
        self.setBrush(Qt.red)
        # self.setFlag(QGraphicsItem.ItemIsMovable)

    def hoverEnterEvent(self, event):
        # app.instance().setOverrideCursor(Qt.OpenHandCursor)
        pass

    def hoverLeaveEvent(self, event):
        app.instance().restoreOverrideCursor()

    def mousePressEvent(self, event):
        pass

    def mouseMoveEvent(self, event):
        orig_position = event.lastScenePos()
        updated_position = event.scenePos()

        original = self.scenePos()
        updated_cursorX = updated_position.x() - orig_position.x() + original.x()
        updated_cursorY = updated_position.y() - orig_position.y() + original.y()
        self.setPos(QPointF(updated_cursorX, updated_cursorY))
        if len(self.collidingItems()) != 0:
            self.setBrush(Qt.black)
        else:
            self.setBrush(Qt.red)


    def mouseReleaseEvent(self, event):
        if len(self.collidingItems()) != 0:
            self.collidingItems()[0].setBrush(Qt.blue)
            self.scene.removeItem(self)
           


class DrawSpace(QGraphicsView):
        # Scene will be set to another class for easier access
    def __init__(self, scene):
        super().__init__()
        self.setScene(scene)
        self.setSceneRect(0,0,5500,5500)


class DrawScene(QGraphicsScene):
    def __init__(self):
        super().__init__()


class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")

        scene = DrawScene()
        draw = DrawSpace(scene)
        top = Top(self)
        bot = Bottom(self, scene)


        self.verticalLayout.addWidget(top)
        self.verticalLayout.addWidget(draw)
        self.verticalLayout.addWidget(bot)


        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())
