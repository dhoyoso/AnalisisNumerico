#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi
from main import *
from sistemasEcuaciones import sistemasEcuaciones
from interpolacion import Interpolacion
from Diferenciacion import diferenciacion
class paginaprincipal(QDialog):
    def __init__(self):
        super(paginaprincipal,self).__init__()
        loadUi('UI/principal.ui',self)
        self.setWindowTitle('Página principal')
        self.continuar.clicked.connect(self.on_pushButton_clicked)

    def unaVariableShow(self):
        self.dialogue = main()
        self.dialogue.show()

    def interpolacionShow(self):
        self.dialogue = Interpolacion()
        self.dialogue.show()

    def sistemasShow(self):
        self.dialogue = sistemasEcuaciones()
        self.dialogue.show()



    @pyqtSlot()
    def on_pushButton_clicked(self):
        if(self.sender().text() == "Continuar"):
            if(self.unavariable.isChecked()):
                print("unavar")
                self.unaVariableShow()
            elif(self.sistemas.isChecked()):
                self.sistemasShow()
                print("sistemas")
            elif (self.interpolacion.isChecked()):
                print("interpol")
                self.interpolacionShow()
            elif (self.diferenciacion.isChecked()):
                self.dialogue = diferenciacion()
                self.dialogue.show()
                print("diferenciacion e integracion")



app = QApplication(sys.argv)
widget = paginaprincipal()
widget.show()
sys._excepthook = sys.excepthook
def exception_hook(exctype, value, traceback):
    print(exctype, value, traceback)
    sys.__excepthook__(exctype, value, traceback)
    sys.exit(1)
sys.excepthook = exception_hook
sys.exit(app.exec_())