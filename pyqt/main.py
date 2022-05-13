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
        
        self.port_dialog = port_dialog(self)
        self.port_dialog.exec_()

        if not self.is_connected():
            print("INSERT TRY AGAIN DIALOG HERE")
        self.show()

    def is_connected(self): #Check if connected
        return len(self.com_port) > 0
    def set_com_port(self, com):
        self.com_port = com

def main():
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui()
    app.exec_()


main()