import numpy as np
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog, QTableWidgetItem
from PyQt5.uic import loadUi
import pylab as plb
from Interpolacion.Neville import Neville


class solucionNeville(QDialog):
    def __init__(self, funcionesInterpolacion):
        super(solucionNeville,self).__init__()
        loadUi('UI/solucionneville.ui',self)
        self.setWindowTitle('Solución')
        self.funcioninterpolacion = funcionesInterpolacion
        self.neville = Neville()
        self.evaluar.clicked.connect(self.on_pushButton_clicked)

    @pyqtSlot()
    def on_pushButton_clicked(self):
        if (self.sender().text().find("Evaluar") != -1):
            self.neville.interpolacion_neville(self.funcioninterpolacion.npuntos, float(self.xs.text()),
                                               np.copy(self.funcioninterpolacion.x),
                                               np.copy(self.funcioninterpolacion.y))
            self.resultado.setText(str(self.neville.resultado))
            n = self.funcioninterpolacion.npuntos
            # k iter
            labels = []
            labels.append("Xn")
            labels.append("F0")
            for x in range(0, n - 1):
                labels.append("F" + str(x + 1))
            for x in range(0, n + 1):
                self.tableWidget.insertColumn(x)
            self.tableWidget.setHorizontalHeaderLabels(labels)
            for x in range(0, n):
                self.tableWidget.insertRow(x)
            for x in range(0, n):
                self.tableWidget.setItem(x, 0, QTableWidgetItem(str(round(self.funcioninterpolacion.x[x], 2))))
            for i in range(0, n):
                for j in range(1, n + 1):
                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(round(self.neville.tabla[i][j - 1], 2))))


