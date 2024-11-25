from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from utils.layouts import *
from utils.widgets import *

class Top(QFrame):
    def __init__(self, placeholder, recipient):
        super().__init__(placeholder)
        self.scene = recipient 
        self.setObjectName('topFrame')
        self.width = 0 # It automatically scales in the Screen
        self.height = 115
        self.setMinimumSize(QSize(self.width, self.height))
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.setStyleSheet("""QFrame#topFrame{background:rgb(234, 196, 163);}
                              """)

        self.layout = HorizontalOrganizer(self)

        self.title = TitleCard(self, 'QIS', 'Quantum Interactive Space')

        self.horSpacer = Spacers(50,0)
        
        self.button1 = Button(self, 'New')
        self.button2 = Button(self, 'Open')
        self.button3 = Button(self, 'Save')
        self.button4 = Button(self, 'Undo')
        self.button5 = Button(self, 'Redo')
        self.button6 = Button(self, 'Select')
        self.button7 = Button(self, 'Delete')
        self.button8 = Button(self, 'Add Notes')
        self.button9 = Button(self, 'Draw Arrow')

        self.howtobutton = Button(self, '?')
        self.documentation = Button(self, 'documentation')
        self.github = Button(self, 'Github')
        self.email = Button(self, 'Email')

            
        self.stack_buttons1 = StackOrganizer(self)
        self.stack_buttons1.stack(top=[self.button1, self.button2, self.button3, self.button4, self.button5],
                                 bottom=[self.button6, self.button7, self.button8, self.button9])
        self.stack_buttons2 = StackOrganizer(self)
        self.stack_buttons2.stack(top=[self.howtobutton,self.documentation], bottom=[self.github, self.email])
        
        for items in [self.title, self.horSpacer, self.stack_buttons1, self.horSpacer, self.stack_buttons2]:
            self.layout.add(items)
