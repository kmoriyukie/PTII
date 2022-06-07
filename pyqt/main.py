from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import (uic, QtWidgets)
import sys

from simple_menu import simple_menu
from graphs import graphs

import serial

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
        # self.port_dialog.exec_()

        # if not self.is_connected():
        #     print("INSERT TRY AGAIN DIALOG HERE")
        
        # self.serial = serial.Serial(port=self.com_port, baudrate=115200)
        # print("connected to: " + self.serial.portstr)
        
        # # self.simple_menu.dist_disp.setText(self.read_com())
        # print(self.read_com())
        self.show()
        # self.serial.close()

    def is_connected(self): #Check if connected
        return len(self.com_port) > 0
    def set_com_port(self, com):
        self.com_port = com
    def read_com(self):
        seq = []
        count = 1
        while True:
            for c in self.serial.read():
                seq.append(chr(c)) #convert from ANSII
                joined_seq = ''.join(str(v) for v in seq) #Make a string from array

                if chr(c) == '\n':
                    return joined_seq
def main():
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui()
    app.exec_()

main()