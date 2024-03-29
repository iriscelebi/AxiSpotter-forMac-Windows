# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ModifyWindow_GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
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
import decimal
from pyaxidraw import axidraw
# import csv
# from pyaxidraw import axidraw
# from PyQt5.QtWidgets import *
# app = QApplication([])
# app.setStyle('Fusion')

# makes GUI correct size for higher screen resolution
#from Spotexp_GUI import Ui_SpottingExp

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)


class Ui_ModifyWindow(QMainWindow):
    def setupUi(self, ModifyWindow):

        # initialize some variables here so when they are changed in the modify
        # window we can track and use the changes in the main window.


        ModifyWindow.setObjectName("ModifyWindow")
        ModifyWindow.resize(531, 477)

        font_title = QtGui.QFont("Arial")
        font_title.setFamily("Arial")
        font_title.setPointSize(12)
        font = QtGui.QFont("Arial")
        font.setFamily("Arial")
        font.setPointSize(10)

        self.centralwidget = QtWidgets.QWidget(ModifyWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 281, 41))
        self.label.setFont(font_title)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 261, 16))
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.label_rown = QtWidgets.QLabel(self.centralwidget)
        self.label_rown.setGeometry(QtCore.QRect(10, 90, 50, 31))
        self.label_rown.setFont(font)
        self.label_rown.setObjectName("label_rown")
        self.label_coln = QtWidgets.QLabel(self.centralwidget)
        self.label_coln.setGeometry(QtCore.QRect(10, 130, 50, 31))
        self.label_coln.setFont(font)
        self.label_coln.setObjectName("label_coln")

        self.label_rowDisp = QtWidgets.QLabel(self.centralwidget)
        self.label_rowDisp.setGeometry(QtCore.QRect(310, 90, 100, 31))
        self.label_rowDisp.setFont(font)
        self.label_rowDisp.setObjectName("label_rowDisp")

        self.label_colDisp = QtWidgets.QLabel(self.centralwidget)
        self.label_colDisp.setGeometry(QtCore.QRect(310, 130, 100, 31))
        self.label_colDisp.setFont(font)
        self.label_colDisp.setObjectName("label_colDisp")

        self.label_pdd = QtWidgets.QLabel(self.centralwidget)
        self.label_pdd.setGeometry(QtCore.QRect(310, 170, 161, 31))
        self.label_pdd.setFont(font)
        self.label_pdd.setObjectName("label_pdd")

        self.label_pdu = QtWidgets.QLabel(self.centralwidget)
        self.label_pdu.setGeometry(QtCore.QRect(310, 210, 161, 31))
        self.label_pdu.setFont(font)
        self.label_pdu.setObjectName("label_pdu")

        self.label_ppd = QtWidgets.QLabel(self.centralwidget)
        self.label_ppd.setGeometry(QtCore.QRect(310, 250, 161, 31))
        self.label_ppd.setFont(font)
        self.label_ppd.setObjectName("label_ppd")

        self.label_ppu = QtWidgets.QLabel(self.centralwidget)
        self.label_ppu.setGeometry(QtCore.QRect(310, 290, 161, 31))
        self.label_ppu.setFont(font)
        self.label_ppu.setObjectName("label_ppu")

        self.spinBox_pdd = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_pdd.setGeometry(QtCore.QRect(410, 170, 47, 31))
        self.spinBox_pdd.setFont(font)
        self.spinBox_pdd.setMinimum(0)
        self.spinBox_pdd.setMaximum(1000)
        #self.spinBox_pdd.setProperty("value", 0)
        self.spinBox_pdd.setObjectName("spinBox_pdd")

        self.spinBox_pdu = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_pdu.setGeometry(QtCore.QRect(410, 210, 47, 31))
        self.spinBox_pdu.setFont(font)
        self.spinBox_pdu.setMinimum(0)
        self.spinBox_pdu.setMaximum(1000)
        #self.spinBox_pdu.setProperty("value", 0)
        self.spinBox_pdu.setObjectName("spinBox_pdu")

    

        self.spinBox_ppd = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_ppd.setGeometry(QtCore.QRect(410, 250, 47, 31))
        self.spinBox_ppd.setFont(font)
        self.spinBox_ppd.setMinimum(0)
        self.spinBox_ppd.setMaximum(1000)
        #self.spinBox_pdd.setProperty("value", 0)
        self.spinBox_ppd.setObjectName("spinBox_ppd")

        self.spinBox_ppu = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_ppu.setGeometry(QtCore.QRect(410, 290, 47, 31))
        self.spinBox_ppu.setFont(font)
        self.spinBox_ppu.setMinimum(0)
        self.spinBox_ppu.setMaximum(1000)
        #self.spinBox_pdu.setProperty("value", 0)
        self.spinBox_pdu.setObjectName("spinBox_ppu")

        self.spinBox_rown = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_rown.setGeometry(QtCore.QRect(150, 90, 47, 31))
        self.spinBox_rown.setFont(font)
        self.spinBox_rown.setMinimum(0)
        self.spinBox_rown.setMaximum(100)
        #self.spinBox_rown.setProperty("value", 0)
        self.spinBox_rown.setObjectName("spinBox_rown")

        self.spinBox_coln = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_coln.setGeometry(QtCore.QRect(150, 130, 47, 31))
        self.spinBox_coln.setFont(font)
        self.spinBox_coln.setMinimum(0)
        self.spinBox_coln.setMaximum(100)
        #self.spinBox_coln.setProperty("value", 0)
        self.spinBox_coln.setObjectName("spinBox_coln")

        self.spinBox_px = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.spinBox_px.setGeometry(QtCore.QRect(200, 170, 47, 31))
        self.spinBox_px.setFont(font)
        self.spinBox_px.setMinimum(0)
        self.spinBox_px.setMaximum(150)
        #self.spinBox_px.setProperty("value", 0)
        self.spinBox_px.setObjectName("spinBox_px")

        self.spinBox_py = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.spinBox_py.setGeometry(QtCore.QRect(150, 170, 47, 31))
        self.spinBox_py.setFont(font)
        self.spinBox_py.setMinimum(0)
        self.spinBox_py.setMaximum(150)
        #self.spinBox_py.setProperty("value", 0)
        self.spinBox_py.setObjectName("spinBox_py")

        self.spinBox_dipPosx1 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.spinBox_dipPosx1.setGeometry(QtCore.QRect(150, 220, 47, 31))
        self.spinBox_dipPosx1.setFont(font)
        self.spinBox_dipPosx1.setMinimum(0)
        self.spinBox_dipPosx1.setMaximum(150)
        self.spinBox_dipPosx1.setObjectName("spinBox_dipPosx1")

        self.spinBox_dipPosx2 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.spinBox_dipPosx2.setGeometry(QtCore.QRect(150, 260, 47, 31))
        self.spinBox_dipPosx2.setFont(font)
        self.spinBox_dipPosx2.setMinimum(0)
        self.spinBox_dipPosx2.setMaximum(150)
        self.spinBox_dipPosx2.setObjectName("spinBox_dipPosx2")

        self.spinBox_dipPosx3 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.spinBox_dipPosx3.setGeometry(QtCore.QRect(150, 300, 47, 31))
        self.spinBox_dipPosx3.setFont(font)
        self.spinBox_dipPosx3.setMinimum(0)
        self.spinBox_dipPosx3.setMaximum(150)
        self.spinBox_dipPosx3.setObjectName("spinBox_dipPosx3")

        self.spinBox_dipPosy1 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.spinBox_dipPosy1.setGeometry(QtCore.QRect(200, 220, 47, 31))
        self.spinBox_dipPosy1.setFont(font)
        self.spinBox_dipPosy1.setMinimum(0)
        self.spinBox_dipPosy1.setMaximum(150)
        self.spinBox_dipPosy1.setObjectName("spinBox_dipPosy1")

        self.spinBox_dipPosy2 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.spinBox_dipPosy2.setGeometry(QtCore.QRect(200, 260, 47, 31))
        self.spinBox_dipPosy2.setFont(font)
        self.spinBox_dipPosy2.setMinimum(0)
        self.spinBox_dipPosy2.setMaximum(150)
        self.spinBox_dipPosy2.setObjectName("spinBox_dipPosy2")

        self.spinBox_dipPosy3 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.spinBox_dipPosy3.setGeometry(QtCore.QRect(200, 300, 47, 31))
        self.spinBox_dipPosy3.setFont(font)
        self.spinBox_dipPosy3.setMinimum(0)
        self.spinBox_dipPosy3.setMaximum(150)
        self.spinBox_dipPosy3.setObjectName("spinBox_dipPosy3")

        self.spinBox_rowDisp = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.spinBox_rowDisp.setGeometry(QtCore.QRect(410, 90, 47, 31))
        self.spinBox_rowDisp.setFont(font)
        self.spinBox_rowDisp.setMinimum(0)
        self.spinBox_rowDisp.setMaximum(500)
        #self.spinBox_rowDisp.setProperty("value", 0)
        self.spinBox_rowDisp.setObjectName("spinBox_rowDisp")

        self.spinBox_colDisp = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.spinBox_colDisp.setGeometry(QtCore.QRect(410, 130, 47, 31))
        self.spinBox_colDisp.setFont(font)
        self.spinBox_colDisp.setMinimum(0)
        self.spinBox_colDisp.setMaximum(500)
        #self.spinBox_colDisp.setProperty("value", 0)
        self.spinBox_colDisp.setObjectName("spinBox_colDisp")

        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(10, 170, 160, 31))
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")

        self.label_dippos = QtWidgets.QLabel(self.centralwidget)
        self.label_dippos.setGeometry(QtCore.QRect(10, 220, 160, 31))
        self.label_dippos.setFont(font)
        self.label_dippos.setObjectName("label_dippos")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(130, 380, 75, 31))
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_save = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_save.setGeometry(QtCore.QRect(10, 380, 101, 31))
        self.pushButton_save.setFont(font)
        self.pushButton_save.setObjectName("pushButton_save")
        ModifyWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ModifyWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 531, 22))
        self.menubar.setObjectName("menubar")
        ModifyWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ModifyWindow)
        self.statusbar.setObjectName("statusbar")
        ModifyWindow.setStatusBar(self.statusbar)

        self.label_rown = QtWidgets.QLabel(self.centralwidget)
        self.label_rown.setGeometry(QtCore.QRect(10, 90, 160, 31))
        self.label_rown.setFont(font)
        self.label_rown.setObjectName("label_rown")

        self.label_coln = QtWidgets.QLabel(self.centralwidget)
        self.label_coln.setGeometry(QtCore.QRect(10, 130, 160, 31))
        self.label_coln.setFont(font)
        self.label_coln.setObjectName("label_coln")

        self.retranslateUi(ModifyWindow)
        QtCore.QMetaObject.connectSlotsByName(ModifyWindow)

        if self.spinBox_rown.text() == '':
            rowNum = 2
        else:
            rowNum = int(self.spinBox_rown.text())

        if self.spinBox_coln.text() == '':
            colNum = 3
        else:
            colNum = int(self.spinBox_coln.text())

        self.rowNum = rowNum
        self.colNum = colNum

        if self.spinBox_pdd.text() == '':
            pdd = 10
        else:
            pdd = int(self.spinBox_pdd.text())
        if self.spinBox_pdu.text() == '':
            pdu = 10
        else:
            pdu = int(self.spinBox_pdu.text())

        self.pdd = pdd
        self.pdu = pdu

        if self.spinBox_ppd.text() == '':
            ppd = 38
        else:
            ppd = int(self.spinBox_ppd.text())
        if self.spinBox_ppu.text() == '':
            ppu = 100
        else:
            ppu = int(self.spinBox_ppu.text())

        self.ppd = ppd
        self.ppu = ppu

        if self.spinBox_rowDisp.text() == '':
            rowDisp = 1.650
        else:
            rowDisp = float(self.spinBox_rowDisp.text())
        if self.spinBox_colDisp.text() == '':
            colDisp = 1.47
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

        if self.spinBox_dipPosx1.text() == '':
            dipPosx1 = 49
        else:
            dipPosx1 = float(self.spinBox_dipPosx1.text())*self.rowDisp
        if self.spinBox_dipPosy1.text() == '':
            dipPosy1 = 88.50
        else:
            dipPosy1 = float(self.spinBox_dipPosy1.text())*self.rowDisp

        self.dipPosx1 = dipPosx1
        self.dipPosy1 = dipPosy1

        if self.spinBox_dipPosx2.text() == '':
            dipPosx2 = 58
        else:
            dipPosx2 = float(self.spinBox_dipPosx2.text())*self.rowDisp
        if self.spinBox_dipPosy2.text() == '':
            dipPosy2 = 88.50
        else:
            dipPosy2 = float(self.spinBox_dipPosy2.text())*self.rowDisp

        self.dipPosx2 = dipPosx2
        self.dipPosy2 = dipPosy2

        if self.spinBox_dipPosx3.text() == '':
            dipPosx3 = 67
        else:
            dipPosx3 = float(self.spinBox_dipPosx3.text())*self.rowDisp
        if self.spinBox_dipPosy2.text() == '':
            dipPosy3 = 88.50
        else:
            dipPosy3 = float(self.spinBox_dipPosy3.text())*self.rowDisp

        self.dipPosx3 = dipPosx3
        self.dipPosy3 = dipPosy3

        self.initialize_saved_values(ModifyWindow)

    def initialize_saved_values(self, ModifyWindow):

        self.spinBox_pdd.setProperty("value", self.pdd)
        self.spinBox_pdu.setProperty("value", self.pdu)
        self.spinBox_ppd.setProperty("value", self.ppd)
        self.spinBox_ppu.setProperty("value", self.ppu)
        self.spinBox_rown.setProperty("value", self.rowNum)
        self.spinBox_coln.setProperty("value", self.colNum)
        self.spinBox_px.setProperty("value", self.startpx)
        self.spinBox_py.setProperty("value", self.startpy)
        self.spinBox_rowDisp.setProperty("value", self.rowDisp)
        self.spinBox_colDisp.setProperty("value", self.colDisp)
        self.spinBox_dipPosx1.setProperty("value", self.dipPosx1)
        self.spinBox_dipPosy1.setProperty("value", self.dipPosy1)
        self.spinBox_dipPosx2.setProperty("value", self.dipPosx2)
        self.spinBox_dipPosy2.setProperty("value", self.dipPosy2)
        self.spinBox_dipPosx3.setProperty("value", self.dipPosx3)
        self.spinBox_dipPosy3.setProperty("value", self.dipPosy3)


    #def initialize_saved_values(self, ModifyWindow):
#
#        self.rowNum = rowNum
#        self.colNum = colNum
#        self.pdd = pdd
#        self.pdu = pdu
#        self.rowDisp = rowDisp
#        self.colDisp = colDisp
#        self.startpx = startpx
#        self.startpy = startpy
#
#        self.spinBox_pdd.setProperty("value", self.pdd)
#        self.spinBox_pdu.setProperty("value", self.pdu)
#        self.spinBox_rown.setProperty("value", self.rowNum)
#        self.spinBox_coln.setProperty("value", self.colNum)
#        self.spinBox_px.setProperty("value", self.startpx)
#        self.spinBox_py.setProperty("value", self.startpy)
#        self.spinBox_rowDisp.setProperty("value", self.rowDisp)
#        self.spinBox_colDisp.setProperty("value", self.colDisp)

    def retranslateUi(self, ModifyWindow):
        _translate = QtCore.QCoreApplication.translate
        ModifyWindow.setWindowTitle(_translate("ModifyWindow", "Modify"))
        self.label.setText(_translate("ModifyWindow", "AxiDraw Spotting Experiment"))
        self.label_2.setText(_translate("ModifyWindow", "Experiment Modification Window"))
        self.label_rown.setText(_translate("ModifyWindow", "Number of Rows: "))
        self.label_coln.setText(_translate("ModifyWindow", "Number of Columns: "))
        self.label_10.setText(_translate("ModifyWindow", "Starting Position (r,c):"))
        self.label_dippos.setText(_translate("ModifyWindow", "Dip Position (1,2,3):"))
        self.pushButton.setText(_translate("ModifyWindow", "Return"))
        self.pushButton_save.setText(_translate("ModifyWindow", "Save Settings"))

        self.label_pdd.setText(_translate("SpottingExp", "Pen Delay Down (ms)"))
        self.label_pdu.setText(_translate("SpottingExp", "Pen Delay Up (ms)"))
        self.label_ppu.setText(_translate("SpottingExp", "Pen Position Up (%)"))
        self.label_ppd.setText(_translate("SpottingExp", "Pen Position Down (%)"))

        self.label_rowDisp.setText(_translate("SpottingExp", "Row Displacement: "))
        self.label_colDisp.setText(_translate("SpottingExp", "Column Displacement: "))

        self.pushButton_save.clicked.connect(self.saveSettings)

    def saveSettings(self):

        rowNum = int(self.spinBox_rown.text())
        colNum = int(self.spinBox_coln.text())

        pdd = int(self.spinBox_pdd.text())
        pdu = int(self.spinBox_pdu.text())

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

        #self.rowNum = float(self.spinBox_rown.text())
        #self.colNum = float(self.spinBox_coln.text())

        #self.pdd = float(self.spinBox_pdd.text())
        #self.pdu = float(self.spinBox_pdu.text())

        #self.rowDisp = float(self.spinBox_rowDisp.text())/100
        #self.colDisp = float(self.spinBox_colDisp.text())/100

        #self.startpx = float(self.spinBox_px.text())*self.colDisp
        #self.startpy = float(self.spinBox_py.text())*self.rowDisp

        self.spinBox_pdd.setProperty("value", pdd)
        self.spinBox_pdu.setProperty("value", pdu)
        self.spinBox_ppd.setProperty("value", ppd)
        self.spinBox_ppu.setProperty("value", ppu)
        self.spinBox_rown.setProperty("value", rowNum)
        self.spinBox_coln.setProperty("value", colNum)
        self.spinBox_px.setProperty("value", startpx/self.colDisp)
        self.spinBox_py.setProperty("value", startpy/self.rowDisp)
        self.spinBox_rowDisp.setProperty("value", rowDisp)
        self.spinBox_colDisp.setProperty("value", colDisp)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ModifyWindow = QtWidgets.QMainWindow()
    ui = Ui_ModifyWindow()
    ui.setupUi(ModifyWindow)
    ModifyWindow.show()
    sys.exit(app.exec_())
