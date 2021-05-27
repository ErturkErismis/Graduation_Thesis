# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ford_Window_Design.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form2(object):
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
        self.Ford_Model_Combo = QtWidgets.QComboBox(Form)
        self.Ford_Model_Combo.setGeometry(QtCore.QRect(180, 110, 131, 24))
        self.Ford_Model_Combo.setToolTipDuration(0)
        self.Ford_Model_Combo.setCurrentText("")
        self.Ford_Model_Combo.setObjectName("Ford_Model_Combo")
        self.Ford_Model_Combo.addItem("")
        self.Ford_Model_Combo.addItem("")
        self.Ford_Model_Combo.addItem("")
        self.Ford_Model_Combo.addItem("")
        self.Ford_Model_Combo.addItem("")
        self.Ford_Model_Combo.addItem("")
        self.Ford_Model_Combo.addItem("")
        self.Ford_Model_Combo.addItem("")
        self.Ford_Model_Combo.addItem("")
        self.Ford_Model_Combo.addItem("")
        self.Ford_Model_Combo.addItem("")
        self.Ford_Model_Combo.addItem("")
        self.Ford_Model_Combo.addItem("")
        self.Ford_Model_Combo.addItem("")
        self.Ford_Model_Combo.addItem("")
        self.Ford_Model_Combo.addItem("")
        self.Ford_Model_Combo.addItem("")
        self.Ford_Model_Combo.addItem("")
        self.Ford_Model_Combo.addItem("")
        self.Ford_Model_Combo.addItem("")
        self.Ford_Model_Combo.addItem("")
        self.Ford_Model_Combo.addItem("")
        self.Ford_Model_Combo.addItem("")
        self.Ford_Year_lineEdit = QtWidgets.QLineEdit(Form)
        self.Ford_Year_lineEdit.setGeometry(QtCore.QRect(180, 170, 131, 31))
        self.Ford_Year_lineEdit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.Ford_Year_lineEdit.setReadOnly(False)
        self.Ford_Year_lineEdit.setObjectName("Ford_Year_lineEdit")
        self.Ford_Trans_comboBox = QtWidgets.QComboBox(Form)
        self.Ford_Trans_comboBox.setGeometry(QtCore.QRect(180, 230, 131, 24))
        self.Ford_Trans_comboBox.setToolTipDuration(0)
        self.Ford_Trans_comboBox.setObjectName("Ford_Trans_comboBox")
        self.Ford_Trans_comboBox.addItem("")
        self.Ford_Trans_comboBox.addItem("")
        self.Ford_Trans_comboBox.addItem("")
        self.Ford_mileage_lineEdit = QtWidgets.QLineEdit(Form)
        self.Ford_mileage_lineEdit.setGeometry(QtCore.QRect(180, 290, 131, 31))
        self.Ford_mileage_lineEdit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.Ford_mileage_lineEdit.setReadOnly(False)
        self.Ford_mileage_lineEdit.setObjectName("Ford_mileage_lineEdit")
        self.Ford_ftype_comboBox = QtWidgets.QComboBox(Form)
        self.Ford_ftype_comboBox.setGeometry(QtCore.QRect(180, 350, 131, 24))
        self.Ford_ftype_comboBox.setToolTipDuration(0)
        self.Ford_ftype_comboBox.setObjectName("Ford_ftype_comboBox")
        self.Ford_ftype_comboBox.addItem("")
        self.Ford_ftype_comboBox.addItem("")
        self.Ford_ftype_comboBox.addItem("")
        self.Ford_ftype_comboBox.addItem("")
        self.Ford_ftype_comboBox.addItem("")
        self.Ford_tax_lineEdit = QtWidgets.QLineEdit(Form)
        self.Ford_tax_lineEdit.setGeometry(QtCore.QRect(180, 410, 131, 31))
        self.Ford_tax_lineEdit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.Ford_tax_lineEdit.setReadOnly(False)
        self.Ford_tax_lineEdit.setObjectName("Ford_tax_lineEdit")
        self.Ford_mpg_lineEdit = QtWidgets.QLineEdit(Form)
        self.Ford_mpg_lineEdit.setGeometry(QtCore.QRect(180, 470, 131, 31))
        self.Ford_mpg_lineEdit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.Ford_mpg_lineEdit.setReadOnly(False)
        self.Ford_mpg_lineEdit.setObjectName("Ford_mpg_lineEdit")
        self.Ford_enginesize_lineEdit = QtWidgets.QLineEdit(Form)
        self.Ford_enginesize_lineEdit.setGeometry(QtCore.QRect(180, 530, 131, 31))
        self.Ford_enginesize_lineEdit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.Ford_enginesize_lineEdit.setReadOnly(False)
        self.Ford_enginesize_lineEdit.setObjectName("Ford_enginesize_lineEdit")
        self.Ford_calculate_pushButton = QtWidgets.QPushButton(Form)
        self.Ford_calculate_pushButton.setGeometry(QtCore.QRect(50, 610, 151, 71))
        self.Ford_calculate_pushButton.setObjectName("Ford_calculate_pushButton")
        self.Ford_Clear_pushButton = QtWidgets.QPushButton(Form)
        self.Ford_Clear_pushButton.setGeometry(QtCore.QRect(260, 610, 151, 71))
        self.Ford_Clear_pushButton.setObjectName("Ford_Clear_pushButton")
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
        self.label_11.setGeometry(QtCore.QRect(660, 490, 31, 20))
        self.label_11.setObjectName("label_11")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(490, 80, 381, 281))
        self.textEdit.setStyleSheet("border-image: url(:/newPrefix/icons/FordPP.jpg);")
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(Form)
        self.Ford_Model_Combo.setCurrentIndex(-1)
        self.Ford_Trans_comboBox.setCurrentIndex(-1)
        self.Ford_ftype_comboBox.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "FORD"))
        self.label.setText(_translate("Form", "MODEL:"))
        self.label_2.setText(_translate("Form", "YEAR:"))
        self.label_3.setText(_translate("Form", "TRANSMİSSİON:"))
        self.label_4.setText(_translate("Form", "MİLE AGE:"))
        self.label_5.setText(_translate("Form", "FUEL TYPE:"))
        self.label_6.setText(_translate("Form", "TAX:"))
        self.label_7.setText(_translate("Form", "MPG:"))
        self.label_8.setText(_translate("Form", "ENGİNE SİZE:"))
        self.Ford_Model_Combo.setItemText(0, _translate("Form", "FİESTA"))
        self.Ford_Model_Combo.setItemText(1, _translate("Form", "FOCUS"))
        self.Ford_Model_Combo.setItemText(2, _translate("Form", "PUMA"))
        self.Ford_Model_Combo.setItemText(3, _translate("Form", "KUGA"))
        self.Ford_Model_Combo.setItemText(4, _translate("Form", "ECOSPORT"))
        self.Ford_Model_Combo.setItemText(5, _translate("Form", "C-MAX"))
        self.Ford_Model_Combo.setItemText(6, _translate("Form", "MONDEO"))
        self.Ford_Model_Combo.setItemText(7, _translate("Form", "KA+"))
        self.Ford_Model_Combo.setItemText(8, _translate("Form", "TOURNEO CUSTOM"))
        self.Ford_Model_Combo.setItemText(9, _translate("Form", "S-MAX"))
        self.Ford_Model_Combo.setItemText(10, _translate("Form", "B-MAX"))
        self.Ford_Model_Combo.setItemText(11, _translate("Form", "EDGE"))
        self.Ford_Model_Combo.setItemText(12, _translate("Form", "TOURNEO CONNECT"))
        self.Ford_Model_Combo.setItemText(13, _translate("Form", "GRAND C-MAX"))
        self.Ford_Model_Combo.setItemText(14, _translate("Form", "KA"))
        self.Ford_Model_Combo.setItemText(15, _translate("Form", "GALAXY"))
        self.Ford_Model_Combo.setItemText(16, _translate("Form", "MUSTANG"))
        self.Ford_Model_Combo.setItemText(17, _translate("Form", "GRAND TOURNEO CONNECT"))
        self.Ford_Model_Combo.setItemText(18, _translate("Form", "FUSİON"))
        self.Ford_Model_Combo.setItemText(19, _translate("Form", "RANGER"))
        self.Ford_Model_Combo.setItemText(20, _translate("Form", "STREETKA"))
        self.Ford_Model_Combo.setItemText(21, _translate("Form", "ESCORT"))
        self.Ford_Model_Combo.setItemText(22, _translate("Form", "TRANSİT TOURNEO"))
        self.Ford_Trans_comboBox.setItemText(0, _translate("Form", "AUTOMATİC"))
        self.Ford_Trans_comboBox.setItemText(1, _translate("Form", "MANUEL"))
        self.Ford_Trans_comboBox.setItemText(2, _translate("Form", "SEMİ-AUTO"))
        self.Ford_ftype_comboBox.setItemText(0, _translate("Form", "DİESEL"))
        self.Ford_ftype_comboBox.setItemText(1, _translate("Form", "HYBRİD"))
        self.Ford_ftype_comboBox.setItemText(2, _translate("Form", "OTHER"))
        self.Ford_ftype_comboBox.setItemText(3, _translate("Form", "PETROL"))
        self.Ford_ftype_comboBox.setItemText(4, _translate("Form", "ELECTRİC"))
        self.Ford_calculate_pushButton.setText(_translate("Form", "CALCULATE"))
        self.Ford_Clear_pushButton.setText(_translate("Form", "CLEAR"))
        self.label_10.setText(_translate("Form", "You can sell your vehicle up or down for 3000£ from the result."))
        self.label_9.setText(_translate("Form", "PRİCE:"))
        self.label_11.setText(_translate("Form", "£"))

import icons_rc
