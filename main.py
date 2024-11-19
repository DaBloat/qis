import sys
from PyQt5.QtWidgets import *
from interfaces import top, bot, workspace


class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")

        scene = workspace.WorkspaceScene()
        work = workspace.Workspace(scene)
        menutop = top.Top(self)
        menubot = bot.Bottom(self, scene)

        self.verticalLayout.addWidget(menutop)
        self.verticalLayout.addWidget(work)
        self.verticalLayout.addWidget(menubot)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())
