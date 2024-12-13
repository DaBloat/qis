
import sys
from mpl_toolkits.mplot3d import Axes3D
from qutip import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from interfaces.workspace import *
from utils.layouts import *


class Try(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QHBoxLayout(self)
        self.figure = plt.figure(constrained_layout = True)
        self.scene = FigureCanvas(self.figure)
        self.ax = self.figure.add_subplot(111, projection='3d')
        self.b = Bloch(fig=self.figure, axes=self.ax)
        self.b.render()
        self.layout.addWidget(self.scene)
        self.scene.draw()
        plt.imsave('try.png', self.b)

class Try2(QWidget):
    def __init__(self):
        super().__init__()
        self.b = Bloch(figsize=[4,4])
        self.b.font_size = 12
        print(self.b)
        self.b.save('assets/trial.png')
        self.pix = QPixmap('assets/trial.png')
        self.item = QGraphicsPixmapItem()
        self.item.setPixmap(self.pix)
        scene = WorkspaceScene()
        work = Workspace(scene)
        scene.addItem(self.item)
        self.verticalLayout = VerticalOrganizer(self)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.add(work)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = Try2()
    main.show()
    sys.exit(app.exec_())
