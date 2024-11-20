from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Top(QFrame):
    def __init__(self, placeholder):
        super().__init__(placeholder)
        self.width = 0 # It automatically scales in the Screen
        self.height = 115
        self.setMinimumSize(QSize(self.width, self.height))
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.setStyleSheet("""background:rgb(255, 255, 255);
                              """)

        self.layout = QHBoxLayout(self)

        self.title = QFrame(self)
        self.title.setObjectName('title')
        self.title.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        self.title.setMinimumSize(50,0)
        self.title.setStyleSheet("""QFrame#title{background: rgb(255,255,255);
                                    border-style:solid;
                                    border-width: 2px;}""")
        self.title_layout = QVBoxLayout(self.title)
        self.text = QLabel("QIS")
        self.text.setAlignment(Qt.AlignCenter)
        self.text.setStyleSheet('font: 87 48pt "Arial Black";\ncolor: rgb(234, 196, 163);')
        self.text2 = QLabel("Quantum Interactive Space")
        self.title_layout.addWidget(self.text)
        self.title_layout.addWidget(self.text2)
        self.layout.addWidget(self.title)

        # self.button = QPushButton(self)
        # self.layout.addWidget(self.button)
