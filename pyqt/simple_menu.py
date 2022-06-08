from PyQt5 import  uic, QtWidgets
from PyQt5.QtWidgets import QWidget,QVBoxLayout, QHBoxLayout, QLabel, QGridLayout, QFrame, QGraphicsDropShadowEffect
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFontDatabase, QFont
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import seaborn as sns

# import seaborn as sb
import matplotlib as plt
tips = sns.load_dataset("tips")
# tips.info()
df = tips.copy()
# df.info()
class simple_menu(QWidget):
    def __init__(self):
        super(simple_menu, self).__init__()
        uic.loadUi('simple_menu.ui', self)


        self.touch_disp = self.findChild(QLabel, 'touch')
        self.dist_disp = self.findChild(QLabel, 'dist')
        self.layout = self.findChild(QGridLayout)
        self.graphs = self.findChild(QVBoxLayout, 'graphs')
        self.graph_frame = self.findChild(QFrame, 'frame')

        self.defineGraphs()
       
        distance = 0

        if distance > 0:
            self.dist_disp.setVisible(True)   
            self.touch_disp.setVisible(False)     
        else:
            self.dist_disp.setVisible(False)
            self.touch_disp.setVisible(True)     
        
        self.isTouching= True
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
        fontId = QFontDatabase.addApplicationFont("resources\WorkSans-VariableFont_wght.ttf")
        families = QFontDatabase.applicationFontFamilies(fontId)
        font = QFont(families[0], 20)
        self.touch_disp.setFont(font)
        self.dist_disp.setFont(font)
        # self.touch_disp.setStyleSheet('font-family: ;')
        
        # self.touch_disp.setFont('')
        if self.isTouching:
            self.touch_disp.setText("Pressure: 100g")
        else:
            self.touch_disp.setText("Pressure: -")
        
            # self.grad.setText("The object is touching!")
        gradient_style = "border-radius: 25px;\
                          background-color:"+ color +";"
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(5)
        shadow.setXOffset(0)
        shadow.setYOffset(2)
        self.grad.setStyleSheet(gradient_style)
        self.grad.setGraphicsEffect(shadow)
        self.setSensorStyle()

    def defineGraphs(self):
        self.fig = Figure(constrained_layout=True)
        self.ax1 = self.fig.add_subplot(121)
        self.ax2 = self.fig.add_subplot(122)
        self.axes=[self.ax1, self.ax2]

        self.fig.subplots_adjust(bottom=0.2, wspace=0.3, hspace=0.01)
        
        self.canvas = FigureCanvas(self.fig)

        stylesheet = "border-radius: 6px;\
                        border-color: #4c8a73; \
                        border-style:inset; \
                        border-width: 2.5px;\
                        background-color: white;"

        tips.plot(kind="scatter", x="total_bill", y="tip", 
                ax=self.axes[0], c='b', label='bla')
        
        df.plot(kind="scatter", x="smoker", y="tip", 
                ax=self.axes[1], c='m', label='bla bla')
        self.canvas.setSizePolicy(QtWidgets.QSizePolicy.Expanding, 
                                  QtWidgets.QSizePolicy.Expanding)
        self.canvas.setMinimumHeight(250)
        self.canvas.setMaximumHeight(350)
        
        self.canvas.updateGeometry()
        self.graphs.addWidget(self.canvas)

        self.graph_frame.setStyleSheet(stylesheet)
        # self.graph_frame.setGraphicsEffect(shadow)
    def setSensorStyle(self, num = None):
        sensor_style = "border-radius: 6px;\
                        border-color: #4c8a73; \
                        border-style:solid; \
                        border-width: 2.5px;\
                        background-color: #ababab;"

        

        self.sensor_box = self.findChild(QFrame, "sensors_2")
        self.sensor_box.setMinimumWidth(self.width() - 20)

        self.sensors_widget = self.findChild(QHBoxLayout, "sensors")
        self.sensors = []
        for i in range(len(self.sensors_widget)):
            self.sensors.append(self.sensors_widget.itemAt(i).widget())
        for s in self.sensors:
            shadow = QGraphicsDropShadowEffect()
            shadow.setBlurRadius(5)
            shadow.setXOffset(0)
            shadow.setYOffset(2)
            
            s.setStyleSheet(sensor_style) 
            s.setGraphicsEffect(shadow)
        

# border-radius: 10px;\nbackground-color: #8385f7;
# border-radius: 10px;\nbackground-color: #53c2af; padding: 2px;