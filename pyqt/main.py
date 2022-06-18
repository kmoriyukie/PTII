from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import (uic, QtWidgets, QtCore)
import sys

from simple_menu import simple_menu
from graphs import graphs

import serial

from widgets.port_dialog import port_dialog, port_item
class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        # uic.loadUi('main.ui', self)
        # self.tab = self.findChild(QTabWidget)

        self.simple_menu = simple_menu(self)
        self.graphs = graphs()
        self.setMinimumHeight(self.simple_menu.height())
        self.setMinimumWidth(self.simple_menu.width())

        
        self.port_dialog = port_dialog(self)
        self.port_dialog.exec_()

        if not self.is_connected():
            print("INSERT TRY AGAIN DIALOG HERE")
        
        self.serial = serial.Serial(port=self.com_port, baudrate=115200)
        print("connected to: " + self.serial.portstr)
        
        self.timer = QtCore.QTimer(self)
        self.timer.setInterval(100)
        self.timer.start()
        self.timer.timeout.connect(self.read_com)

        # # self.simple_menu.dist_disp.setText(self.read_com())
        print(self.read_com())
        self.setCentralWidget(self.simple_menu)
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
                    self.simple_menu.update(joined_seq)
                    return joined_seq


def main():
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui()
    app.exec_()

main()