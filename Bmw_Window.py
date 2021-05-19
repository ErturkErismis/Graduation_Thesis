# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Bmw_Window_Design.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_BMW(object):
    def setupUi(self, BMW):
        BMW.setObjectName("BMW")
        BMW.resize(942, 733)
        BMW.setStyleSheet("QWidget{\n"
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
        self.label = QtWidgets.QLabel(BMW)
        self.label.setGeometry(QtCore.QRect(50, 110, 111, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(BMW)
        self.label_2.setGeometry(QtCore.QRect(50, 170, 111, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(BMW)
        self.label_3.setGeometry(QtCore.QRect(40, 230, 131, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(BMW)
        self.label_4.setGeometry(QtCore.QRect(50, 290, 111, 31))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(BMW)
        self.label_5.setGeometry(QtCore.QRect(50, 350, 111, 31))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(BMW)
        self.label_6.setGeometry(QtCore.QRect(50, 410, 111, 31))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(BMW)
        self.label_7.setGeometry(QtCore.QRect(50, 470, 111, 31))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(BMW)
        self.label_8.setGeometry(QtCore.QRect(50, 530, 111, 31))
        self.label_8.setObjectName("label_8")
        self.Bmw_Model_Combo = QtWidgets.QComboBox(BMW)
        self.Bmw_Model_Combo.setGeometry(QtCore.QRect(180, 110, 131, 24))
        self.Bmw_Model_Combo.setToolTipDuration(0)
        self.Bmw_Model_Combo.setCurrentText("")
        self.Bmw_Model_Combo.setObjectName("Bmw_Model_Combo")
        self.Bmw_Model_Combo.addItem("")
        self.Bmw_Model_Combo.addItem("")
        self.Bmw_Model_Combo.addItem("")
        self.Bmw_Model_Combo.addItem("")
        self.Bmw_Model_Combo.addItem("")
        self.Bmw_Model_Combo.addItem("")
        self.Bmw_Model_Combo.addItem("")
        self.Bmw_Model_Combo.addItem("")
        self.Bmw_Model_Combo.addItem("")
        self.Bmw_Model_Combo.addItem("")
        self.Bmw_Model_Combo.addItem("")
        self.Bmw_Model_Combo.addItem("")
        self.Bmw_Model_Combo.addItem("")
        self.Bmw_Model_Combo.addItem("")
        self.Bmw_Model_Combo.addItem("")
        self.Bmw_Model_Combo.addItem("")
        self.Bmw_Model_Combo.addItem("")
        self.Bmw_Model_Combo.addItem("")
        self.Bmw_Model_Combo.addItem("")
        self.Bmw_Model_Combo.addItem("")
        self.Bmw_Model_Combo.addItem("")
        self.Bmw_Model_Combo.addItem("")
        self.Bmw_Model_Combo.addItem("")
        self.Bmw_Model_Combo.addItem("")
        self.Bmw_Trans_comboBox = QtWidgets.QComboBox(BMW)
        self.Bmw_Trans_comboBox.setGeometry(QtCore.QRect(180, 230, 131, 24))
        self.Bmw_Trans_comboBox.setToolTipDuration(0)
        self.Bmw_Trans_comboBox.setObjectName("Bmw_Trans_comboBox")
        self.Bmw_Trans_comboBox.addItem("")
        self.Bmw_Trans_comboBox.addItem("")
        self.Bmw_Trans_comboBox.addItem("")
        self.Bmw_ftype_comboBox = QtWidgets.QComboBox(BMW)
        self.Bmw_ftype_comboBox.setGeometry(QtCore.QRect(180, 350, 131, 24))
        self.Bmw_ftype_comboBox.setToolTipDuration(0)
        self.Bmw_ftype_comboBox.setObjectName("Bmw_ftype_comboBox")
        self.Bmw_ftype_comboBox.addItem("")
        self.Bmw_ftype_comboBox.addItem("")
        self.Bmw_ftype_comboBox.addItem("")
        self.Bmw_ftype_comboBox.addItem("")
        self.Bmw_ftype_comboBox.addItem("")
        self.Bmw_Year_lineEdit = QtWidgets.QLineEdit(BMW)
        self.Bmw_Year_lineEdit.setGeometry(QtCore.QRect(180, 170, 131, 31))
        self.Bmw_Year_lineEdit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.Bmw_Year_lineEdit.setReadOnly(False)
        self.Bmw_Year_lineEdit.setObjectName("Bmw_Year_lineEdit")
        self.Bmw_mileage_lineEdit = QtWidgets.QLineEdit(BMW)
        self.Bmw_mileage_lineEdit.setGeometry(QtCore.QRect(180, 290, 131, 31))
        self.Bmw_mileage_lineEdit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.Bmw_mileage_lineEdit.setReadOnly(False)
        self.Bmw_mileage_lineEdit.setObjectName("Bmw_mileage_lineEdit")
        self.Bmw_tax_lineEdit = QtWidgets.QLineEdit(BMW)
        self.Bmw_tax_lineEdit.setGeometry(QtCore.QRect(180, 410, 131, 31))
        self.Bmw_tax_lineEdit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.Bmw_tax_lineEdit.setReadOnly(False)
        self.Bmw_tax_lineEdit.setObjectName("Bmw_tax_lineEdit")
        self.Bmw_mpg_lineEdit = QtWidgets.QLineEdit(BMW)
        self.Bmw_mpg_lineEdit.setGeometry(QtCore.QRect(180, 470, 131, 31))
        self.Bmw_mpg_lineEdit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.Bmw_mpg_lineEdit.setReadOnly(False)
        self.Bmw_mpg_lineEdit.setObjectName("Bmw_mpg_lineEdit")
        self.Bmw_enginesize_lineEdit = QtWidgets.QLineEdit(BMW)
        self.Bmw_enginesize_lineEdit.setGeometry(QtCore.QRect(180, 530, 131, 31))
        self.Bmw_enginesize_lineEdit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.Bmw_enginesize_lineEdit.setReadOnly(False)
        self.Bmw_enginesize_lineEdit.setObjectName("Bmw_enginesize_lineEdit")
        self.Bmw_calculate_pushButton = QtWidgets.QPushButton(BMW)
        self.Bmw_calculate_pushButton.setGeometry(QtCore.QRect(50, 610, 151, 71))
        self.Bmw_calculate_pushButton.setObjectName("Bmw_calculate_pushButton")
        self.Bmw_Clear_pushButton = QtWidgets.QPushButton(BMW)
        self.Bmw_Clear_pushButton.setGeometry(QtCore.QRect(260, 610, 151, 71))
        self.Bmw_Clear_pushButton.setObjectName("Bmw_Clear_pushButton")
        self.label_9 = QtWidgets.QLabel(BMW)
        self.label_9.setGeometry(QtCore.QRect(450, 480, 111, 31))
        self.label_9.setObjectName("label_9")
        self.Bmw_price_lineEdit = QtWidgets.QLineEdit(BMW)
        self.Bmw_price_lineEdit.setGeometry(QtCore.QRect(520, 480, 131, 31))
        self.Bmw_price_lineEdit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.Bmw_price_lineEdit.setReadOnly(False)
        self.Bmw_price_lineEdit.setObjectName("Bmw_price_lineEdit")
        self.label_11 = QtWidgets.QLabel(BMW)
        self.label_11.setGeometry(QtCore.QRect(660, 490, 31, 18))
        self.label_11.setObjectName("label_11")
        self.label_10 = QtWidgets.QLabel(BMW)
        self.label_10.setGeometry(QtCore.QRect(450, 360, 471, 111))
        self.label_10.setObjectName("label_10")
        self.textEdit = QtWidgets.QTextEdit(BMW)
        self.textEdit.setEnabled(False)
        self.textEdit.setGeometry(QtCore.QRect(490, 80, 381, 281))
        self.textEdit.setStyleSheet("border-image: url(:/newPrefix/icons/BmwPP.jpg);")
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(BMW)
        self.Bmw_Model_Combo.setCurrentIndex(-1)
        self.Bmw_Trans_comboBox.setCurrentIndex(-1)
        self.Bmw_ftype_comboBox.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(BMW)

    def retranslateUi(self, BMW):
        _translate = QtCore.QCoreApplication.translate
        BMW.setWindowTitle(_translate("BMW", "BMW"))
        self.label.setText(_translate("BMW", "MODEL:"))
        self.label_2.setText(_translate("BMW", "YEAR:"))
        self.label_3.setText(_translate("BMW", "TRANSMİSSİON:"))
        self.label_4.setText(_translate("BMW", "MİLE AGE:"))
        self.label_5.setText(_translate("BMW", "FUEL TYPE:"))
        self.label_6.setText(_translate("BMW", "TAX:"))
        self.label_7.setText(_translate("BMW", "MPG:"))
        self.label_8.setText(_translate("BMW", "ENGİNE SİZE:"))
        self.Bmw_Model_Combo.setItemText(0, _translate("BMW", "1 Series"))
        self.Bmw_Model_Combo.setItemText(1, _translate("BMW", "2 Series"))
        self.Bmw_Model_Combo.setItemText(2, _translate("BMW", "3 Series"))
        self.Bmw_Model_Combo.setItemText(3, _translate("BMW", "4 Series"))
        self.Bmw_Model_Combo.setItemText(4, _translate("BMW", "5 Series"))
        self.Bmw_Model_Combo.setItemText(5, _translate("BMW", "6 Series"))
        self.Bmw_Model_Combo.setItemText(6, _translate("BMW", "7 Series"))
        self.Bmw_Model_Combo.setItemText(7, _translate("BMW", "8 Series"))
        self.Bmw_Model_Combo.setItemText(8, _translate("BMW", "M2"))
        self.Bmw_Model_Combo.setItemText(9, _translate("BMW", "M3"))
        self.Bmw_Model_Combo.setItemText(10, _translate("BMW", "M4"))
        self.Bmw_Model_Combo.setItemText(11, _translate("BMW", "M5"))
        self.Bmw_Model_Combo.setItemText(12, _translate("BMW", "M6"))
        self.Bmw_Model_Combo.setItemText(13, _translate("BMW", "X1"))
        self.Bmw_Model_Combo.setItemText(14, _translate("BMW", "X2"))
        self.Bmw_Model_Combo.setItemText(15, _translate("BMW", "X3"))
        self.Bmw_Model_Combo.setItemText(16, _translate("BMW", "X4"))
        self.Bmw_Model_Combo.setItemText(17, _translate("BMW", "X5"))
        self.Bmw_Model_Combo.setItemText(18, _translate("BMW", "X6"))
        self.Bmw_Model_Combo.setItemText(19, _translate("BMW", "X7"))
        self.Bmw_Model_Combo.setItemText(20, _translate("BMW", "Z3"))
        self.Bmw_Model_Combo.setItemText(21, _translate("BMW", "Z4"))
        self.Bmw_Model_Combo.setItemText(22, _translate("BMW", "İ3"))
        self.Bmw_Model_Combo.setItemText(23, _translate("BMW", "İ8"))
        self.Bmw_Trans_comboBox.setItemText(0, _translate("BMW", "AUTOMATİC"))
        self.Bmw_Trans_comboBox.setItemText(1, _translate("BMW", "MANUEL"))
        self.Bmw_Trans_comboBox.setItemText(2, _translate("BMW", "SEMİ-AUTO"))
        self.Bmw_ftype_comboBox.setItemText(0, _translate("BMW", "DİESEL"))
        self.Bmw_ftype_comboBox.setItemText(1, _translate("BMW", "ELECTRİC"))
        self.Bmw_ftype_comboBox.setItemText(2, _translate("BMW", "HYBRİD"))
        self.Bmw_ftype_comboBox.setItemText(3, _translate("BMW", "OTHER"))
        self.Bmw_ftype_comboBox.setItemText(4, _translate("BMW", "PETROL"))
        self.Bmw_calculate_pushButton.setText(_translate("BMW", "CALCULATE"))
        self.Bmw_Clear_pushButton.setText(_translate("BMW", "CLEAR"))
        self.label_9.setText(_translate("BMW", "PRİCE:"))
        self.label_11.setText(_translate("BMW", "£"))
        self.label_10.setText(_translate("BMW", "You can sell your vehicle up or down for 3000£ from the result."))

#import icons_rc
