from PyQt5 import  uic, QtWidgets
from PyQt5.QtWidgets import QWidget,QHBoxLayout, QLabel, QGridLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import seaborn as sns

# import seaborn as sb
import matplotlib as plt
tips = sns.load_dataset("tips")
tips.info()
df = tips.smoker
df.info()
class simple_menu(QWidget):
    def __init__(self):
        super(simple_menu, self).__init__()
        uic.loadUi('simple_menu.ui', self)

        sensor_style = "border-radius: 5px;\
                        border-color: #4c8a73; \
                        border-style:solid; \
                        border-width: 2px;\
                        background-color: #ababab;"


        self.touch_disp = self.findChild(QLabel, 'touch')
        self.dist_disp = self.findChild(QLabel, 'dist')
        self.layout = self.findChild(QGridLayout)
        
        self.fig = Figure()
        self.ax1 = self.fig.add_subplot(121)
        self.ax2 = self.fig.add_subplot(122, sharex=self.ax1, sharey=self.ax1)
        self.axes=[self.ax1, self.ax2]
        self.canvas = FigureCanvas(self.fig)
        

        tips.plot(kind="scatter", x="total_bill", y="tip", 
                ax=self.axes[0], c='b', label='bla')
        self.canvas.setSizePolicy(QtWidgets.QSizePolicy.Expanding, 
                                  QtWidgets.QSizePolicy.Expanding)
        self.canvas.setMinimumHeight(300)
        self.canvas.updateGeometry()
        self.layout.addWidget(self.canvas)

        distance = 0

        if distance > 0:
            self.dist_disp.setVisible(True)   
            self.touch_disp.setVisible(False)     
        else:
            self.dist_disp.setVisible(False)
            self.touch_disp.setVisible(True)     
        
        self.isTouching= False
        self.dist_disp.setText("Distance: "+str(distance)+" cm")
        if distance >= 1: # green
            color = "#00ff00"
        elif distance > 0.7: #yellow
            color = "#ffff00"
        elif distance > 0.3: #orange
            color = "#fc7f00"
        else: # red
            color = "#ff0000"
            self.isTouching = True

        if self.isTouching:
            self.touch_disp.setText("Pressure: 100g")
        else:
            self.touch_disp.setText("Pressure: -")
        
            # self.grad.setText("The object is touching!")
        gradient_style = "border-radius: 25px;\
                          background-color:"+ color +";"
        self.grad.setStyleSheet(gradient_style)

        
        self.sensors_widget = self.findChild(QHBoxLayout, "sensors")
        self.sensors = []
        for i in range(len(self.sensors_widget)):
            self.sensors.append(self.sensors_widget.itemAt(i).widget())

        for s in self.sensors:
            s.setStyleSheet(sensor_style) 


# border-radius: 10px;\nbackground-color: #8385f7;
# border-radius: 10px;\nbackground-color: #53c2af; padding: 2px;