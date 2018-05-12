from PyQt5.QtCore import pyqtSlot
import matplotlib.pyplot as plt
import numpy as np
from Biseccion import Biseccion
from BusquedasIncrementales import BusquedasIncrementales
from Newton import Newton
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog, QTableWidgetItem
from PyQt5.uic import loadUi
from RaicesMultiples import RaicesMultiples
from ReglaFalsa import ReglaFalsa
from Secante import Secante



from PuntoFijo import PuntoFijo

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

class SolucionIterativos(QDialog):
    def __init__(self, sistemas):
        super(SolucionIterativos,self).__init__()
        loadUi('UI/solucionecuacionesiterativas.ui',self)
        self.setWindowTitle('Solucion')
        self.sistemas = sistemas
        self.pushButton_3.clicked.connect(self.on_pushButton_clicked)
        # k iter
        print(self.sistemas.iteraciones)
        n = self.sistemas.n
        labels = []
        for x in range(0, n):
            labels.append("X" + str(x + 1))
        for x in range(0, n):
            self.tableWidget.insertColumn(x)
        self.tableWidget.setHorizontalHeaderLabels(labels)
        for x in range(0, len(self.sistemas.iteraciones)):
            self.tableWidget.insertRow(x)
        for i in range(0, len(self.sistemas.iteraciones)):
            for j in range(0, n):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(round(self.sistemas.iteraciones[i][j],9))))


    def clearParameters(self):
        self.tableWidget.clear()

    @pyqtSlot()
    def on_pushButton_clicked(self):
        self.tableWidget.clear()
