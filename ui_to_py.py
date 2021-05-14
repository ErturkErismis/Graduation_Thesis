from PyQt5 import uic

with open ("Ford_Window.py","w",encoding="utf-8") as fout:
    uic.compileUi("Ford_Window_Design.ui",fout)