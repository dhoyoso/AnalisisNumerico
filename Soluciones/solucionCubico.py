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
        inicial = self.cubico.etapas[0]
        final = self.cubico.etapas[-1]
        xns = self.cubico.xns
        n = self.cubico.n * 4
        marcas = self.cubico.marcas
        print("ini", inicial)
        # primera iter
        labels = []
        for x in range(0, n):
            labels.append(str(marcas[x]))
        labels.append("B")
        for x in range(0, n + 1):
            self.tableWidget.insertColumn(x)
        self.tableWidget.setHorizontalHeaderLabels(labels)
        for x in range(0, n):
            self.tableWidget.insertRow(x)
        for i in range(0, n):
            for j in range(0, n + 1):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(inicial[i][j])))
        # k iter

        labels = []
        for x in range(0, n):
            labels.append(str(marcas[self.cubico.marcasfinales[x]-1]))
        labels.append("B")
        for x in range(0, n + 1):
            self.tableWidget_2.insertColumn(x)
        self.tableWidget_2.setHorizontalHeaderLabels(labels)
        for x in range(0, n):
            self.tableWidget_2.insertRow(x)
        for i in range(0, n):
            for j in range(0, n + 1):
                self.tableWidget_2.setItem(i, j, QTableWidgetItem(str(round(final[i][j], 2))))
        print(xns)
        solucion = []

        for i in range(0, n):
            solucion.append(" " + str(marcas[i]) + " = " + str(round(xns[i], 2)))
        #self.label_7.setText("".join(solucion))
        print("".join(solucion))
        #print(marcas)

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
            self.resultado.setText(str(self.cubico.hallarValor(float(self.xs.text()))))
        elif (self.sender().text().find("Graficar") != -1):
            print("graficar")
            self.graficar()