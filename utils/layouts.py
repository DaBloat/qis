from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Spacers(QSpacerItem):
    def __init__(self, x, y, policy=QSizePolicy.Fixed):
        super().__init__(x, y, policy)

class StackOrganizer(QVBoxLayout):
    def __init__(self, placeholder):
        super().__init__(placeholder)
        self.top = HorizontalOrganizer(placeholder)
        self.bottom = HorizontalOrganizer(placeholder)
        self.addItem(self.top)
        self.addItem(self.bottom)

    def stack(self,top,bottom):
        for widget in top:
            self.top.add(widget)

        for widget in bottom:
            self.bottom.add(widget)

class VerticalOrganizer(QVBoxLayout):
    def __init__(self, placeholder):
        super().__init__(placeholder)

    def stretch(self):
        self.addStretch()


    def add(self, item):
        try:
            self.addWidget(item)
        except TypeError:
            self.addItem(item)



class HorizontalOrganizer(QHBoxLayout):
    def __init__(self, placeholder):
        super().__init__(placeholder)
    
    def stretch(self):
        self.addStretch()

    def add(self, item):
        try:
            self.addWidget(item)
        except TypeError:
            self.addItem(item)
        

