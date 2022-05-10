from PyQt5 import uic
from PyQt5.QtWidgets import QWidget

class graphs(QWidget):
    def __init__(self):
        super(graphs, self).__init__()
        uic.loadUi('graphs.ui', self)