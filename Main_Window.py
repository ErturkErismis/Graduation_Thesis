# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main_Window_Design.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(741, 636)
        MainWindow.setStyleSheet("QMainWindow{\n"
"background-color:    #CC9900;\n"
"}\n"
"QPushButton {\n"
"    background-color: palegoldenrod;\n"
"    border-width: 2px;\n"
"    border-color: darkkhaki;\n"
"    border-style: solid;\n"
"    border-radius: 5;\n"
"    padding: 3px;\n"
"    min-width: 9ex;\n"
"    min-height: 2.5ex;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"   background-color: khaki;\n"
"}\n"
"\n"
"/* Increase the padding, so the text is shifted when the button is\n"
"   pressed. */\n"
"QPushButton:pressed {\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    background-color: #006600;\n"
"}\n"
"\n"
"QLabel, QAbstractButton {\n"
"    font: bold;\n"
"}\n"
"\n"
"/* Mark mandatory fields with a brownish color. */\n"
".mandatory {\n"
"    color: brown;\n"
"}\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Audi_winbutton = QtWidgets.QPushButton(self.centralwidget)
        self.Audi_winbutton.setGeometry(QtCore.QRect(170, 190, 171, 131))
        self.Audi_winbutton.setObjectName("Audi_winbutton")
        self.Merc_winbutton = QtWidgets.QPushButton(self.centralwidget)
        self.Merc_winbutton.setGeometry(QtCore.QRect(390, 190, 181, 131))
        self.Merc_winbutton.setObjectName("Merc_winbutton")
        self.Ford_winbutton = QtWidgets.QPushButton(self.centralwidget)
        self.Ford_winbutton.setGeometry(QtCore.QRect(170, 340, 171, 131))
        self.Ford_winbutton.setObjectName("Ford_winbutton")
        self.Bmw_winbutton = QtWidgets.QPushButton(self.centralwidget)
        self.Bmw_winbutton.setGeometry(QtCore.QRect(390, 340, 181, 131))
        self.Bmw_winbutton.setObjectName("Bmw_winbutton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 110, 351, 51))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 741, 29))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Car Price Prediction"))
        self.Audi_winbutton.setText(_translate("MainWindow", "AUDİ"))
        self.Merc_winbutton.setText(_translate("MainWindow", "MERCEDES"))
        self.Ford_winbutton.setText(_translate("MainWindow", "FORD"))
        self.Bmw_winbutton.setText(_translate("MainWindow", "BMW"))
        self.label.setText(_translate("MainWindow", "                   Please,Select The Brand"))

