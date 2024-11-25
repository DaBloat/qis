from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class TitleCard(QFrame):
    def __init__(self, placeholder, title, description):
        super().__init__(placeholder)
        self.setObjectName('titleCard')
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        self.setMinimumSize(150,0)
        self.setStyleSheet("""QFrame#titleCard{background: rgb(255,255,255);
                                    border-style:solid;
                                    border-width: 2px;}""")

        self.title_layout = QVBoxLayout(self)
        self.title = QLabel(title)
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setStyleSheet('font: 87 48pt "Arial Black";')


        self.description = QLabel(description)
        self.description.setStyleSheet('font-size: 7.5pt')
        self.description.setAlignment(Qt.AlignCenter)
        
        for labels in [self.title, self.description]:
            self.title_layout.addWidget(labels)

class Button(QPushButton):
    def __init__(self, placeholder, text):
        super().__init__(placeholder)
        self.setText(text)

class ScrollArea(QScrollArea):
    def __init__(self, placeholder, recipient, vertOpt, horiOpt):
        super().__init__(placeholder)
        self.opt = {'AlwaysOn':Qt.ScrollBarAlwaysOn, 
                    "AlwaysOff":Qt.ScrollBarAlwaysOff}
        self.setVerticalScrollBarPolicy(self.opt[vertOpt])
        self.setHorizontalScrollBarPolicy(self.opt[horiOpt])

class HistoryBlock(QFrame):
    def __init__(self, placeholder):
        super().__init__(placeholder)
        self.setObjectName('history')
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        self.setMinimumSize(250, 0)

class OutputMatrix(QFrame):
    def __init__(self, placeholder):
        super().__init__(placeholder)
        self.setObjectName('output_matrix')
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        self.setMinimumSize(250, 0)


        
