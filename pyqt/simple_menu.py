from PyQt5 import  uic
from PyQt5.QtWidgets import QWidget,QHBoxLayout, QLabel
class simple_menu(QWidget):
    def __init__(self):
        super(simple_menu, self).__init__()
        uic.loadUi('simple_menu.ui', self)

        sensor_style = "border-radius: 10px;\
                        border-color: #53c2af; \
                         border-style:double; \
                        border-width: 2px;"
                        # background-color: #bdbeff;"


        self.touch_disp = self.findChild(QLabel, 'touch')
        self.dist_disp = self.findChild(QLabel, 'dist')
        
        
        self.touch_disp.setText("I detected 100g of pressure!")
                
        distance = -1

        if distance > 0:
            self.dist_disp.setVisible(True)   
            self.touch_disp.setVisible(False)     
        else:
            self.dist_disp.setVisible(False)
            self.touch_disp.setVisible(True)     
        
        
        self.dist_disp.setText("The object is "+str(distance)+" cm away!")
        if distance >= 1: # green
            color = "#00ff00"
        elif distance > 0.7: #yellow
            color = "#ffff00"
        elif distance > 0.3: #orange
            color = "#fc7f00"
        else: # red
            color = "#ff0000"
            # self.grad.setText("The object is touching!")
        gradient_style = "border-radius: 10px;\
                          background-color:"+ color +";"
        self.grad.setStyleSheet(gradient_style)

        
        self.sensors_widget = self.findChild(QHBoxLayout, "sensors")
        self.sensors = []
        for i in range(len(self.sensors_widget)):
            self.sensors.append(self.sensors_widget.itemAt(i).widget())

        for s in self.sensors:
            s.setStyleSheet(sensor_style) 