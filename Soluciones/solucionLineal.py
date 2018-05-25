import numpy as np
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog, QTableWidgetItem
from PyQt5.uic import loadUi
import pylab as plb
from Interpolacion.Trazadores.cubicoNatural import CubicoNatural


class solucionLineal(QDialog):
    def __init__(self, funcionesInterpolacion, lineal):
        super(solucionLineal,self).__init__()
        loadUi('UI/solucionlineal.ui',self)
        self.setWindowTitle('Solución')
        self.funciones = funcionesInterpolacion
        self.lineal = lineal
        self.evaluar.clicked.connect(self.on_pushButton_clicked)
        self.botongraficar.clicked.connect(self.on_pushButton_clicked)
        self.polinomio.setText("F(x): \n" + self.lineal.funcion)

    def graficar(self):
        if(self.lineal.funcion!=""):
            vfun = np.vectorize(self.lineal.hallarValor)
            x = np.linspace(self.lineal.x[0], self.lineal.x[-1])
            y = vfun(x)
        # Funcion que vamos a graficar con los valores de x generados.
            plb.plot(x, y, color='purple', label='F(x)')
        # Valores sobre el eje X
            plb.legend(loc='best')
        #plb.plot(X, ejeX)
            plb.xlabel("X")
            plb.ylabel("Y")
            plb.grid(True)
            plb.show()

    @pyqtSlot()
    def on_pushButton_clicked(self):
        if (self.sender().text().find("Evaluar") != -1):
            print("evaluar")
            self.resultado.setText(str(self.lineal.hallarValor(float(self.xs.text()))))
        elif (self.sender().text().find("Graficar") != -1):
            print("graficar")
            self.graficar()