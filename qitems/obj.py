import sys
from mpl_toolkits.mplot3d import Axes3D
from qutip import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import *


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



if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = Try()
    main.show()
    sys.exit(app.exec_())
