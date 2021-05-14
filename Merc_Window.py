# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Merc_Window_Design.ui'
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
        self.label_3.setGeometry(QtCore.QRect(40, 230, 131, 31))
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
        self.Merc_Model_Combo = QtWidgets.QComboBox(Form)
        self.Merc_Model_Combo.setGeometry(QtCore.QRect(180, 110, 131, 24))
        self.Merc_Model_Combo.setToolTipDuration(0)
        self.Merc_Model_Combo.setCurrentText("")
        self.Merc_Model_Combo.setObjectName("Merc_Model_Combo")
        self.Merc_Model_Combo.addItem("")
        self.Merc_Model_Combo.addItem("")
        self.Merc_Model_Combo.addItem("")
        self.Merc_Model_Combo.addItem("")
        self.Merc_Model_Combo.addItem("")
        self.Merc_Model_Combo.addItem("")
        self.Merc_Model_Combo.addItem("")
        self.Merc_Model_Combo.addItem("")
        self.Merc_Model_Combo.addItem("")
        self.Merc_Model_Combo.addItem("")
        self.Merc_Model_Combo.addItem("")
        self.Merc_Model_Combo.addItem("")
        self.Merc_Model_Combo.addItem("")
        self.Merc_Model_Combo.addItem("")
        self.Merc_Model_Combo.addItem("")
        self.Merc_Model_Combo.addItem("")
        self.Merc_Model_Combo.addItem("")
        self.Merc_Model_Combo.addItem("")
        self.Merc_Model_Combo.addItem("")
        self.Merc_Model_Combo.addItem("")
        self.Merc_Model_Combo.addItem("")
        self.Merc_Model_Combo.addItem("")
        self.Merc_Model_Combo.addItem("")
        self.Merc_Model_Combo.addItem("")
        self.Merc_Model_Combo.addItem("")
        self.Merc_Model_Combo.addItem("")
        self.Merc_Model_Combo.addItem("")
        self.Merc_Year_lineEdit = QtWidgets.QLineEdit(Form)
        self.Merc_Year_lineEdit.setGeometry(QtCore.QRect(180, 170, 131, 31))
        self.Merc_Year_lineEdit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.Merc_Year_lineEdit.setReadOnly(False)
        self.Merc_Year_lineEdit.setObjectName("Merc_Year_lineEdit")
        self.Merc_Trans_comboBox = QtWidgets.QComboBox(Form)
        self.Merc_Trans_comboBox.setGeometry(QtCore.QRect(180, 230, 131, 24))
        self.Merc_Trans_comboBox.setToolTipDuration(0)
        self.Merc_Trans_comboBox.setObjectName("Merc_Trans_comboBox")
        self.Merc_Trans_comboBox.addItem("")
        self.Merc_Trans_comboBox.addItem("")
        self.Merc_Trans_comboBox.addItem("")
        self.Merc_Trans_comboBox.addItem("")
        self.Merc_mileage_lineEdit = QtWidgets.QLineEdit(Form)
        self.Merc_mileage_lineEdit.setGeometry(QtCore.QRect(180, 290, 131, 31))
        self.Merc_mileage_lineEdit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.Merc_mileage_lineEdit.setReadOnly(False)
        self.Merc_mileage_lineEdit.setObjectName("Merc_mileage_lineEdit")
        self.Merc_ftype_comboBox = QtWidgets.QComboBox(Form)
        self.Merc_ftype_comboBox.setGeometry(QtCore.QRect(180, 350, 131, 24))
        self.Merc_ftype_comboBox.setToolTipDuration(0)
        self.Merc_ftype_comboBox.setObjectName("Merc_ftype_comboBox")
        self.Merc_ftype_comboBox.addItem("")
        self.Merc_ftype_comboBox.addItem("")
        self.Merc_ftype_comboBox.addItem("")
        self.Merc_ftype_comboBox.addItem("")
        self.Merc_tax_lineEdit = QtWidgets.QLineEdit(Form)
        self.Merc_tax_lineEdit.setGeometry(QtCore.QRect(180, 410, 131, 31))
        self.Merc_tax_lineEdit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.Merc_tax_lineEdit.setReadOnly(False)
        self.Merc_tax_lineEdit.setObjectName("Merc_tax_lineEdit")
        self.Merc_mpg_lineEdit = QtWidgets.QLineEdit(Form)
        self.Merc_mpg_lineEdit.setGeometry(QtCore.QRect(180, 470, 131, 31))
        self.Merc_mpg_lineEdit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.Merc_mpg_lineEdit.setReadOnly(False)
        self.Merc_mpg_lineEdit.setObjectName("Merc_mpg_lineEdit")
        self.Merc_enginesize_lineEdit = QtWidgets.QLineEdit(Form)
        self.Merc_enginesize_lineEdit.setGeometry(QtCore.QRect(180, 530, 131, 31))
        self.Merc_enginesize_lineEdit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.Merc_enginesize_lineEdit.setReadOnly(False)
        self.Merc_enginesize_lineEdit.setObjectName("Merc_enginesize_lineEdit")
        self.Merc_calculate_pushButton = QtWidgets.QPushButton(Form)
        self.Merc_calculate_pushButton.setGeometry(QtCore.QRect(50, 610, 151, 71))
        self.Merc_calculate_pushButton.setObjectName("Merc_calculate_pushButton")
        self.Merc_Clear_pushButton = QtWidgets.QPushButton(Form)
        self.Merc_Clear_pushButton.setGeometry(QtCore.QRect(260, 610, 151, 71))
        self.Merc_Clear_pushButton.setObjectName("Merc_Clear_pushButton")
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(450, 360, 471, 111))
        self.label_10.setObjectName("label_10")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(450, 480, 111, 31))
        self.label_9.setObjectName("label_9")
        self.Merc_price_lineEdit = QtWidgets.QLineEdit(Form)
        self.Merc_price_lineEdit.setGeometry(QtCore.QRect(520, 480, 131, 31))
        self.Merc_price_lineEdit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.Merc_price_lineEdit.setReadOnly(False)
        self.Merc_price_lineEdit.setObjectName("Merc_price_lineEdit")
        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setGeometry(QtCore.QRect(660, 490, 31, 18))
        self.label_11.setObjectName("label_11")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(490, 80, 381, 281))
        self.textEdit.setStyleSheet("border-image: url(:/newPrefix/icons/MercPP.png);")
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(Form)
        self.Merc_Model_Combo.setCurrentIndex(-1)
        self.Merc_Trans_comboBox.setCurrentIndex(-1)
        self.Merc_ftype_comboBox.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "MERCEDES"))
        self.label.setText(_translate("Form", "MODEL:"))
        self.label_2.setText(_translate("Form", "YEAR:"))
        self.label_3.setText(_translate("Form", "TRANSMİSSİON:"))
        self.label_4.setText(_translate("Form", "MİLE AGE:"))
        self.label_5.setText(_translate("Form", "FUEL TYPE:"))
        self.label_6.setText(_translate("Form", "TAX:"))
        self.label_7.setText(_translate("Form", "MPG:"))
        self.label_8.setText(_translate("Form", "ENGİNE SİZE:"))
        self.Merc_Model_Combo.setItemText(0, _translate("Form", "SLK"))
        self.Merc_Model_Combo.setItemText(1, _translate("Form", "S CLASS"))
        self.Merc_Model_Combo.setItemText(2, _translate("Form", "SL CLASS"))
        self.Merc_Model_Combo.setItemText(3, _translate("Form", "G CLASS"))
        self.Merc_Model_Combo.setItemText(4, _translate("Form", "GLE CLASS"))
        self.Merc_Model_Combo.setItemText(5, _translate("Form", "GLA CLASS"))
        self.Merc_Model_Combo.setItemText(6, _translate("Form", "A CLASS"))
        self.Merc_Model_Combo.setItemText(7, _translate("Form", "B CLASS"))
        self.Merc_Model_Combo.setItemText(8, _translate("Form", "GLC CLASS"))
        self.Merc_Model_Combo.setItemText(9, _translate("Form", "C CLASS"))
        self.Merc_Model_Combo.setItemText(10, _translate("Form", "E CLASS"))
        self.Merc_Model_Combo.setItemText(11, _translate("Form", "GL CLASS"))
        self.Merc_Model_Combo.setItemText(12, _translate("Form", "CLS CLASS"))
        self.Merc_Model_Combo.setItemText(13, _translate("Form", "CLC CLASS"))
        self.Merc_Model_Combo.setItemText(14, _translate("Form", "CLA CLASS"))
        self.Merc_Model_Combo.setItemText(15, _translate("Form", "V CLASS"))
        self.Merc_Model_Combo.setItemText(16, _translate("Form", "M CLASS"))
        self.Merc_Model_Combo.setItemText(17, _translate("Form", "CL CLASS"))
        self.Merc_Model_Combo.setItemText(18, _translate("Form", "GLS CLASS"))
        self.Merc_Model_Combo.setItemText(19, _translate("Form", "GLB CLASS"))
        self.Merc_Model_Combo.setItemText(20, _translate("Form", "X CLASS"))
        self.Merc_Model_Combo.setItemText(21, _translate("Form", "180"))
        self.Merc_Model_Combo.setItemText(22, _translate("Form", "CLK"))
        self.Merc_Model_Combo.setItemText(23, _translate("Form", "R CLASS"))
        self.Merc_Model_Combo.setItemText(24, _translate("Form", "230"))
        self.Merc_Model_Combo.setItemText(25, _translate("Form", "220"))
        self.Merc_Model_Combo.setItemText(26, _translate("Form", "200"))
        self.Merc_Trans_comboBox.setItemText(0, _translate("Form", "AUTOMATİC"))
        self.Merc_Trans_comboBox.setItemText(1, _translate("Form", "MANUEL"))
        self.Merc_Trans_comboBox.setItemText(2, _translate("Form", "OTHER"))
        self.Merc_Trans_comboBox.setItemText(3, _translate("Form", "SEMİ-AUTO"))
        self.Merc_ftype_comboBox.setItemText(0, _translate("Form", "DİESEL"))
        self.Merc_ftype_comboBox.setItemText(1, _translate("Form", "HYBRİD"))
        self.Merc_ftype_comboBox.setItemText(2, _translate("Form", "OTHER"))
        self.Merc_ftype_comboBox.setItemText(3, _translate("Form", "PETROL"))
        self.Merc_calculate_pushButton.setText(_translate("Form", "CALCULATE"))
        self.Merc_Clear_pushButton.setText(_translate("Form", "CLEAR"))
        self.label_10.setText(_translate("Form", "You can sell your vehicle up or down for 3000£ from the result."))
        self.label_9.setText(_translate("Form", "PRİCE:"))
        self.label_11.setText(_translate("Form", "£"))

import icons_rc
