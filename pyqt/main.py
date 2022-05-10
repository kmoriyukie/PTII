from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import (uic, QtWidgets)
import sys

from simple_menu import simple_menu
from graphs import graphs
class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('main.ui', self)
        self.tab = self.findChild(QTabWidget)
        self.tab.addTab(simple_menu(), 'Tab 1')
        self.tab.addTab(graphs(), 'Tab 2')
        self.show()
    def connect(self): #Check if connected
        connected = True
        return connected

            

app = QtWidgets.QApplication(sys.argv)
ui = Ui()
app.exec_()
