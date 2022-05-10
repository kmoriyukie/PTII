from PyQt5 import  uic
from PyQt5.QtWidgets import QWidget
class simple_menu(QWidget):
    def __init__(self):
        super(simple_menu, self).__init__()
        uic.loadUi('simple_menu.ui', self)