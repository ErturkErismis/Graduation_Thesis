# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Audi_Window_Design.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(942, 733)
        Form.setStyleSheet("QWidget{\n"
"background-color:    #00ff7f;\n"
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
"QComboBox, QLineEdit, QSpinBox, QTextEdit, QListView {\n"
"   background-color: cornsilk;\n"
"   selection-color: #0a214c; \n"
"   selection-background-color: #C19A6B;\n"
"}\n"
"")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(50, 110, 111, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(50, 170, 111, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(50, 230, 121, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(50, 290, 111, 31))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(50, 350, 111, 31))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(50, 410, 111, 31))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(50, 470, 111, 31))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(50, 530, 111, 31))
        self.label_8.setObjectName("label_8")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(180, 110, 131, 24))
        self.comboBox.setToolTipDuration(0)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(180, 170, 131, 31))
        self.lineEdit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit.setReadOnly(False)
        self.lineEdit.setObjectName("lineEdit")
        self.comboBox_2 = QtWidgets.QComboBox(Form)
        self.comboBox_2.setGeometry(QtCore.QRect(180, 230, 131, 24))
        self.comboBox_2.setToolTipDuration(0)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(180, 290, 131, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.comboBox_3 = QtWidgets.QComboBox(Form)
        self.comboBox_3.setGeometry(QtCore.QRect(180, 350, 131, 24))
        self.comboBox_3.setToolTipDuration(0)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(180, 410, 131, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(180, 470, 131, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(Form)
        self.lineEdit_5.setGeometry(QtCore.QRect(180, 530, 131, 31))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(450, 480, 111, 31))
        self.label_9.setObjectName("label_9")
        self.lineEdit_6 = QtWidgets.QLineEdit(Form)
        self.lineEdit_6.setGeometry(QtCore.QRect(520, 480, 131, 31))
        self.lineEdit_6.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_6.setReadOnly(False)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(50, 610, 151, 71))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(260, 610, 151, 71))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(450, 360, 471, 111))
        self.label_10.setObjectName("label_10")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(510, 120, 371, 241))
        self.textEdit.setStyleSheet("border-image: url(:/newPrefix/icons/AudiPP.jpg);")
        self.textEdit.setObjectName("textEdit")
        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setGeometry(QtCore.QRect(660, 490, 31, 18))
        self.label_11.setObjectName("label_11")

        self.retranslateUi(Form)
        self.comboBox.setCurrentIndex(-1)
        self.comboBox_2.setCurrentIndex(-1)
        self.comboBox_3.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Audi"))
        self.label.setText(_translate("Form", "MODEL:"))
        self.label_2.setText(_translate("Form", "YEAR:"))
        self.label_3.setText(_translate("Form", "TRANSMİSSİON:"))
        self.label_4.setText(_translate("Form", "MİLE AGE:"))
        self.label_5.setText(_translate("Form", "FUEL TYPE:"))
        self.label_6.setText(_translate("Form", "TAX:"))
        self.label_7.setText(_translate("Form", "MPG:"))
        self.label_8.setText(_translate("Form", "ENGİNE SİZE:"))
        self.comboBox.setItemText(0, _translate("Form", "A1"))
        self.comboBox.setItemText(1, _translate("Form", "A2"))
        self.comboBox.setItemText(2, _translate("Form", "A3"))
        self.comboBox.setItemText(3, _translate("Form", "A4"))
        self.comboBox.setItemText(4, _translate("Form", "A5"))
        self.comboBox.setItemText(5, _translate("Form", "A6"))
        self.comboBox.setItemText(6, _translate("Form", "A7"))
        self.comboBox.setItemText(7, _translate("Form", "A8"))
        self.comboBox.setItemText(8, _translate("Form", "Q2"))
        self.comboBox.setItemText(9, _translate("Form", "Q3"))
        self.comboBox.setItemText(10, _translate("Form", "Q5"))
        self.comboBox.setItemText(11, _translate("Form", "Q7"))
        self.comboBox.setItemText(12, _translate("Form", "Q8"))
        self.comboBox.setItemText(13, _translate("Form", "RS3"))
        self.comboBox.setItemText(14, _translate("Form", "RS4"))
        self.comboBox.setItemText(15, _translate("Form", "RS5"))
        self.comboBox.setItemText(16, _translate("Form", "RS6"))
        self.comboBox.setItemText(17, _translate("Form", "RS7"))
        self.comboBox.setItemText(18, _translate("Form", "S3"))
        self.comboBox.setItemText(19, _translate("Form", "S4"))
        self.comboBox.setItemText(20, _translate("Form", "S5"))
        self.comboBox.setItemText(21, _translate("Form", "S8"))
        self.comboBox.setItemText(22, _translate("Form", "SQ5"))
        self.comboBox.setItemText(23, _translate("Form", "SQ7"))
        self.comboBox.setItemText(24, _translate("Form", "R8"))
        self.comboBox.setItemText(25, _translate("Form", "TT"))
        self.comboBox_2.setItemText(0, _translate("Form", "AUTOMATİC"))
        self.comboBox_2.setItemText(1, _translate("Form", "MANUEL"))
        self.comboBox_2.setItemText(2, _translate("Form", "SEMİ-AUTO"))
        self.comboBox_3.setItemText(0, _translate("Form", "DİESEL"))
        self.comboBox_3.setItemText(1, _translate("Form", "PETROL"))
        self.comboBox_3.setItemText(2, _translate("Form", "HYBRİD"))
        self.label_9.setText(_translate("Form", "PRİCE:"))
        self.pushButton.setText(_translate("Form", "CALCULATE"))
        self.pushButton_2.setText(_translate("Form", "CLEAR"))
        self.label_10.setText(_translate("Form", "You can sell your vehicle up or down for 3000£ from the result."))
        self.label_11.setText(_translate("Form", "£"))

import icons_rc
