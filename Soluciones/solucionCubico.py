import numpy as np
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog, QTableWidgetItem
from PyQt5.uic import loadUi
import pylab as plb
from Interpolacion.Trazadores.cubicoNatural import CubicoNatural


class solucionCubico(QDialog):
    def __init__(self, funcionesInterpolacion, cubico):
        super(solucionCubico,self).__init__()
        loadUi('UI/solucioncubico.ui',self)
        self.setWindowTitle('Solución')
        self.funciones = funcionesInterpolacion
        self.cubico = cubico
        self.evaluar.clicked.connect(self.on_pushButton_clicked)
        self.botongraficar.clicked.connect(self.on_pushButton_clicked)
        #self.lix.setText(self.cubico.Lxs)
        #self.polinomio.setText(self.lagrange.pol)


    @pyqtSlot()
    def on_pushButton_clicked(self):
        if (self.sender().text().find("Evaluar") != -1):
            print("evaluar")
            #self.resultado.setText(str(self.lagrange.hallarvalor(float(self.xs.text()))))
        elif (self.sender().text().find("Graficar") != -1):
            print("graficar")
        # self.graficar()