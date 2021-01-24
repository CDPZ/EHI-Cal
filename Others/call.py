
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import numpy as np
import pandas as pd

import matplotlib
matplotlib.use("Qt5Agg")  # 声明使用QT5
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

class Ui_Draw(object):
    def setupUi(self, Draw):
        Draw.setObjectName("Draw")
        Draw.resize(171, 81)
        self.load = QtWidgets.QPushButton(Draw)
        self.load.setGeometry(QtCore.QRect(0, 0, 171, 81))
        self.load.setObjectName("load")
        
# =============================================================================
#         self.Campus.setGeometry(QtCore.QRect(30, 110, 761, 681))
#         self.Campus.setObjectName("Campus")
# =============================================================================

        self.retranslateUi(Draw)
        QtCore.QMetaObject.connectSlotsByName(Draw)

    def retranslateUi(self, Draw):
        _translate = QtCore.QCoreApplication.translate
        Draw.setWindowTitle(_translate("Draw", "Draw"))
        self.load.setText(_translate("Draw", "导入文件..."))
        self.load.clicked.connect(self.open_event)
    def open_event(self):
        _translate = QtCore.QCoreApplication.translate
        directory1 = QFileDialog.getOpenFileName(None, "选择文件", "H:/")
        path = directory1[0]
        if path is not None:
            self.F = MyFigure(width=3, height=2, dpi=100)
            self.F.draw(path)
            graphicscene = QtWidgets.QGraphicsScene()  # 第三步，创建一个QGraphicsScene，因为加载的图形（FigureCanvas）不能直接放到graphicview控件中，必须先放到graphicScene，然后再把graphicscene放到graphicview中
            graphicscene.addWidget(self.F)  # 第四步，把图形放到QGraphicsScene中，注意：图形是作为一个QWidget放到QGraphicsScene中的
            self.Campus = QtWidgets.QGraphicsView(Draw)
            self.Campus.setScene(graphicscene) # 第五步，把QGraphicsScene放入QGraphicsView
            self.Campus.show()
        else:
            print("")
#创建一个matplotlib图形绘制类
class MyFigure(FigureCanvas):
    def __init__(self,width=10, height=10, dpi=100):
        #第一步：创建一个创建Figure
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        #第二步：在父类中激活Figure窗口
        super(MyFigure,self).__init__(self.fig) #此句必不可少，否则不能显示图形
        #第三步：创建一个子图，用于绘制图形用，111表示子图编号，如matlab的subplot(1,1,1)
        self.axes = self.fig.add_subplot(111)
    #第四步：就是画图，【可以在此类中画，也可以在其它类中画】

    def center(self, closedx,closedy):
        
        area = 0.0
        C_x,C_y = 0.0,0.0
    
        for i in range(len(closedx)):
            x = closedx[i]  
            y = closedy[i]  
     
            if i == len(closedx)-1:
                x1 = closedx[0]
                y1 = closedy[0]
            else:
                x1 = closedx[i + 1]
                y1 = closedy[i + 1]
     
            fg = (x*y1 - y*x1)/2.0
     
            area += fg
            C_x += fg*(x+x1+0)/3.0
            C_y += fg*(y+y1+0)/3.0
    
        C_x = C_x/area
        C_y = C_y/area
     
        return C_x,C_y
    
    def draw(self,path):
        plt.rcParams['font.sans-serif']=['SimHei']
        plt.rcParams['axes.unicode_minus']=False
        df = pd.read_csv(path, header=0)
        x = []
        y = []
        for i in range(df.shape[0]):
            x.append(df.iloc[i][1])
            y.append(df.iloc[i][2])
            
        self.axes.set(xlim=[min(y)-25, max(y)+25], ylim=[min(x)-25, max(x)+25], title='Campus', ylabel='X-Axis', xlabel='Y-Axis')
        startx = x[0]
        starty = y[0]
        closedx = []
        closedy = []
        #dep = []
        status = 1
        for i in range(len(x)):
            if x[i] == startx and y[i] == starty and status == 0:
                closedx.append(x[i])
                closedy.append(y[i])
                #dep.append(plt.fill(closedy, closedx, color='black', linestyle='dashed'))
                plt.plot(closedy, closedx, color='black', linestyle='dashed')
                cx, cy = self.center(closedx, closedy)
                if i < 29:
                    plt.text(cy, cx, '信息学部', fontsize=9, color = "k", style = "italic", weight = "light", verticalalignment='center', horizontalalignment='center')
                elif i < 76:
                    plt.text(cy, cx, '文理学部', fontsize=9, color = "k", style = "italic", weight = "light", verticalalignment='center', horizontalalignment='center')
                elif i < 103:
                    plt.text(cy, cx, '工学部', fontsize=9, color = "k", style = "italic", weight = "light", verticalalignment='center', horizontalalignment='center')
                else :
                    plt.text(cy, cx, '医学部', fontsize=9, color = "k", style = "italic", weight = "light", verticalalignment='center', horizontalalignment='center')
                #plt.annotate(u'叶子',(x,y),fontproperties=font) 
                closedy = []
                closedx = []
    
                if i + 1 < len(x):
                    startx = x[i + 1]
                    starty = y[i + 1]
                    status = 1
            elif x[i] == startx and y[i] == starty and status != 0:
                status = 0
                closedx.append(x[i])
                closedy.append(y[i])
            else:
                closedx.append(x[i])
                closedy.append(y[i])
    # =============================================================================
    #     for i in range(len(dep)):
    #         ax.add_patch(dep[i])
    # =============================================================================
        plt.scatter(y, x, color='red', marker='+')
        plt.show()
        print("ok")

 
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = QtWidgets.QWidget()
    ui = Ui_Draw()
    ui.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())