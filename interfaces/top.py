from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Top(QFrame):
    def __init__(self, placeholder):
        super().__init__(placeholder)
        self.setObjectName('topFrame')
        self.width = 0 # It automatically scales in the Screen
        self.height = 115
        self.setMinimumSize(QSize(self.width, self.height))
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.setStyleSheet("""QFrame#topFrame{background:rgb(234, 196, 163);}
                              """)

        self.layout = QHBoxLayout(self)

        self.title = QFrame(self)
        self.title.setObjectName('title')
        self.title.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        self.title.setMinimumSize(150,0)
        self.title.setStyleSheet("""QFrame#title{background: rgb(255,255,255);
                                    border-style:solid;
                                    border-width: 2px;}""")
        self.title_layout = QVBoxLayout(self.title)
        self.text = QLabel("QIS")
        self.text.setAlignment(Qt.AlignCenter)
        self.text.setStyleSheet('font: 87 48pt "Arial Black";')
        self.text2 = QLabel("Quantum Interactive Space")
        self.text2.setStyleSheet('font-size: 7.5pt')
        self.text2.setAlignment(Qt.AlignCenter)
        self.title_layout.addWidget(self.text)
        self.title_layout.addWidget(self.text2)
        self.layout.addWidget(self.title)

        self.horizontalSpacer = QSpacerItem(50, 0, QSizePolicy.Fixed)
        self.layout.addItem(self.horizontalSpacer)
        self.vertlayout = QVBoxLayout(self)
        self.layout.addLayout(self.vertlayout)
         
        self.flayerbutton = QHBoxLayout(self)
        self.vertlayout.addLayout(self.flayerbutton)

        self.slayerbutton = QHBoxLayout(self)
        self.vertlayout.addLayout(self.slayerbutton)

        self.button1 = QPushButton('Sample 1')
        self.flayerbutton.addWidget(self.button1)
        self.button2 = QPushButton('Sample 2')
        self.flayerbutton.addWidget(self.button2)
        self.button3 = QPushButton('Sample 3')
        self.flayerbutton.addWidget(self.button3)
        self.button4 = QPushButton('Sample 4')
        self.flayerbutton.addWidget(self.button4)
        
        self.button5 = QPushButton('Sample 5')
        self.flayerbutton.addWidget(self.button5)
        self.button6 = QPushButton('Sample 6')
        self.slayerbutton.addWidget(self.button6)
        self.button7 = QPushButton('Sample 7')
        self.slayerbutton.addWidget(self.button7)
        self.button8 = QPushButton('Sample 8')
        self.slayerbutton.addWidget(self.button8)


        self.horizontalSpacer2 = QSpacerItem(50, 0, QSizePolicy.Fixed)
        self.layout.addItem(self.horizontalSpacer2)
        self.vertlayout2 = QVBoxLayout(self)
        self.layout.addLayout(self.vertlayout2)
         
        self.howtolayerbutton = QHBoxLayout(self)
        self.vertlayout2.addLayout(self. howtolayerbutton)

        self.reachlayerbutton = QHBoxLayout(self)
        self.vertlayout2.addLayout(self.reachlayerbutton)
        self.buttontry = QPushButton('?')
        self.howtolayerbutton.addWidget(self.buttontry)
        self.documentation = QPushButton('documentation')
        self.howtolayerbutton.addWidget(self.documentation)

        self.email = QPushButton('email')
        self.reachlayerbutton.addWidget(self.email)
        self.github = QPushButton('github')
        self.reachlayerbutton.addWidget(self.github)

