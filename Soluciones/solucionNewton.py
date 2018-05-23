import numpy as np
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog, QTableWidgetItem
from PyQt5.uic import loadUi
import pylab as plb
from Interpolacion.newton import NewtonInterpolacion


class solucionNewton(QDialog):
    def __init__(self, funcionesInterpolacion, newton):
        super(solucionNewton,self).__init__()
        loadUi('UI/solucionnewton.ui',self)
        self.setWindowTitle('Solución')
        self.funciones = funcionesInterpolacion
        self.newton = newton
        self.agregar.clicked.connect(self.on_pushButton_clicked)
        self.evaluar.clicked.connect(self.on_pushButton_clicked)
        self.botongraficar.clicked.connect(self.on_pushButton_clicked)
        n = self.funciones.npuntos
        # k iter
        labels = []
        labels.append("Xn")
        labels.append("F(Xn)")
        for x in range(0, n-1):
            labels.append("Derivada " + str(x + 1))
        for x in range(0, n + 1):
            self.tableWidget.insertColumn(x)
        self.tableWidget.setHorizontalHeaderLabels(labels)
        for x in range(0, n):
            self.tableWidget.insertRow(x)
        for x in range(0,n):
            self.tableWidget.setItem(x, 0, QTableWidgetItem(str(round(self.funciones.x[x], 2))))
        for i in range(0, n):
            for j in range(1, n+1):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(round(self.newton.tabla[i][j-1], 2))))
        self.solucion.setText(self.newton.pol)
        self.labels = labels

    def agregarPunto(self):
        while (self.tableWidget.rowCount() > 0):
            self.tableWidget.removeRow(0)
        self.tableWidget.insertColumn(self.tableWidget.columnCount())
        self.labels.append("Derivada " + str(self.tableWidget.columnCount()-2))
        self.tableWidget.setHorizontalHeaderLabels(self.labels)
        self.newton = NewtonInterpolacion()
        self.funciones.setNpuntos(self.funciones.npuntos +1)
        self.funciones.x.append(float(self.xn.text()))
        self.funciones.y.append(float(self.yn.text()))
        self.newton.newtonInterpolacion(self.funciones.npuntos, np.copy(self.funciones.x), np.copy(self.funciones.y))
        n = self.funciones.npuntos
        for x in range(0, n):
            self.tableWidget.insertRow(x)
        for x in range(0, n):
            self.tableWidget.setItem(x, 0, QTableWidgetItem(str(round(self.funciones.x[x], 2))))
        for i in range(0, n):
            for j in range(1, n + 1):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(round(self.newton.tabla[i][j - 1], 2))))
        self.solucion.setText(self.newton.pol)

    def graficar(self):
        # Nos da un arreglo con 256 elementos en el intervalo [a,b] para graficarlos
        x = np.linspace(-50,50, 1000, endpoint=True)
        # Funcion que vamos a graficar con los valores de x generados.
        if(self.newton.pol!=""):
            fx = eval(self.newton.pol)
            plb.plot(x, fx, color='purple', label='P(x)')

        # Valores sobre el eje X
        plb.legend(loc='best')
        #plb.plot(X, ejeX)
        plb.xlabel("X")
        plb.ylabel("Y")
        plb.grid(True)


        plb.show()



    @pyqtSlot()
    def on_pushButton_clicked(self):
        if (self.sender().text() == "Agregar"):
            self.agregarPunto()
        elif (self.sender().text().find("Evaluar") != -1):
            self.resultado.setText(str(self.newton.hallarvalor(float(self.xs.text()))))
        elif (self.sender().text().find("Graficar") != -1):
            self.graficar()


