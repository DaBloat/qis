from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Workspace(QGraphicsView):
        # Scene will be set to another class for easier access
    def __init__(self, scene):
        super().__init__()
        self.setScene(scene)
        self.setSceneRect(0,0,5500,5500)


class WorkspaceScene(QGraphicsScene):
    def __init__(self):
        super().__init__()
