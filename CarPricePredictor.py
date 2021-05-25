import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from Main_Window import *
from Audi_Window import *
from Bmw_Window import *
from Merc_Window import *
from Ford_Window import *

#----------------------Create App-------------------#
#---------------------------------------------------------#
Uygulama=QApplication(sys.argv)
penAna=QMainWindow()
ui=Ui_MainWindow()
ui.setupUi(penAna)
penAna.show()

penAudi=QWidget()
ui2=Ui_Form()
ui2.setupUi(penAudi)

penBmw=QWidget()
ui3=Ui_BMW()
ui3.setupUi(penBmw)

penMerc=QWidget()
ui4=Ui_Form3()
ui4.setupUi(penMerc)

penFord=QWidget()
ui5=Ui_Form2()
ui5.setupUi(penFord)



#----------------------Create Windows-------------------#
#---------------------------------------------------------#
def Audi_Win():
    penAudi.show()

def Bmw_Win():
    penBmw.show()

def Merc_Win():
    penMerc.show()

def Ford_Win():
    penFord.show()

#----------------------ClearButtons -------------------#
#---------------------------------------------------------#
def Audi_Clear():
    a=" "
    ui2.comboBox.setCurrentIndex(-1)
    ui2.lineEdit.clear()
    ui2.comboBox_2.setCurrentIndex(-1)
    ui2.lineEdit_2.clear()
    ui2.comboBox_3.setCurrentIndex(-1)
    ui2.lineEdit_3.clear()
    ui2.lineEdit_4.clear()
    ui2.lineEdit_5.clear()
    ui2.lineEdit_6.clear()

def Bmw_Clear():
    ui3.Bmw_Model_Combo.setCurrentIndex(-1)
    ui3.Bmw_Year_lineEdit.clear()
    ui3.Bmw_Trans_comboBox.setCurrentIndex(-1)
    ui3.Bmw_mileage_lineEdit.clear()
    ui3.Bmw_ftype_comboBox.setCurrentIndex(-1)
    ui3.Bmw_tax_lineEdit.clear()
    ui3.Bmw_mpg_lineEdit.clear()
    ui3.Bmw_enginesize_lineEdit.clear()
    ui3.Bmw_price_lineEdit.clear()

def Merc_Clear():

    ui4.Merc_Model_Combo.setCurrentIndex(-1)
    ui4.Merc_Year_lineEdit.clear()
    ui4.Merc_Trans_comboBox.setCurrentIndex(-1)
    ui4.Merc_mileage_lineEdit.clear()
    ui4.Merc_ftype_comboBox.setCurrentIndex(-1)
    ui4.Merc_tax_lineEdit.clear()
    ui4.Merc_mpg_lineEdit.clear()
    ui4.Merc_enginesize_lineEdit.clear()
    ui4.Merc_price_lineEdit.clear()

def Ford_Clear():

    ui5.Ford_Model_Combo.setCurrentIndex(-1)
    ui5.Ford_Year_lineEdit.clear()
    ui5.Ford_Trans_comboBox.setCurrentIndex(-1)
    ui5.Ford_mileage_lineEdit.clear()
    ui5.Ford_ftype_comboBox.setCurrentIndex(-1)
    ui5.Ford_tax_lineEdit.clear()
    ui5.Ford_mpg_lineEdit.clear()
    ui5.Ford_enginesize_lineEdit.clear()
    ui5.Merc_price_lineEdit.clear()







#----------------------Signal-Slot-------------------#
#---------------------------------------------------------#
ui.Audi_winbutton.clicked.connect(Audi_Win)
ui.Ford_winbutton.clicked.connect(Ford_Win)
ui.Bmw_winbutton.clicked.connect(Bmw_Win)
ui.Merc_winbutton.clicked.connect(Merc_Win)
ui2.pushButton_2.clicked.connect(Audi_Clear)
ui3.Bmw_Clear_pushButton.clicked.connect(Bmw_Clear)
ui4.Merc_Clear_pushButton.clicked.connect(Merc_Clear)
ui5.Ford_Clear_pushButton.clicked.connect(Ford_Clear)



sys.exit(Uygulama.exec_())
