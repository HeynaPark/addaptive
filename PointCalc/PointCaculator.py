import sys
from xml.etree.ElementTree import tostring
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import QImage, QPainter, QPen, QPixmap, QColor, QBrush, QPainterPath
from PyQt5.QtWidgets import QPushButton, QSizePolicy
from PyQt5.QtWidgets import QFileDialog, QGraphicsView, QGraphicsScene
from PyQt5.QtCore import QRectF, Qt, QLineF, QPointF
from PyQt5 import QtGui



fileName=None
load = None
px = None
form_class = uic.loadUiType("mainwindow.ui")[0]


#############################
#  Main Window              #
#############################

class MyWindow(QMainWindow, form_class):
    
    pixmap =None

    def __init__(self):
        super().__init__()
        self.chosen_points = []
        QMainWindow().__init__(self)
        self.setupUi(self)
        self.showMaximized()
        filename = None

        self.view = View(self)
        self.view.setUI(self.label_mouse)
        self.view.setUI_com(self.comboBox)
        self.view.setUI_x1(self.lineEdit_x1)
        self.view.setUI_x2(self.lineEdit_x2)
        self.view.setUI_x3(self.lineEdit_x3)
        self.view.setUI_x4(self.lineEdit_x4)
        self.view.setUI_y1(self.lineEdit_y1)
        self.view.setUI_y2(self.lineEdit_y2)
        self.view.setUI_y3(self.lineEdit_y3)
        self.view.setUI_y4(self.lineEdit_y4)
        self.horizontalLayout_5.addWidget(self.view)

        
        for i in range(1,5):
            lineEdit_x = self.findChild(QLineEdit, "lineEdit_x"+str(i)).setText("300.45")
            lineEdit_ax = self.findChild(QLineEdit, "lineEdit_ax"+str(i)).setText("303.3")
            lineEdit_y = self.findChild(QLineEdit, "lineEdit_y"+str(i)).setText("605.7")
            lineEdit_ay = self.findChild(QLineEdit, "lineEdit_ay"+str(i)).setText("604.54")
            lineEdit_x
            lineEdit_ax
            lineEdit_y
            lineEdit_ay
        
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(4)
        self.tableWidget.setHorizontalHeaderLabels(["Point x","Point y","X Error","Y Error","Deviation (σ)"])
        self.actionOpen_O.triggered.connect(self.open)


        self.lineEdit_x1.textChanged[str].connect(self.TableSetting_x1)
        self.lineEdit_x2.textChanged[str].connect(self.TableSetting_x2)
        self.lineEdit_x3.textChanged[str].connect(self.TableSetting_x3)
        self.lineEdit_x4.textChanged[str].connect(self.TableSetting_x4)
        self.lineEdit_y1.textChanged[str].connect(self.TableSetting_y1)
        self.lineEdit_y2.textChanged[str].connect(self.TableSetting_y2)
        self.lineEdit_y3.textChanged[str].connect(self.TableSetting_y3)
        self.lineEdit_y4.textChanged[str].connect(self.TableSetting_y4)
        
        self.pushButton.clicked.connect(self.calculate)
        self.pushButton_add.clicked.connect(self.addPoint)
        self.pushButton_clear.clicked.connect(self.view.clear)
        
       
        

    def open(self):
        fileName, _ = QFileDialog.getOpenFileName(self,
                            "Open Image File",'.',"Images (*.png *.xpm *.jpg)") 
        self.filename = fileName
        if fileName != "":
            self.view.load(fileName)
        if fileName:
            self.pixmap = QPixmap(fileName)
        width = int(self.view.width())
        self.label_5.setNum(width)
        self.label_5.adjustSize()
        height = int(self.view.height())
        self.label_6.setNum(height)
        self.label_6.adjustSize()
        wid = int(self.pixmap.width())
        hei = int(self.pixmap.height())
        self.label_8.setText(str(wid)+" X "+str(hei))

    # def paintEvent(self, paint_event):
    #     if self.filename:
    #         pixmap_ = QPixmap(self.pixmap.size())
    #         qp=QPainter(self.pixmap)
    #         self.label.setPixmap(self.pixmap)
    #         #qp.drawPixmap(self.label.rect(), self.pixmap)
    #         qp.drawPoint(300,200)
    #         qp.end()
    #         for pos in self.chosen_points:
    #             qp.drawPoint(pos)

    def keyReleaseEvent(self,event):
        if event.key()==49:
            self.comboBox.setCurrentIndex(1)
        if event.key()==50:
            self.comboBox.setCurrentIndex(2)
        if event.key()==51:
            self.comboBox.setCurrentIndex(3)
        if event.key()==52:
            self.comboBox.setCurrentIndex(4)

    def mouseReleaseEvent(self, cursor_event):
        self.chosen_points.append(cursor_event.pos())
        self.update()
    
    def addPoint(self,add_event):
        print(str(add_event.x())+" , "+str(add_event.y()))
    
    
    def calculate(self):
        for i in range(1,5):
            lineEdit_x = self.findChild(QLineEdit, "lineEdit_x"+str(i)).text()
            lineEdit_ax = self.findChild(QLineEdit, "lineEdit_ax"+str(i)).text()
            lineEdit_y = self.findChild(QLineEdit, "lineEdit_y"+str(i)).text()
            lineEdit_ay = self.findChild(QLineEdit, "lineEdit_ay"+str(i)).text()
            x = float(lineEdit_x)
            ax = float(lineEdit_ax)
            y = float(lineEdit_y)
            ay = float(lineEdit_ay)
            calx =round((x-ax),7)
            caly =round((y-ay),7)
            mean =round((((calx**2+caly**2)/2)**(1/2)),7)
            self.tableWidget.setItem(i-1,2,QTableWidgetItem(str(calx)))
            self.tableWidget.setItem(i-1,3,QTableWidgetItem(str(caly)))
            self.tableWidget.setItem(i-1,4,QTableWidgetItem(str(mean)))


    def TableSetting_x1(self,text):
        self.tableWidget.setItem(0,0,QTableWidgetItem(text))
    def TableSetting_x2(self,text):
        self.tableWidget.setItem(1,0,QTableWidgetItem(text)) 
    def TableSetting_x3(self,text):
        self.tableWidget.setItem(2,0,QTableWidgetItem(text))
    def TableSetting_x4(self,text):
        self.tableWidget.setItem(3,0,QTableWidgetItem(text))
    def TableSetting_y1(self,text):
        self.tableWidget.setItem(0,1,QTableWidgetItem(text))
    def TableSetting_y2(self,text):
        self.tableWidget.setItem(1,1,QTableWidgetItem(text)) 
    def TableSetting_y3(self,text):
        self.tableWidget.setItem(2,1,QTableWidgetItem(text))
    def TableSetting_y4(self,text):
        self.tableWidget.setItem(3,1,QTableWidgetItem(text))
  


#############################
#  Graphics Widget          #
#############################

class View(QGraphicsView):

    image = None
    window = None
    window_com = None
    window_x1 =None
    window_x2 =None
    window_x3 =None
    window_x4 =None
    window_y1 =None
    window_y2 =None
    window_y3 =None
    window_y4 =None
    sta =None
    
    def __init__(self, form_class):
        super(View,self).__init__()
        self.scene = QGraphicsScene(self)
        self.graphicsView = QGraphicsView()

        self.items =[]
        self.chosen_points =[]
        
        self.setRenderHint(QPainter.HighQualityAntialiasing)
        self.setFixedSize(1440,810)
        
        self.start = QPointF()
        self.end = QPointF() 
        
        self.past_x =None
        self.past_y =None
        self.present_x = None
        self.present_y = None
        

    def load(self,fileName):
        self.image = QImage(fileName)
        if self.image.isNull():
            QMessageBox.information(self,QApplication.applicationName(),
                                    "Cannot load "+fileName)
            self.setWindowTitle("Image viewer")

        image =QPixmap.fromImage(self.image)
        img_scaled = QPixmap()
        img_scaled = image.scaled(self.width(),self.height(),Qt.KeepAspectRatio)
        print(str(self.width())+"+"+str(self.height()))
        self.scene.addPixmap(img_scaled)
        self.setScene(self.scene)      

    def moveEvent(self,event):
        rect = QRectF(self.rect())
        rect.adjust(0,0,-2,-2)
        self.scene.setSceneRect(rect)
    
    def clear(self):
        self.viewport.update()
        self.scene.clear()

    def mousePressEvent(self, event):
        if event.button == Qt.RightButton:
            self.start =event.pos()
            self.end= event.pos()
        
    def mouseMoveEvent(self, event):
        pen = QPen(QColor(0,255,0),5)
        x=event.x()
        y=event.y()
        if self.past_x is None:
            self.past_x = x
            self.past_y = y
        else:
            self.present_x =x
            self.present_y = y
        if event.buttons() & Qt.RightButton: 
            
            self.end = event.pos()

            if len(self.items)>0:
                self.scene.removeItem(self.items[-1])
                del(self.items[-1])
            line = QLineF(self.past_x,self.past_y,self.end.x(),self.end.y())
            self.items.append(self.scene.addLine(line,pen))

        px = event.localPos().x()
        py = event.localPos().y()
        mouse_pt = "Mouse Point : x = {0},y={1}".format(event.x(),event.y())
        self.window.setText(mouse_pt)
        self.window.adjustSize()
        print(str(event.x())+" , "+str(event.y()))
        if (1==self.window_com.currentIndex()):
            self.window_x1.setText(str(px))
            self.window_y1.setText(str(py))
        if (2==self.window_com.currentIndex()):
            self.window_x2.setText(str(px))
            self.window_y2.setText(str(py))
        if (3==self.window_com.currentIndex()):
            self.window_x3.setText(str(px))
            self.window_y3.setText(str(py))
        if (4==self.window_com.currentIndex()):
            self.window_x4.setText(str(px))
            self.window_y4.setText(str(py))
    
    def mouseReleaseEvent(self, event):
        pen_line = QPen(QColor(0,255,0),5)
        x=event.x()
        y=event.y()
        if self.past_x is None:
            self.past_x = x
            self.past_y = y
        else:
            self.present_x =x
            self.present_y = y
        line = QLineF(self.past_x,self.past_y,self.end.x(),self.end.y())
        self.items.append(self.scene.addLine(line,pen_line))

        pen = QPen(QColor(255,255,255),10)
        if(1==self.window_com.currentIndex()):
            x1=event.x()
            y1=event.y()
            brush = QBrush(QColor(255,0,0))
            ellipse1 =self.scene.addEllipse(x1,y1,5,5,pen,brush)
            self.items.append(ellipse1)

        if(2==self.window_com.currentIndex()):
            brush = QBrush(QColor(255,255,0))
            self.scene.addEllipse(x,y,5,5,pen,brush)
        if(3==self.window_com.currentIndex()):
            brush = QBrush(QColor(0,255,0))
            self.scene.addEllipse(x,y,5,5,pen,brush)
        if(4==self.window_com.currentIndex()):
            brush = QBrush(QColor(0,0,255))
            self.scene.addEllipse(x,y,4,4,pen,brush)
        print(x)
        self.past_x = x
        self.past_y = y

    def setUI(self, label_mouse):
        self.window = label_mouse  
    def setUI_com(self, ComboBox):
        self.window_com = ComboBox
    def setUI_x1(self, lineEdit_x1):
        self.window_x1 = lineEdit_x1
    def setUI_x2(self, lineEdit_x2):
        self.window_x2 = lineEdit_x2
    def setUI_x3(self, lineEdit_x3):
        self.window_x3 = lineEdit_x3
    def setUI_x4(self, lineEdit_x4):
        self.window_x4 = lineEdit_x4
    def setUI_y1(self, lineEdit_y1):
        self.window_y1 = lineEdit_y1
    def setUI_y2(self, lineEdit_y2):
        self.window_y2 = lineEdit_y2
    def setUI_y3(self, lineEdit_y3):
        self.window_y3 = lineEdit_y3
    def setUI_y4(self, lineEdit_y4):
        self.window_y4 = lineEdit_y4  
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()