from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from utils.widgets import *
from utils.layouts import *


class Bottom(QFrame):
    def __init__(self, placeholder, recipient):
        super().__init__(placeholder)
        self.scene = recipient
        self.width = 0 # It automatically scales in the Screen
        self.height = 130
        self.setObjectName("bottomFrame")
        self.setMinimumSize(QSize(self.width, self.height))
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.setStyleSheet("QFrame#bottomFrame{background:rgb(234, 196, 163);}")

        self.layout = HorizontalOrganizer(self)

        self.vertlayout = VerticalOrganizer(self)
        
        self.button1 = Button(self, 'qubit')
        self.button2 = Button(self, 'operators')
        self.button3 = Button(self, 'functions')
        self.button4 = Button(self, 'gates')



        self.scrollarea = ScrollArea(self, self.scene, "AlwaysOff", "AlwaysOn")
       

        self.history = HistoryBlock(self)
        # self.history.setStyleSheet("""QFrame#history{background: rgb(255,255,255);
        #                            border-style:solid;
        #                            border-width: 2px;}""")

        

        self.output_matr = OutputMatrix(self)
        #self.output_matr.setStyleSheet("""QFrame#outMatrix{background: rgb(255,255,255);
        #                            border-style:solid;
        #                            border-width: 2px;}""")
        
        for i in [self.button1,self.button2, self.button3, self.button4]:
            self.vertlayout.add(i)

        self.layout.add(self.vertlayout)
        self.layout.add(self.scrollarea)
        self.layout.add(self.history)
        self.layout.add(self.output_matr)
