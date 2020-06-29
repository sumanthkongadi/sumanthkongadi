# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'final.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import numpy as np
import pandas as pd
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog, QMessageBox
from PyQt5.QtGui import QIcon, QPixmap
from sklearn import metrics
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
import operator
from tqdm import tqdm
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure



class Ui_MainWindow(QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1120, 596)
        self.fileval = ""
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.bbutton = QtWidgets.QPushButton(self.centralwidget)
        self.bbutton.setGeometry(QtCore.QRect(30, 20, 281, 31))
        self.bbutton.setObjectName("bbutton")
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(40, 150, 251, 22))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalSlider_2 = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_2.setGeometry(QtCore.QRect(40, 230, 251, 22))
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.error = QtWidgets.QTextEdit(self.centralwidget)
        self.error.setGeometry(QtCore.QRect(80, 270, 211, 101))
        self.error.setObjectName("error")
        #################################################################################
        self.trainvl = 0
        self.testvl = 0
        self.v = ""
        ##########################################################################################
        self.r2 = QtWidgets.QTextEdit(self.centralwidget)
        self.r2.setGeometry(QtCore.QRect(80, 380, 211, 31))
        self.r2.setObjectName("r2")
        self.x = QtWidgets.QLineEdit(self.centralwidget)
        self.x.setGeometry(QtCore.QRect(80, 430, 211, 31))
        self.x.setObjectName("x")
        self.y = QtWidgets.QLineEdit(self.centralwidget)
        self.y.setGeometry(QtCore.QRect(80, 480, 211, 31))
        self.y.setObjectName("y")
        self.sbutton = QtWidgets.QPushButton(self.centralwidget)
        self.sbutton.setGeometry(QtCore.QRect(630, 470, 121, 31))
        self.sbutton.setObjectName("sbutton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 270, 51, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 380, 47, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 430, 51, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 480, 47, 31))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(40, 190, 31, 21))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(40, 116, 41, 20))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(330, 20, 47, 13))
        self.label_7.setObjectName("label_7")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(10, 520, 781, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.trainvallbl = QtWidgets.QLabel(self.centralwidget)
        self.trainvallbl.setGeometry(QtCore.QRect(80, 120, 47, 13))
        self.trainvallbl.setText("")
        self.trainvallbl.setObjectName("trainvallbl")
        self.testvallbl = QtWidgets.QLabel(self.centralwidget)
        self.testvallbl.setGeometry(QtCore.QRect(90, 190, 47, 21))
        self.testvallbl.setText("")
        self.testvallbl.setObjectName("testvallbl")
        
        self.figure =Figure()
        self.canvas =FigureCanvas(self.figure)
        lay = QtWidgets.QVBoxLayout(self.centralwidget)
        lay.setContentsMargins(330, 40, 120, 125)
        lay.addWidget(self.canvas)
        self.toolbar =NavigationToolbar(self.canvas,self) 
        lay.addWidget(self.toolbar)        
        
        self.datasetlbl = QtWidgets.QLabel(self.centralwidget)
        self.datasetlbl.setGeometry(QtCore.QRect(40, 60, 271, 16))
        self.datasetlbl.setText("")
        self.datasetlbl.setObjectName("datasetlbl")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(820, 20, 47, 13))
        self.label_8.setObjectName("label_8")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(820, 40, 251, 441))
        self.textEdit.setObjectName("textEdit")
        self.getcolumnsbtn = QtWidgets.QPushButton(self.centralwidget)
        self.getcolumnsbtn.setGeometry(QtCore.QRect(500, 472, 111, 31))
        self.getcolumnsbtn.setObjectName("getcolumnsbtn")
        self.consolelbl = QtWidgets.QLabel(self.centralwidget)
        self.consolelbl.setGeometry(QtCore.QRect(826, 512, 241, 21))
        self.consolelbl.setText("")
        self.consolelbl.setObjectName("consolelbl")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1120, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
		
    ########################################################################
        
        self.sbutton.clicked.connect(self.linearregression)
        self.bbutton.clicked.connect(self.openFileNameDialog)
        self.horizontalSlider.valueChanged[int].connect(self.valuechangetrain)
        self.horizontalSlider_2.valueChanged[int].connect(self.valuechangetest)
        self.getcolumnsbtn.clicked.connect(self.getcolumns)
    ########################################################################
        
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.bbutton.setText(_translate("MainWindow", "Browse"))
        self.sbutton.setText(_translate("MainWindow", "Start"))
        self.label.setText(_translate("MainWindow", "ERROR:"))
        self.label_2.setText(_translate("MainWindow", "R2="))
        self.label_3.setText(_translate("MainWindow", "X="))
        self.label_4.setText(_translate("MainWindow", "Y="))
        self.label_5.setText(_translate("MainWindow", "TEST:"))
        self.label_6.setText(_translate("MainWindow", "TRAIN:"))
        self.label_7.setText(_translate("MainWindow", "GRAPH:"))
        self.label_8.setText(_translate("MainWindow", "Console:"))
        self.getcolumnsbtn.setText(_translate("MainWindow", "Get Columns"))
    

    
       
        



    
    def openFileNameDialog(self):
        options = QFileDialog.Options()
        self.fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileNmeme()","","all files(*);;csv files(*.csv *.xlsx *.xls)",options = options)
        if self.fileName:
                print(self.fileName)
                self.datasetlbl.setText(self.fileName)
                self.v = pd.read_csv(self.fileName)
    
        
    def linearregression(self):
        
        self.progressBar.setValue(0)
         
        self.X = self.v[self.x.text()].values.reshape(-1,1)
        self.Y = self.v[self.y.text()].values.reshape(-1,1)
        self.textEdit.append(str(self.X))
        self.textEdit.append(str(self.Y))
        print(self.X)
        print(self.Y)
        
        
        
             
        self.X_train, self.X_test, self.Y_train, self.Y_test = train_test_split(self.X,self.Y,test_size=0.5)
        self.lm = LinearRegression()
        self.model = self.lm.fit(self.X_train,self.Y_train)
        self.textEdit.append(str(self.lm.intercept_))
        self.progressBar.setValue(20)
        self.textEdit.append(str(self.lm.coef_))
        self.progressBar.setValue(40)
        self.r = self.model.score(self.X_train,self.Y_train)
        self.r2.append(str(self.r))
        self.progressBar.setValue(60)
        self.predictions = self.model.predict(self.X_test)
       
        
        self.ax = self.figure.add_subplot(111)
        self.ax.clear()
        self.ax.scatter(self.v[self.x.text()],self.v[self.y.text()],c = 'black')
        self.ax.plot(self.X_test,self.predictions, c = 'blue', linewidth = 2)
        self.canvas.draw()
        self.progressBar.setValue(80)
        
        self.error.setText("")
        self.error.append(f'MAE:\n {metrics.mean_absolute_error(self.Y_test,self.predictions)} \n MSE: \n{metrics.mean_squared_error(self.Y_test,self.predictions)} \n RMSE: \n {np.sqrt(metrics.mean_squared_error(self.Y_test,self.predictions))}')
        self.progressBar.setValue(100)
        self.progressBar.hide()
        
    def valuechangetrain(self, value):

        self.trainvl = value
        print(self.trainvl)
        self.trainvallbl.setText(str(value))
        
        
    def valuechangetest(self, value):

        self.testvl = value
        print(self.testvl)
        self.testvallbl.setText(str(value))
        
    
                
            
     
    def getcolumns(self):
            self.v.describe()
            for col in self.v.columns:
                    print(col)
                    self.textEdit.append(col)
            self.textEdit.append('''_____________________
            Please add X and Y values before analysing''')
			
			
			

    
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

