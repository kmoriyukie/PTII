from PyQt5 import  uic
from PyQt5.QtWidgets import QWidget,QHBoxLayout
class simple_menu(QWidget):
    def __init__(self):
        super(simple_menu, self).__init__()
        uic.loadUi('simple_menu.ui', self)

        sensor_style = "border-radius: 10px;\
                        background-color: #bdbeff"

        self.sensors_widget = self.findChild(QHBoxLayout)
        # print(len(self.sensors))
        self.sensors = []
        for i in range(len(self.sensors_widget)):
            self.sensors.append(self.sensors_widget.itemAt(i).widget())

        for s in self.sensors:
            s.setStyleSheet(sensor_style) 