import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from Main_Window import *
from Audi_Window import *
from Bmw_Window import *
from Merc_Window import *
from Ford_Window import *
#----------------------UYGULAMA OLUŞTUR-------------------#
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
ui2=Ui_BMW()
ui2.setupUi(penBmw)

penMerc=QWidget()
ui2=Ui_Form3()
ui2.setupUi(penMerc)

penFord=QWidget()
ui2=Ui_Form2()
ui2.setupUi(penFord)

def Audi_Win():
    penAudi.show()

def Bmw_Win():
    penBmw.show()

def Merc_Win():
    penMerc.show()

def Ford_Win():
    penFord.show()



ui.Audi_winbutton.clicked.connect(Audi_Win)
ui.Ford_winbutton.clicked.connect(Ford_Win)
ui.Bmw_winbutton.clicked.connect(Bmw_Win)
ui.Merc_winbutton.clicked.connect(Merc_Win)


sys.exit(Uygulama.exec_())
