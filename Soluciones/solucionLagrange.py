import numpy as np
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog, QTableWidgetItem
from PyQt5.uic import loadUi

from AnalisisNumerico.Interpolacion.lagrange import Lagrange


class solucionLagrange(QDialog):
    def __init__(self, funcionesInterpolacion, lagrange):
        super(solucionLagrange,self).__init__()
        loadUi('UI/solucionlagrange.ui',self)
        self.setWindowTitle('Solución')
        self.funciones = funcionesInterpolacion
        self.lagrange = lagrange
        self.agregar.clicked.connect(self.on_pushButton_clicked)
        self.evaluar.clicked.connect(self.on_pushButton_clicked)
        self.lix.setText(self.lagrange.Lxs)
        self.polinomio.setText(self.lagrange.pol)


    def agregarPunto(self):

        self.lagrange = Lagrange()
        self.funciones.setNpuntos(self.funciones.npuntos +1)
        self.funciones.x.append(float(self.xn.text()))
        self.funciones.y.append(float(self.yn.text()))
        self.lagrange.lagrange(self.funciones.npuntos, np.copy(self.funciones.x), np.copy(self.funciones.y))
        self.lix.setText(self.lagrange.Lxs)
        self.polinomio.setText(self.lagrange.pol)


    @pyqtSlot()
    def on_pushButton_clicked(self):
        if (self.sender().text() == "Agregar"):
            self.agregarPunto()
        elif (self.sender().text().find("Evaluar") != -1):
            self.resultado.setText(str(self.lagrange.hallarvalor(float(self.xs.text()))))

