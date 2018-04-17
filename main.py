import sys

import matplotlib.pyplot as plt
import numpy as np
from Funciones import Funciones
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi
from paramBisec import paramBisec
from paramBusquedas import paramBusquedas
from paramNewton import paramNewton
from paramPunto import paramPunto
from paramRaices import paramRaices
from paramRegla import paramRegla
from paramSecante import paramSecante

from AnalisisNumerico.Datos import datos

## Create functions and set domain length
x = np.arange(0.0, 2.0, 0.01)
y = x**2
dy = 2*x - 1

## Plot functions and a point where they intersect
plt.plot(x, y)
plt.plot(x, dy)
plt.plot(1, 1, 'or')

## Config the graph
plt.title('A Cool Graph')
plt.xlabel('X')
plt.ylabel('Y')
#plt.ylim([0, 4])
plt.grid(True)
plt.legend(['y = x^2', 'y = 2x'], loc='upper left')

## Show the graph


class main(QDialog):
    def __init__(self):
        super(main,self).__init__()
        loadUi('UI/paginaprincipal.ui',self)
        self.funciones = Funciones()
        self.setWindowTitle('Página principal')
        self.continuar.clicked.connect(self.on_pushButton_clicked)
        self.ingfuncion.clicked.connect(self.on_pushButton_clicked)

    def paramBusquedasShow(self):
        self.dialogue = paramBusquedas(self.funciones)
        self.dialogue.show()
        #self.solucionWindow.show()

    def paramBiseccionShow(self):
        self.dialogue = paramBisec(self.funciones)
        self.dialogue.show()

    def paramReglaFalsaShow(self):
        self.dialogue = paramRegla(self.funciones)
        self.dialogue.show()

    def paramPuntoFijoShow(self):
        self.dialogue = paramPunto(self.funciones)
        self.dialogue.show()

    def paramNewtonShow(self):
        self.dialogue = paramNewton(self.funciones)
        self.dialogue.show()

    def paramSecanteShow(self):
        self.dialogue = paramSecante(self.funciones)
        self.dialogue.show()

    def paramRaicesShow(self):
        self.dialogue = paramRaices(self.funciones)
        self.dialogue.show()

    def datosShow(self):
        self.dialogue = datos(self.funciones)
        self.dialogue.show()

    @pyqtSlot()
    def on_pushButton_clicked(self):
        if(self.sender().text() == "Continuar"):
            if(self.Busquedas.isChecked()):
                print("busquedas")
                self.paramBusquedasShow()
            elif(self.Grafico.isChecked()):
                #TODO
                print("grafico")
            elif (self.Biseccion.isChecked()):
                print("biseccion")
                self.paramBiseccionShow()
            elif (self.Regla.isChecked()):
                self.paramReglaFalsaShow()
                print("regla")
            elif (self.Punto.isChecked()):
                self.paramPuntoFijoShow()
                print("punto")
            elif (self.Newton.isChecked()):
                self.paramNewtonShow()
                print("newton")
            elif (self.Secante.isChecked()):
                self.paramSecanteShow()
                print("secante")
            elif (self.Raices.isChecked()):
                self.paramRaicesShow()
                print("raices")
        elif(self.sender().text().find("Ingresar") != -1):
            self.datosShow()




app = QApplication(sys.argv)
widget = main()
widget.show()
sys.exit(app.exec())