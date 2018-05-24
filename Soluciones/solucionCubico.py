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
        self.ecuaciones.setText(self.cubico.ecuaciones)
        self.polinomio.setText("F(x): \n" + self.cubico.funcion)

    def graficar(self):
        if(self.cubico.funcion!=""):
            vfun = np.vectorize(self.cubico.hallarValor)
            x = np.linspace(self.cubico.x[0], self.cubico.x[-1])
            y = vfun(x)
        # Funcion que vamos a graficar con los valores de x generados.
            plb.plot(x, y, color='purple', label='P(x)')
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
            self.resultado.setText(str(self.cubico.hallarvalor(float(self.xs.text()))))
        elif (self.sender().text().find("Graficar") != -1):
            print("graficar")
            self.graficar()