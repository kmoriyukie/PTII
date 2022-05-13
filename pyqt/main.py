from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import (uic, QtWidgets)
import sys

from simple_menu import simple_menu
from graphs import graphs

import serial
from serial.tools import list_ports

from widgets.port_dialog import port_dialog, port_item
class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('main.ui', self)
        self.tab = self.findChild(QTabWidget)

        self.simple_menu = simple_menu()
        self.graphs = graphs()
        
        self.tab.addTab(self.simple_menu, 'Tab 1')
        self.tab.addTab(self.graphs, 'Tab 2')
        
        self.port_dialog = port_dialog()
        self.port_dialog.exec_()
        # self.serial = serial.Serial()
        # self.serial.port='COM7'
        # self.serial.open()
        # self.serial.close()
        # print(self.serial.read())
        self.show()
    def conn(self): #Check if connected
        ls = list(list_ports.comports())
        for item in ls:
            pass
        connected = True
        return connected

            

app = QtWidgets.QApplication(sys.argv)
ui = Ui()
app.exec_()
