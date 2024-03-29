# -*- coding: utf-8 -*-
# run again.  Do not edit this file unless you know what you are doing.
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from functools import partial
from pathlib import Path
import sys
import pickle
import os
import math
import decimal
#import cv2
import numpy as np
from pyaxidraw import axidraw

#I had to add this for myself - Emre

from ModifyWindow_GUI import Ui_ModifyWindow

# makes GUI correct size for higher screen resolution

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
# Set up the main GUI window
class Ui_SpottingExp(QMainWindow):

    #Set up buttons and widgets
    def setupUi(self, SpottingExp):

        self.connection = False              # variable to see the connection status of the axidraw
        self.ad = axidraw.AxiDraw()          # Initialize class
        self.ad.interactive()                # Enter interactive context
        self.ad.options.units = 2           # change units to millimeters
        self.ad.options.pen_pos_up = 34
        self.ad.options.pen_pos_down = 100
        self.ad.update()

        SpottingExp.setObjectName("SpottingExp")
        SpottingExp.resize(650, 400)
        SpottingExp.setWindowOpacity(1)
        self.centralwidget = QtWidgets.QWidget(SpottingExp)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 281, 51))
        font_16 = QtGui.QFont()
        font_16.setFamily("Arial")
        font_16.setPointSize(16)
        self.label.setFont(font_16)
        self.label.setObjectName("label")

        font_10 = QtGui.QFont()
        font_10.setFamily("Arial")
        font_10.setPointSize(8)
        
        font_12 = QtGui.QFont()
        font_12.setFamily("Arial")
        font_12.setPointSize(10)
        
        font_bold12 = QtGui.QFont()
        font_bold12.setFamily("Arial")
        font_bold12.setPointSize(10)
        font_bold12.setBold(True)
        font_bold12.setWeight(75)

        spinBoxpos1 = 150
        spinBoxpos2 = 200
        spinBoxpos3 = 500
        spinBoxpos4 = 550


        self.pushButton_CONNECT = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_CONNECT.setGeometry(QtCore.QRect(375, 10, 81, 31))
        self.pushButton_CONNECT.setFont(font_12)
        self.pushButton_CONNECT.setObjectName("pushButton_CONNECT")

        self.pushButton_DISCONNECT = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_DISCONNECT.setGeometry(QtCore.QRect(475, 10, 81, 31))
        self.pushButton_DISCONNECT.setFont(font_12)
        self.pushButton_DISCONNECT.setObjectName("pushButton_DISCONNECT")

        self.pushButton_PENDOWN = QtWidgets.QPushButton(self.centralwidget) #used to be PENUP
        self.pushButton_PENDOWN.setGeometry(QtCore.QRect(250, 90, 81, 31))
        self.pushButton_PENDOWN.setFont(font_12)
        self.pushButton_PENDOWN.setObjectName("pushButton_PENDOWN")

        self.pushButton_PENUP = QtWidgets.QPushButton(self.centralwidget) #used to be PENDOWN
        self.pushButton_PENUP.setGeometry(QtCore.QRect(250, 50, 81, 31))
        self.pushButton_PENUP.setFont(font_12)
        self.pushButton_PENUP.setObjectName("pushButton_PENUP")

        self.pushButton_HOME = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_HOME.setGeometry(QtCore.QRect(10,340, 81, 31))
        self.pushButton_HOME.setFont(font_12)
        self.pushButton_HOME.setObjectName("pushButton_HOME")

        self.pushButton_SPOT = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_SPOT.setGeometry(QtCore.QRect(150, 340, 81, 31))
        self.pushButton_SPOT.setFont(font_bold12)
        self.pushButton_SPOT.setObjectName("pushButton_SPOT")

        SpottingExp.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SpottingExp)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 578, 22))
        self.menubar.setObjectName("menubar")
        SpottingExp.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SpottingExp)
        self.statusbar.setObjectName("statusbar")
        SpottingExp.setStatusBar(self.statusbar)

        self.pushButton_DIP = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_DIP.setGeometry(QtCore.QRect(10, 260, 81, 31))
        self.pushButton_DIP.setFont(font_12)
        self.pushButton_DIP.setObjectName("pushButton_DIP")

        self.sampleno_DIP = QtWidgets.QComboBox(self.centralwidget)
        self.sampleno_DIP.addItems(["1", "2", "3", "4", "5", "6", "7", "8"])
        self.sampleno_DIP.setGeometry(QtCore.QRect(spinBoxpos1, 260, 50, 31))
        self.sampleno_DIP.setFont(font_12)
        self.sampleno_DIP.setObjectName("sampleno_DIP")

        self.tipNo = QtWidgets.QComboBox(self.centralwidget)
        self.tipNo.addItems(["1", "2", "3", "4", "5", "6", "7", "8"])
        self.tipNo.setGeometry(QtCore.QRect(spinBoxpos3-50, 340, 50, 31))
        self.tipNo.setFont(font_12)
        self.tipNo.setObjectName("tipNo")

        self.pushButton_CLT = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_CLT.setGeometry(QtCore.QRect(500, 340, 81, 31))
        self.pushButton_CLT.setFont(font_12)
        self.pushButton_CLT.setObjectName("pushButton_CLT")

        self.pushButton_GetT = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_GetT.setGeometry(QtCore.QRect(spinBoxpos3-130, 340, 81, 31))
        self.pushButton_GetT.setFont(font_12)
        self.pushButton_GetT.setObjectName("pushButton_GetT")

        
        self.spinBox_goPosx = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.spinBox_goPosx.setGeometry(QtCore.QRect(spinBoxpos1, 300, 60, 31))
        self.spinBox_goPosx.setFont(font_12)
        self.spinBox_goPosx.setMinimum(0)
        self.spinBox_goPosx.setMaximum(150)
        self.spinBox_goPosx.setProperty("value", 0)
        self.spinBox_goPosx.setObjectName("spinBox_goPosx")

        self.spinBox_goPosy = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.spinBox_goPosy.setGeometry(QtCore.QRect(spinBoxpos2 + 20, 300, 60, 31))
        self.spinBox_goPosy.setFont(font_12)
        self.spinBox_goPosy.setMinimum(0)
        self.spinBox_goPosy.setMaximum(150)
        self.spinBox_goPosy.setProperty("value", 0)
        self.spinBox_goPosy.setObjectName("spinBox_goPosy")

        self.pushButton_GoTo = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_GoTo.setGeometry(QtCore.QRect(10, 300, 81, 31))
        self.pushButton_GoTo.setFont(font_12)
        self.pushButton_GoTo.setObjectName("pushButton_GoTo")

        #MODIFY WINDOW CARRIED BELOW THIS LINE

        self.label_rown = QtWidgets.QLabel(self.centralwidget)
        self.label_rown.setGeometry(QtCore.QRect(10+660, 90, 50, 31))
        self.label_rown.setFont(font_12)
        self.label_rown.setObjectName("label_rown")
        self.label_coln = QtWidgets.QLabel(self.centralwidget)
        self.label_coln.setGeometry(QtCore.QRect(10+660, 130, 50, 31))
        self.label_coln.setFont(font_12)
        self.label_coln.setObjectName("label_coln")

        self.label_rowDisp = QtWidgets.QLabel(self.centralwidget)
        self.label_rowDisp.setGeometry(QtCore.QRect(spinBoxpos3-150, 130, 150, 31))
        self.label_rowDisp.setFont(font_12)
        self.label_rowDisp.setObjectName("label_rowDisp")

        self.label_colDisp = QtWidgets.QLabel(self.centralwidget)
        self.label_colDisp.setGeometry(QtCore.QRect(spinBoxpos3-150, 170, 150, 31))
        self.label_colDisp.setFont(font_12)
        self.label_colDisp.setObjectName("label_colDisp")
       
        self.label_ppd = QtWidgets.QLabel(self.centralwidget)
        self.label_ppd.setGeometry(QtCore.QRect(10, 50, 161, 31))
        self.label_ppd.setFont(font_12)
        self.label_ppd.setObjectName("label_ppd")

        self.label_ppu = QtWidgets.QLabel(self.centralwidget)
        self.label_ppu.setGeometry(QtCore.QRect(10, 90, 161, 31))
        self.label_ppu.setFont(font_12)
        self.label_ppu.setObjectName("label_ppu")

        

        self.spinBox_ppu = QtWidgets.QSpinBox(self.centralwidget) #used to be spinBox_ppd
        self.spinBox_ppu.setGeometry(QtCore.QRect(spinBoxpos1, 50, 47, 31))
        self.spinBox_ppu.setFont(font_12)
        self.spinBox_ppu.setMinimum(0)
        self.spinBox_ppu.setMaximum(1000)
        self.spinBox_ppu.setObjectName("spinBox_ppu")

        self.spinBox_ppd = QtWidgets.QSpinBox(self.centralwidget) #used to be spinBox_ppu
        self.spinBox_ppd.setGeometry(QtCore.QRect(spinBoxpos1, 90, 47, 31))
        self.spinBox_ppd.setFont(font_12)
        self.spinBox_ppd.setMinimum(0)
        self.spinBox_ppd.setMaximum(1000)
        self.spinBox_ppd.setObjectName("spinBox_ppd")

        self.spinBox_rown = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_rown.setGeometry(QtCore.QRect(spinBoxpos1, 130, 47, 31))
        self.spinBox_rown.setFont(font_12)
        self.spinBox_rown.setMinimum(0)
        self.spinBox_rown.setMaximum(100)
        self.spinBox_rown.setObjectName("spinBox_rown")

        self.spinBox_coln = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_coln.setGeometry(QtCore.QRect(spinBoxpos1, 170, 47, 31))
        self.spinBox_coln.setFont(font_12)
        self.spinBox_coln.setMinimum(0)
        self.spinBox_coln.setMaximum(100)
        self.spinBox_coln.setObjectName("spinBox_coln")

        self.spinBox_px = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.spinBox_px.setGeometry(QtCore.QRect(spinBoxpos2, 210, 47, 31))
        self.spinBox_px.setFont(font_12)
        self.spinBox_px.setMinimum(0)
        self.spinBox_px.setMaximum(150)
        self.spinBox_px.setObjectName("spinBox_px")

        self.spinBox_py = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.spinBox_py.setGeometry(QtCore.QRect(spinBoxpos1, 210, 47, 31))
        self.spinBox_py.setFont(font_12)
        self.spinBox_py.setMinimum(0)
        self.spinBox_py.setMaximum(150)
        self.spinBox_py.setObjectName("spinBox_py")



        self.spinBox_rowDisp = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.spinBox_rowDisp.setGeometry(QtCore.QRect(spinBoxpos3, 130, 47, 31))
        self.spinBox_rowDisp.setFont(font_12)
        self.spinBox_rowDisp.setMinimum(0)
        self.spinBox_rowDisp.setMaximum(500)
        self.spinBox_rowDisp.setObjectName("spinBox_rowDisp")

        self.spinBox_colDisp = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.spinBox_colDisp.setGeometry(QtCore.QRect(spinBoxpos3, 170, 47, 31))
        self.spinBox_colDisp.setFont(font_12)
        self.spinBox_colDisp.setMinimum(0)
        self.spinBox_colDisp.setMaximum(500)
        self.spinBox_colDisp.setObjectName("spinBox_colDisp")

        self.label_startpos = QtWidgets.QLabel(self.centralwidget)
        self.label_startpos.setGeometry(QtCore.QRect(10, 210, 160, 31))
        self.label_startpos.setFont(font_12)
        self.label_startpos.setObjectName("label_startpos")

        self.label_dippos = QtWidgets.QLabel(self.centralwidget)
        self.label_dippos.setGeometry(QtCore.QRect(spinBoxpos3-130, 220, 160, 31))
        self.label_dippos.setFont(font_12)
        self.label_dippos.setObjectName("label_dippos")

        self.label_rown = QtWidgets.QLabel(self.centralwidget)
        self.label_rown.setGeometry(QtCore.QRect(10, 130, 160, 31))
        self.label_rown.setFont(font_12)
        self.label_rown.setObjectName("label_rown")

        self.label_coln = QtWidgets.QLabel(self.centralwidget)
        self.label_coln.setGeometry(QtCore.QRect(10, 170, 160, 31))
        self.label_coln.setFont(font_12)
        self.label_coln.setObjectName("label_coln")

        #MODIFY WINDOW ABOVE THIS LINE

        if self.spinBox_rown.text() == '':
            rowNum = 1 #Kreiver
        else:
            rowNum = int(self.spinBox_rown.text())

        if self.spinBox_coln.text() == '':
            colNum = 4 #Kreiver
        else:
            colNum = int(self.spinBox_coln.text())

        self.rowNum = rowNum
        self.colNum = colNum

        
        pdd = 10         
        pdu = 10

        self.pdd = pdd
        self.pdu = pdu

        if self.spinBox_ppd.text() == '':
            ppd = 34 #Kreiver
        else:
            ppd = int(self.spinBox_ppd.text())
        if self.spinBox_ppu.text() == '':
            ppu = 100
        else:
            ppu = int(self.spinBox_ppu.text())

        self.ppd = ppd
        self.ppu = ppu


        if self.spinBox_rowDisp.text() == '':
            rowDisp = 1.1
        else:
            rowDisp = float(self.spinBox_rowDisp.text())
        if self.spinBox_colDisp.text() == '':
            colDisp = 1.1
        else:
            colDisp = float(self.spinBox_colDisp.text())

        self.rowDisp = rowDisp
        self.colDisp = colDisp

        if self.spinBox_px.text() == '':
            startpx = 1
        else:
            startpx = float(self.spinBox_px.text())*self.colDisp
        if self.spinBox_py.text() == '':
            startpy = 1
        else:
            startpy = float(self.spinBox_py.text())*self.rowDisp

        self.startpx = startpx
        self.startpy = startpy

        
        dipPosx1 = 144 #Kreiver, in cm        
        dipPosy1 = 69.5 #Kreiver, in cm
        
        self.dipPosx1 = dipPosx1
        self.dipPosy1 = dipPosy1

        
        dipPosx2 = 144 #Kreiver    
        dipPosy2 = 60.5 #Kreiver
            
        self.dipPosx2 = dipPosx2
        self.dipPosy2 = dipPosy2

        
        dipPosx3 = 144 #Kreiver        
        dipPosy3 = 51.5 #Kreiver
       
        self.dipPosx3 = dipPosx3
        self.dipPosy3 = dipPosy3

        #Kreiver, for Dip Sample
        self.dipPositionx = 144.50
        self.dipPositiony = 69.50

        self.tipPositionx = 79.50
        self.tipPositiony = 91.30
        
        # self.spinBox_pdd.setValue(self.pdd)
        # self.spinBox_pdu.setValue(self.pdu)
        # self.spinBox_ppd.setValue(self.ppd)
        # self.spinBox_ppu.setValue(self.ppu)
        # self.spinBox_rown.setValue(self.rowNum)
        # self.spinBox_coln.setValue(self.colNum)
        # self.spinBox_px.setValue(self.startpx)
        # self.spinBox_py.setValue(self.startpy)
        # self.spinBox_rowDisp.setValue(self.rowDisp)
        # self.spinBox_colDisp.setValue(self.colDisp)
        # self.spinBox_dipPosx1.setValue(self.dipPosx1)
        # self.spinBox_dipPosy1.setValue(self.dipPosy1)
        # self.spinBox_dipPosx2.setValue(self.dipPosx2)
        # self.spinBox_dipPosy2.setValue(self.dipPosy2)
        # self.spinBox_dipPosx3.setValue(self.dipPosx3)
        # self.spinBox_dipPosy3.setValue(self.dipPosy3)

        
        self.spinBox_ppd.setProperty("value", self.ppd)
        self.spinBox_ppu.setProperty("value", self.ppu)
        
        self.spinBox_rown.setProperty("value", self.rowNum)
        self.spinBox_coln.setProperty("value", self.colNum)
        
        self.spinBox_px.setProperty("value", self.startpx)
        self.spinBox_py.setProperty("value", self.startpy)
        
        self.spinBox_rowDisp.setProperty("value", self.rowDisp)
        self.spinBox_colDisp.setProperty("value", self.colDisp)
        

        self.retranslateUi(SpottingExp)

        QtCore.QMetaObject.connectSlotsByName(SpottingExp)

        # Connect buttons to events and functions
        self.pushButton_CONNECT.clicked.connect(self.connectAxi)
        self.pushButton_DISCONNECT.clicked.connect(self.disconnectAxi)
       
        self.pushButton_PENDOWN.clicked.connect(lambda: self.ad.pendown()) #USED TO BE PENUP
        self.pushButton_PENUP.clicked.connect(lambda: self.ad.penup()) #USED TO BE PENDOWN
        
        self.pushButton_HOME.clicked.connect(lambda: self.ad.goto(0, 0))
        
        self.pushButton_SPOT.clicked.connect(self.runSpotter)
        
        self.pushButton_DIP.clicked.connect(self.DipSample)
        self.sampleno_DIP.currentIndexChanged.connect(self.index_changed)
        self.tipNo.currentIndexChanged.connect(self.index_changed_tip)
        
        self.pushButton_CLT.clicked.connect(self.ClearTip)
        self.pushButton_GetT.clicked.connect(self.GetTip)
        
        self.pushButton_GoTo.clicked.connect(lambda: self.ad.goto(float(self.spinBox_goPosx.text()),float(self.spinBox_goPosy.text())))

        
        self.spinBox_ppd.valueChanged.connect(self.UpdateModiVal)
        self.spinBox_ppu.valueChanged.connect(self.UpdateModiVal)
        
        self.spinBox_rown.valueChanged.connect(self.UpdateModiVal)
        self.spinBox_coln.valueChanged.connect(self.UpdateModiVal)
        
        self.spinBox_rowDisp.valueChanged.connect(self.UpdateModiVal)
        self.spinBox_colDisp.valueChanged.connect(self.UpdateModiVal)
        
        self.spinBox_px.valueChanged.connect(self.UpdateModiVal)
        self.spinBox_py.valueChanged.connect(self.UpdateModiVal)

    # adding text to all the buttons and labels
    def retranslateUi(self, SpottingExp):
        _translate = QtCore.QCoreApplication.translate

        SpottingExp.setWindowTitle(_translate("SpottingExp", "Spotting Experiment"))
        self.label.setText(_translate("SpottingExp", "AxiDraw Spotting Experiment"))
        self.pushButton_CONNECT.setText(_translate("SpottingExp", "Connect"))
        self.pushButton_DISCONNECT.setText(_translate("SpottingExp", "Disconnect"))
        self.pushButton_PENDOWN.setText(_translate("SpottingExp", "Pen Down")) #used to be PENUP
        self.pushButton_PENUP.setText(_translate("SpottingExp", "Pen Up")) #used to be PENDOWN
        self.pushButton_SPOT.setText(_translate("SpottingExp", "Spot!"))
        self.pushButton_HOME.setText(_translate("SpottingExp", "Home"))
        self.pushButton_DIP.setText(_translate("SpottingExp", "Dip"))
        self.pushButton_CLT.setText(_translate("SpottingExp", "Clear Tip"))
        self.pushButton_GetT.setText(_translate("SpottingExp", "Get Tip"))
        self.pushButton_GoTo.setText(_translate("SpottingExp", "Go(x,y)"))

        #FROM MODIFY WINDOW

        self.label_rown.setText(_translate("SpottingExp", "Number of Columns: ")) #FIXED THE ROW COLUMN IN ONLY TEXT
        self.label_coln.setText(_translate("SpottingExp", "Number of Rows: "))
        self.label_startpos.setText(_translate("SpottingExp", "Starting Position (c,r):"))
        
        self.label_ppu.setText(_translate("SpottingExp", "Pen Position Down (%)"))
        self.label_ppd.setText(_translate("SpottingExp", "Pen Position Up (%)"))

        self.label_rowDisp.setText(_translate("SpottingExp", "Column Displacement: "))
        self.label_colDisp.setText(_translate("SpottingExp", "Row Displacement: "))

        #END FROM MOD WINDOW


    def connectAxi(self):
        if self.connection == False:
            self.ad.interactive() 
            self.ad.connect() 
            self.ad.options.units = 2 
            self.ad.update()
            self.connection = True
            msg = QMessageBox()
            msg.setWindowTitle("Connection Status")
            msg.setText("AxiDraw is now connected.")
            msg.setStandardButtons(QMessageBox.Ok)
            x = msg.exec_()
        elif self.connection == True:
            msg = QMessageBox()
            msg.setWindowTitle("Connection Status")
            msg.setText("AxiDraw is already connected.")
            msg.setStandardButtons(QMessageBox.Ok)
            x = msg.exec_()

    # disconnect Axidraw duh.
    def disconnectAxi(self):
        if self.connection == True:
            self.ad.disconnect()
            self.ad.plot_setup() #
            self.ad.options.mode = "manual" 
            self.ad.options.manual_cmd = "disable_xy" 
            self.ad.plot_run() 
            self.connection = False
            msg = QMessageBox()
            msg.setWindowTitle("Connection Status")
            msg.setText("AxiDraw is now disconnected.")
            msg.setStandardButtons(QMessageBox.Ok)
            x = msg.exec_()
        elif self.connection == False:
            msg = QMessageBox()
            msg.setWindowTitle("Connection Status")
            msg.setText("AxiDraw is already disconnected.")
            msg.setStandardButtons(QMessageBox.Ok)
            x = msg.exec_()


    def runSpotter(self):

        self.UpdateModiVal()

        if self.connection == False:
            msg = QMessageBox()
            msg.setWindowTitle("Connection Status")
            msg.setText("Please connect the AxiDraw.")
            msg.setStandardButtons(QMessageBox.Ok)
            x = msg.exec_()

        n = 0
        def makeRow(self):
            self.ad.update()

             
            
            for i in range(self.colNum):
                self.DipSample()
                
                self.ad.goto(self.startpx+((i-1)*self.colDisp)+ float(self.spinBox_goPosx.text()), float(self.spinBox_goPosy.text()) + (-self.startpy+((-n+1)*self.rowDisp)))
                #spinBox_goPosy = constant; self.startpy depends on relative col start position; -n+1 term dictates direction of # of columns
                self.ad.options.pen_pos_up = self.ppu
                self.ad.options.pen_pos_down = self.ppd
                self.ad.update()

                self.ad.pendown()
                self.ad.penup()
                self.ad.go(self.colDisp, 0)
            print("Loop ended")
            self.ad.go((-self.colNum)*(self.colDisp), -self.rowDisp)

        for i in range(self.rowNum):
            makeRow(self)
            n+=1
        self.ad.goto(float(self.spinBox_goPosx.text()), float(self.spinBox_goPosy.text()))

    def index_changed(self, i): # i is an int for the dip sample
        
        index = self.sampleno_DIP.currentText()
        pitch = 9
        constanty = 69.50
        self.dipPositiony = constanty - (int(index)-1)*pitch

    def index_changed_tip(self, i): # i is an int for the dip sample

        index = self.tipNo.currentText()
        pitch = 7
        constantx = 79.5
        self.tipPositionx = (int(index)-1)*pitch + constantx


    def DipSample(self):

        self.UpdateModiVal()

        self.ad.options.pen_pos_up = self.ppu
        self.ad.options.pen_pos_down = 0
        self.ad.update()
        
        if self.connection == False:
            msg = QMessageBox()
            msg.setWindowTitle("Connection Status")
            msg.setText("Please connect the AxiDraw.")
            msg.setStandardButtons(QMessageBox.Ok)
            x = msg.exec_()
        else:
            
            self.ad.goto(self.dipPositionx, self.dipPositiony)

            self.ad.pendown()
            self.ad.penup()
            self.ad.goto(self.startpx + float(self.spinBox_goPosx.text()), self.startpy + float(self.spinBox_goPosy.text()))

    def ClearTip(self):
        if self.connection == False:
            msg = QMessageBox()
            msg.setWindowTitle("Connection Status")
            msg.setText("Please connect the AxiDraw.")
            msg.setStandardButtons(QMessageBox.Ok)
            x = msg.exec_()
        else:
            self.ad.penup()
            self.ad.goto(0,0)
            self.ad.options.pen_pos_down = 33
            self.ad.update()
            self.ad.pendown()
            self.ad.goto(10,75) #Kreiver
            self.ad.penup()
            self.ad.goto(0,0)
            self.ad.options.pen_pos_up = self.ppu
            self.ad.update()

    def GetTip(self):
        if self.connection == False:
            msg = QMessageBox()
            msg.setWindowTitle("Connection Status")
            msg.setText("Please connect the AxiDraw.")
            msg.setStandardButtons(QMessageBox.Ok)
            x = msg.exec_()
        else:
            # print(self.tipPositionx)
            self.ad.goto(self.tipPositionx,self.tipPositiony)
            self.ad.options.pen_pos_down = 0
            self.ad.update()
            self.ad.pendown()
            self.ad.penup()
            self.ad.options.pen_pos_down = self.ppd
            self.ad.goto(self.tipPositionx,0)
            self.ad.goto(0,0)


    def UpdateModiVal(self):
        self.ad.options.pen_pos_up = self.ppu
        self.ad.options.pen_pos_down = self.ppd
        self.ad.options.pen_delay_down = self.pdd
        self.ad.options.pen_delay_up = self.pdu

        rowNum = int(self.spinBox_rown.text())
        colNum = int(self.spinBox_coln.text())

        

        ppd = int(self.spinBox_ppd.text())
        ppu = int(self.spinBox_ppu.text())

        rowDisp = float(self.spinBox_rowDisp.text())
        colDisp = float(self.spinBox_colDisp.text())

        self.rowDisp = rowDisp
        self.colDisp = colDisp

        startpx = float(self.spinBox_px.text())*self.colDisp
        startpy = float(self.spinBox_py.text())*self.rowDisp

        dipPosx1 = float(self.spinBox_dipPosx1.text())
        dipPosy1 = float(self.spinBox_dipPosy1.text())

        dipPosx2 = float(self.spinBox_dipPosx2.text())
        dipPosy2 = float(self.spinBox_dipPosy2.text())

        dipPosx3 = float(self.spinBox_dipPosx3.text())
        dipPosy3 = float(self.spinBox_dipPosy3.text())

        self.rowNum = rowNum
        self.colNum = colNum

        self.pdd = pdd
        self.pdu = pdu

        self.ppd = ppd
        self.ppu = ppu

        self.startpx = startpx
        self.startpy = startpy

        self.dipPosx1 = dipPosx1
        self.dipPosy1 = dipPosy1

        self.dipPosx2 = dipPosx2
        self.dipPosy2 = dipPosy2

        self.dipPosx3 = dipPosx3
        self.dipPosy3 = dipPosy3

 
        self.spinBox_ppd.setValue(ppd)
        self.spinBox_ppu.setValue(ppu)
        self.spinBox_rown.setValue(rowNum)
        self.spinBox_coln.setValue(colNum)
        self.spinBox_px.setValue(startpx/self.colDisp)
        self.spinBox_py.setValue(startpy/self.rowDisp)
        self.spinBox_rowDisp.setValue(rowDisp)
        self.spinBox_colDisp.setValue(colDisp)

        self.ad.update()

    def keyPressEvent(self, event):
        if self.connection == False:
            msg = QMessageBox()
            msg.setWindowTitle("Connection Status")
            msg.setText("Please connect the AxiDraw.")
            msg.setStandardButtons(QMessageBox.Ok)
            x = msg.exec_()
        else:
            self.UpdateModiVal()

            if event.key() == Qt.Key_Up:
                self.ad.penup()
            elif event.key() == Qt.Key_Down:
                self.ad.pendown()

# close gui
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SpottingExp = QtWidgets.QMainWindow()
    ui = Ui_SpottingExp()
    ui.setupUi(SpottingExp)
    SpottingExp.show()
    sys.exit(app.exec_())
