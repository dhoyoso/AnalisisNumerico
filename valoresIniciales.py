import math

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog, QTableWidgetItem
from PyQt5.uic import loadUi


class ValoresIniciales(QDialog):

    def __init__(self, sistemas):
        super(ValoresIniciales, self).__init__()
        loadUi('UI/valoresiniciales.ui', self)
        self.setWindowTitle('Ingresa los valores iniciales')
        self.sistemas = sistemas
        self.n = self.sistemas.n
        n = self.n
        self.guardar.clicked.connect(self.on_pushButton_clicked)
        # k iter
        if(self.sistemas.numiter == 0):
            labels = []
            for x in range(0, n):
                labels.append("X" + str(x + 1))
            for x in range(0, n):
                self.tableWidget.insertColumn(x)
            self.tableWidget.setHorizontalHeaderLabels(labels)
            self.tableWidget.insertRow(0)
            for i in range(0, n):
                self.tableWidget.setItem(0, i, QTableWidgetItem(" "))
        else:
            labels = []
            for x in range(0, n):
                labels.append("X" + str(x + 1))
            for x in range(0, n):
                self.tableWidget.insertColumn(x)
            self.tableWidget.setHorizontalHeaderLabels(labels)
            self.tableWidget.insertRow(0)
            for i in range(0, n):
                self.tableWidget.setItem(0, i, QTableWidgetItem(str(self.sistemas.xceros[i])))
            self.tol.setValue(abs(math.log(self.sistemas.tol,10)))
            self.iter.setValue(self.sistemas.numiter)
            self.lamb.setValue(self.sistemas.lamb)

    def getXceros(self):
        b = [None] * self.n
        for i in range(0, self.n):
            b[i] = float(self.tableWidget.item(0, i).text())
        return b

    @pyqtSlot()
    def on_pushButton_clicked(self):
        self.sistemas.setXceros(self.getXceros())
        self.sistemas.setLamb(self.lamb.value())
        self.sistemas.setNumiter(self.iter.value())
        self.sistemas.setTol(math.pow(10, -1 * self.tol.value()))
        self.close()
