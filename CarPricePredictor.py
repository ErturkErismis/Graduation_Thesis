import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from Main_Window import *
from Audi_Window import *
from Bmw_Window import *
from Merc_Window import *
from Ford_Window import *
import tensorflow as tf
import numpy as np
import pandas as pd
import seaborn as sbn
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.metrics import mean_absolute_error,mean_squared_error
from tensorflow.keras.models import load_model
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
import joblib

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

#----------------------CalculateButtons -------------------#
#---------------------------------------------------------#

def Audi_Calculate():

    model=load_model("AudiModel.h5")
    scaler=joblib.load("Audiscaler.save")

    Year=float(ui2.lineEdit.text())
    Mage=float(ui2.lineEdit_2.text())
    tax =float(ui2.lineEdit_3.text())
    Mpg=float(ui2.lineEdit_4.text())
    Enginesize=float(ui2.lineEdit_5.text())

    if ui2.comboBox_2.currentText() == "AUTOMATİC":
        #Arr.append(1)
        #Arr.append(0)
        #Arr.append(0)
        Arr=[[Year,Mage,tax,Mpg,Enginesize,1,0,0]]
    elif ui2.comboBox_2.currentText() == "MANUEL":
        #Arr.append(0)
        #Arr.append(1)
        #Arr.append(0)
        Arr=[[Year,Mage,tax,Mpg,Enginesize,0,1,0]]
    elif ui2.comboBox_2.currentText() == "SEMİ-AUTO":
        #Arr.append(0)
        #Arr.append(0)
        #Arr.append(1)
        Arr=[[Year,Mage,tax,Mpg,Enginesize,0,0,1]]
    if ui2.comboBox_3.currentText() == "DİESEL":
        Arr[0].append(1)
        Arr[0].append(0)
        Arr[0].append(0)
    elif ui2.comboBox_3.currentText() == "PETROL":
        Arr[0].append(0)
        Arr[0].append(0)
        Arr[0].append(1)
    elif ui2.comboBox_3.currentText() == "HYBRİD":
        Arr[0].append(0)
        Arr[0].append(1)
        Arr[0].append(0)

    if ui2.comboBox.currentText() == "A1":
        Arr2=[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    
    elif ui2.comboBox.currentText() == "A2":
        Arr2=[0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    
    elif ui2.comboBox.currentText() == "A3":
        Arr2=[0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    
    elif ui2.comboBox.currentText() == "A4":
        Arr2=[0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    elif ui2.comboBox.currentText() == "A5":
        Arr2=[0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    elif ui2.comboBox.currentText() == "A6":
        Arr2=[0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    elif ui2.comboBox.currentText() == "A7":
        Arr2=[0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    elif ui2.comboBox.currentText() == "A8":
        Arr2=[0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    elif ui2.comboBox.currentText() == "Q2":
        Arr2=[0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    elif ui2.comboBox.currentText() == "Q3":
        Arr2=[0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    elif ui2.comboBox.currentText() == "Q5":
        Arr2=[0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    elif ui2.comboBox.currentText() == "Q7":
        Arr2=[0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    elif ui2.comboBox.currentText() == "Q8":
        Arr2=[0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0]
        
    elif ui2.comboBox.currentText() == "R8":
        Arr2=[0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0]

    elif ui2.comboBox.currentText() == "RS3":
        Arr2=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0]

    elif ui2.comboBox.currentText() == "RS4":
        Arr2=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0]

    elif ui2.comboBox.currentText() == "RS5":
        Arr2=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0]

    elif ui2.comboBox.currentText() == "RS6":
        Arr2=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0]

    elif ui2.comboBox.currentText() == "RS7":
        Arr2=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0]

    elif ui2.comboBox.currentText() == "S3":
        Arr2=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0]

    elif ui2.comboBox.currentText() == "S4":
        Arr2=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0]

    elif ui2.comboBox.currentText() == "S5":
        Arr2=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0]

    elif ui2.comboBox.currentText() == "S8":
        Arr2=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0]

    elif ui2.comboBox.currentText() == "SQ5":
        Arr2=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0]

    elif ui2.comboBox.currentText() == "SQ7":
        Arr2=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0]

    elif ui2.comboBox.currentText() == "TT":
        Arr2=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]


    Arr[0].extend(Arr2)
    
    #for x in Arr:
       # print(x)
    
    #Arr=[[2014,31930,580,21.9,5.2,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0]]

    Arr=scaler.transform(Arr)

    x=model.predict(Arr)

    ui2.lineEdit_6.setText(str(x))
    print(x)






#----------------------Signal-Slot-------------------#
#---------------------------------------------------------#
ui.Audi_winbutton.clicked.connect(Audi_Win)
ui.Ford_winbutton.clicked.connect(Ford_Win)
ui.Bmw_winbutton.clicked.connect(Bmw_Win)
ui.Merc_winbutton.clicked.connect(Merc_Win)
ui2.pushButton_2.clicked.connect(Audi_Clear)
ui2.pushButton.clicked.connect(Audi_Calculate)
ui3.Bmw_Clear_pushButton.clicked.connect(Bmw_Clear)
ui4.Merc_Clear_pushButton.clicked.connect(Merc_Clear)
ui5.Ford_Clear_pushButton.clicked.connect(Ford_Clear)



sys.exit(Uygulama.exec_())
