from PyQt5 import  uic, QtWidgets
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QGridLayout, QFrame, QGraphicsDropShadowEffect   
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFontDatabase, QFont, QPixmap
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import seaborn as sns

import time

# import seaborn as sb
import matplotlib as plt
tips = sns.load_dataset("penguins")
# tips.info()
df = tips.copy()
# df.info()

class sensor_info():
    def __init__(self, number, title, body, frame, parent):
        self.number = number
        self.title = title
        self.body = body
        self.frame = frame
        self.parent = parent

        self.isBeingTouched = self.checkStatus()

        fontId = QFontDatabase.addApplicationFont("resources\WorkSans-VariableFont_wght.ttf")
        families = QFontDatabase.applicationFontFamilies(fontId)
        font = QFont(families[0], 14, weight = 0)
        font.setUnderline(True)
        self.title.setFont(font)
        
        self.body.setFont(QFont(families[0], 12))

    def checkStatus(self): # UPDATE SENSOR STATUS, REMOVE HARD CODED STUFF
        if self.number == 1:
            self.distance = 0
            self.pressure = 100
        if self.number == 2:
            self.distance = 0.1
            self.pressure = 0
        if self.number == 3:
            self.distance = 0.2
            self.pressure = 0
        if self.number == 4:
            self.distance = 0.3
            self.pressure = 0
        
        return True
    def setStyleSheet(self):
        if self.pressure < 10:
            self.frame.setStyleSheet("border-radius: 20px; \
                                      background-color: #9EB3C2;")
        else:
            self.frame.setStyleSheet("border-radius: 20px; \
                                      background-color: #FF6047;")
        
        self.frame.setGraphicsEffect(self.parent.newShadowObject(xoff=-0.5, radius=5))

    def setText(self):
        self.title.setText('Sensor ' + str(self.number))
        if self.pressure > 0: self.body.setText('Pressure: ' + str(self.pressure) + 'g')
        else: self.body.setText('Distance: ' + str(self.distance) + 'm')
        
    def update(self, d, p):
        self.distance = d
        self.pressure = p
        self.setText()
        self.setStyleSheet()




class simple_menu(QWidget):
    def __init__(self, parent = None):
        super(simple_menu, self).__init__()
        uic.loadUi('simple_menu.ui', self)
        # self.setParent(parent)
        self.setStyleSheet("background-color: #F7F7FF;")

        self.defineChildren()
        
        self.distance = 0
        self.isTouching= True
        self.whichGraphToDisplay = 'distance'
        self.time = time.time()
        self.graphindex = []
        self.distanceHistory = []
        self.pressureHistory = []

        fontId = QFontDatabase.addApplicationFont("resources\WorkSans-VariableFont_wght.ttf")
        families = QFontDatabase.applicationFontFamilies(fontId)
        self.fontFamily = QFont(families[0], 18)
        self.fontFamily2 = QFont(families[0], 14)
        self.fontFamilySmall = QFont(families[0], 12)
        
        self.touch_disp.setFont(self.fontFamily)
        self.dist_disp.setFont(self.fontFamily)
        self.pressure = 100
        self.distance = 10
        self.updateWidgets()
        self.updateGraphsDisp()
        self.setGradBar()
        self.setSensorStyle(2)
        self.setupInfoBoxes()
        self.drawButtons()
    
    def defineChildren(self):
        self.touch_disp = self.findChild(QLabel, 'touch')
        self.dist_disp = self.findChild(QLabel, 'dist')
        self.layout = self.findChild(QGridLayout)
        self.graphs = self.findChild(QVBoxLayout, 'graphs')
        self.graph_frame = self.findChild(QFrame, 'frame')
        self.fig = Figure()

        self.buttons = []
        self.sensorInfoList = []
        
        self.sensorInfoDispList = []

        for b in range(3):
            self.buttons.append(self.findChild(QLabel, 'button' + str(b + 1)))
        for s in range(4): 
            self.sensorInfoList.append(sensor_info(s + 1, 
                                                   self.findChild(QLabel, 'sensor' + str(s + 1) + '_title'), 
                                                   self.findChild(QLabel, 'sensor' + str(s + 1) + '_body'),
                                                   self.findChild(QFrame, 'sensor_' + str(s + 1)),
                                                   self))

    def drawButtons(self):
        self.button_width = self.buttons[0].width() - 10
        self.button_height = self.buttons[0].height() - 10
        img4 = QPixmap('resources\\plus.png')
        img3 = QPixmap('resources\menu.png')
        img2 = QPixmap('resources\\resilience.png')
        img = QPixmap('resources\\height.png')
        
        style = "background-color: #BDD5EA; \
                 padding: 5px; \
                 border-radius: 10px;"

        self.buttons[0].setPixmap(img.scaled(self.button_width, self.button_height, Qt.KeepAspectRatio))
        self.buttons[1].setPixmap(img2.scaledToHeight(self.button_height))
        self.buttons[2].setPixmap(img3.scaledToHeight(self.button_height))
        for n, b in enumerate(self.buttons):
            shadow = self.newShadowObject(radius=5, xoff=1)
            b.setGraphicsEffect(shadow)
            b.setStyleSheet(style)
            b.mousePressEvent = lambda state, n = n: self.buttonClicked(n)
    def setupInfoBoxes(self):
        for s in self.sensorInfoList:
            s.setStyleSheet()
            s.setText()
            
    def buttonClicked(self, n):
        if n == 0:   self.whichGraphToDisplay = 'distance'
        elif n == 1: self.whichGraphToDisplay = 'pressure'
        elif n == 2: self.whichGraphToDisplay = 'all'
        
        if n != 3: self.updateGraphsDisp()

    def setGradBar(self):
        self.dist_disp.setText("Distance: "+str(self.distance)+" cm")
        if self.distance >= 8: # green
            color = "#00ff00"
        elif self.distance >= 45: #yellow
            color = "#ffff00"
        elif self.distance >= 20: #orange
            color = "#fc7f00"
        else: # red
            color = "#ff0000"
            self.isTouching = True
        self.grad.setMaximumWidth((100 - self.distance)*(self.width()))
        
        gradient_style = "border-radius: 25px;\
                          background-color:"+ color +";"
        shadow = self.newShadowObject(radius=10, xoff=2)
        self.grad.setStyleSheet(gradient_style)
        self.grad.setGraphicsEffect(shadow)

    def updateGraphsDisp(self):
        self.fig.clf()
        self.fig.subplots_adjust(bottom=0.15, wspace=0.3, hspace=0.01)
        if self.whichGraphToDisplay == 'all':
            self.ax1 = self.fig.add_subplot(211)
            self.ax2 = self.fig.add_subplot(212, sharex = self.ax1)
            self.ax1.grid(True)
            self.ax2.grid(True)    

            self.ax2.set_xlabel("Time (s)")
            self.ax1.set_ylabel("Distance (cm)")

            self.ax2.set_ylabel("Pressure (g)")
            
            self.fig.subplots_adjust(bottom=0.15, wspace=0.3, hspace=0.3)

        elif self.whichGraphToDisplay == 'distance' or self.whichGraphToDisplay == 'pressure':
            self.ax = self.fig.add_subplot(111)
            if self.whichGraphToDisplay == 'distance': self.ax.set_ylabel(self.whichGraphToDisplay.capitalize() + " (cm)")
            else: self.ax.set_ylabel(self.whichGraphToDisplay.capitalize() + " (g)")
            self.ax.set_xlabel("Time (s)")
            self.ax.grid(True)
        
        self.canvas_stylesheet = "border-radius: 6px;\
                                  border-color: #2E294E; \
                                  border-style:inset; \
                                  border-width: 2.5px;\
                                  background-color: white;"

        self.canvas = FigureCanvas(self.fig)
        self.canvas.setSizePolicy(QtWidgets.QSizePolicy.Expanding, 
                                  QtWidgets.QSizePolicy.Expanding)
        self.canvas.setMinimumHeight(250)
        self.canvas.setMaximumHeight(350)
        
        self.canvas.updateGeometry()
        for i in reversed(range(self.graphs.count())): 
            self.graphs.itemAt(i).widget().setParent(None)
        self.graphs.addWidget(self.canvas)
        self.updateGraphs()
        self.graph_frame.setStyleSheet(self.canvas_stylesheet)

    def clearGraphs(self):
        if self.whichGraphToDisplay == 'all':
            self.ax1.clear()
            self.ax2.clear()
        else: 
            self.ax.clear()
        
    def updateGraphs(self):
        if self.whichGraphToDisplay == 'all':
            self.ax1.plot(self.graphindex, self.distanceHistory, '-b')
            self.ax2.plot(self.graphindex, self.pressureHistory, '-m')
        else:
            if self.whichGraphToDisplay == 'distance':
                self.ax.plot(self.graphindex, self.distanceHistory)
            else:
                self.ax.plot(self.graphindex,self.pressureHistory)
            

    def setSensorStyle(self, num = None):
        
        sensor_style = "border-radius: 5px;\
                        border-color: #495867; \
                        border-style:solid; \
                        border-width: 2.5px;\
                        background-color: #495867;"

        sensor_style_2 = "border-radius: 5px;\
                        border-color: #FE5F55; \
                        border-style:solid; \
                        border-width: 2.5px;\
                        background-color: #FE5F55;"
        

        self.sensor_box = self.findChild(QFrame, "sensors_2")
        self.sensor_box.setMinimumWidth(self.width() - 20)

        self.sensors_widget = self.findChild(QHBoxLayout, "sensors")
        self.sensors = []
        for i in range(len(self.sensors_widget)):
            self.sensors.append(self.sensors_widget.itemAt(i).widget())
        for s in self.sensors:
            shadow = self.newShadowObject()
            
            if s.objectName() == 'disp_sensor' + str(num):
                s.setStyleSheet(sensor_style_2)
            else:
                s.setStyleSheet(sensor_style) 
            s.setGraphicsEffect(shadow)

    def newShadowObject(self, radius=1, xoff = -0.5, yoff = 2):
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(radius)
        shadow.setXOffset(xoff)
        shadow.setYOffset(yoff)
        return shadow
    
    def updateWidgets(self):
        if self.distance > 0:
            self.dist_disp.setVisible(True)   
            self.touch_disp.setVisible(False)     
        else:
            self.dist_disp.setVisible(False)
            self.touch_disp.setVisible(True)     

        self.touch_disp.setText("Pressure: " + str(self.pressure) + 'g')
        self.dist_disp.setText('Distance: ' + str(self.distance) + 'm')

    def update(self, string):
        string = string.split('\n')[0]
        infolist = string.split('..') # Separa a informação dos sensores
        print(infolist)
        for i in infolist:
            aux = i.split(',')
            if len(aux) > 0:
                self.sensorInfoList[int(aux[0])].update(int(aux[1]), int(aux[2]))

        
        self.distance, self.pressure = self.getMeanValues()
        if len(self.pressureHistory) >= 100:
            self.distanceHistory.remove(self.distanceHistory[0])
            self.pressureHistory.remove(self.pressureHistory[0])
            self.graphindex.remove(self.graphindex[0])    
        
        self.graphindex.append(-self.time + time.time())

        self.distanceHistory.append(self.distance)
        self.pressureHistory.append(self.pressure)

        self.updateWidgets()
        self.updateGraphsDisp()
        
        self.setGradBar()

    def getMeanValues(self):
        mp = 0
        md = 0
        for s in self.sensorInfoList:
            mp += s.pressure
            md += s.distance
        
        mp /= len(self.sensorInfoList)
        md /= len(self.sensorInfoList)
        return mp, md