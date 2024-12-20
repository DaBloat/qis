import sys
from PyQt5.QtWidgets import *
from utils.layouts import *
from interfaces.top import Top
from interfaces.bot import Bottom
from interfaces.workspace import *


class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.verticalLayout = VerticalOrganizer(self)
        self.verticalLayout.setObjectName("verticalLayout")

        scene = WorkspaceScene()
        work = Workspace(scene)
        menutop = Top(self, scene)
        menubot = Bottom(self, scene)

        for part in [menutop, work, menubot]:
            self.verticalLayout.add(part)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())
