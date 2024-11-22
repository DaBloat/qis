import sys
from PyQt5.QtWidgets import *
from interfaces.top import Top
from interfaces.bot import Bottom
from interfaces.workspace import *


class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")

        scene = WorkspaceScene()
        work = Workspace(scene)
        menutop = Top(self)
        menubot = Bottom(self, scene)

        self.verticalLayout.addWidget(menutop)
        self.verticalLayout.addWidget(work)
        self.verticalLayout.addWidget(menubot)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())
