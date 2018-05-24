import numpy as np
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog, QTableWidgetItem
from PyQt5.uic import loadUi
import pylab as plb
from Interpolacion.lagrange import Lagrange


class solucionLagrange(QDialog):
    def __init__(self, funcionesInterpolacion, lagrange):
        super(solucionLagrange,self).__init__()
        loadUi('UI/solucionlagrange.ui',self)
        self.setWindowTitle('Solución')
        self.funciones = funcionesInterpolacion
        self.lagrange = lagrange
        self.agregar.clicked.connect(self.on_pushButton_clicked)
        self.evaluar.clicked.connect(self.on_pushButton_clicked)
        self.botongraficar.clicked.connect(self.on_pushButton_clicked)
        self.lix.setText(self.lagrange.Lxs)
        self.polinomio.setText(self.lagrange.pol)

    def graficar(self):
        # Nos da un arreglo con 256 elementos en el intervalo [a,b] para graficarlos
        x = np.linspace(-50,50, 1000, endpoint=True)
        # Funcion que vamos a graficar con los valores de x generados.
        if(self.lagrange.pol!=""):
            fx = eval(self.lagrange.pol)
            plb.plot(x, fx, color='purple', label='P(x)')

        # Valores sobre el eje X
        plb.legend(loc='best')
        #plb.plot(X, ejeX)
        plb.xlabel("X")
        plb.ylabel("Y")
        plb.grid(True)
        plb.show()


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
        elif (self.sender().text().find("Graficar") != -1):
            self.graficar()

