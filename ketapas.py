from PyQt5.QtCore import pyqtSlot
import matplotlib.pyplot as plt
import numpy as np
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog, QTableWidgetItem
from PyQt5.uic import loadUi

class Ketapas(QDialog):

    def __init__(self, funciones, marcas):
        super(Ketapas,self).__init__()
        loadUi('UI/ketapas.ui',self)
        self.setWindowTitle('Etapas')
        self.sistemas = funciones
        self.siguiente.clicked.connect(self.on_pushButton_clicked)
        self.anterior.clicked.connect(self.on_pushButton_clicked)
        self.contadorEtapa = 0
        self.marcas = marcas
        self.etapa.setText(str(self.contadorEtapa +1))
        self.imprimirMatriz(self.sistemas.etapas[self.contadorEtapa])
        print(self.marcas)
        self.setEtapa(self.marcas , self.sistemas.etapas[self.contadorEtapa])
        if (self.contadorEtapa == (self.sistemas.n - 2)):
            self.siguiente.setEnabled(False)
            self.siguiente.setDisabled(True)
        else:
            self.siguiente.setEnabled(True)
            self.siguiente.setDisabled(False)

        if (self.contadorEtapa == 0):
            self.anterior.setEnabled(False)
            self.anterior.setDisabled(True)
        else:
            self.anterior.setEnabled(True)
            self.anterior.setDisabled(False)

    def clearParameters(self):
        self.tableWidget.clear()

    def imprimirMatriz(self, Ab):
        print('\n'.join(['     '.join(['{:4}'.format(round(item, 2)) for item in row]) for row in Ab]))

    def setEtapa(self, marcas, final):
        self.tableWidget.clear()
        if marcas == []:
            n = self.sistemas.n
            print("entre a marcas[] y n = "+ str(n))
            # k iter
            labels = []
            for x in range(0, n):
                labels.append("X" + str(x + 1))
            labels.append("B")
            labels.append("B")
            for x in range(0, n + 1):
                self.tableWidget.insertColumn(x)
            self.tableWidget.setHorizontalHeaderLabels(labels)
            for x in range(0, n):
                self.tableWidget.insertRow(x)
            for i in range(0, n):
                for j in range(0, n + 1):
                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(round(final[i][j], 2))))
        else:
            n = self.sistemas.n
            # k iter
            labels = []
            for x in range(0, n):
                labels.append("X" + str(marcas[x]))
            labels.append("B")
            for x in range(0, n + 1):
                self.tableWidget.insertColumn(x)
            self.tableWidget.setHorizontalHeaderLabels(labels)
            for x in range(0, n):
                self.tableWidget.insertRow(x)
            for i in range(0, n):
                for j in range(0, n + 1):
                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(round(final[i][j], 2))))
            print(marcas)

    def setEtapa2(self, marcas, final):
        self.tableWidget.clear()
        if marcas == []:
            n = self.sistemas.n
            print("entre a marcas[] y n = "+ str(n))
            # k iter
            labels = []
            for x in range(0, n):
                labels.append("X" + str(x + 1))
            labels.append("B")
            labels.append("B")
            self.tableWidget.setHorizontalHeaderLabels(labels)
            for i in range(0, n):
                for j in range(0, n + 1):
                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(round(final[i][j], 2))))
        else:
            n = self.sistemas.n
            # k iter
            labels = []
            for x in range(0, n):
                labels.append("X" + str(marcas[x]))
            labels.append("B")
            self.tableWidget.setHorizontalHeaderLabels(labels)
            for i in range(0, n):
                for j in range(0, n + 1):
                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(round(final[i][j], 2))))
            print(marcas)


    @pyqtSlot()
    def on_pushButton_clicked(self):
        if (self.sender().text() == "Anterior"):
            print("anterior")
            self.contadorEtapa -= 1
            self.etapa.setText(str(self.contadorEtapa + 1))
            print(str(self.contadorEtapa))
            if(self.contadorEtapa == 0):
                self.setEtapa2(self.marcas, self.sistemas.etapas[self.contadorEtapa])
                self.anterior.setEnabled(False)
                self.anterior.setDisabled(True)
            else:
                self.setEtapa2(self.marcas, self.sistemas.etapas[self.contadorEtapa])
                self.anterior.setEnabled(True)
                self.anterior.setDisabled(False)
            if (self.contadorEtapa == (self.sistemas.n - 2)):
                self.setEtapa2(self.marcas, self.sistemas.etapas[self.contadorEtapa])
                self.siguiente.setEnabled(False)
                self.siguiente.setDisabled(True)
            else:
                self.setEtapa2(self.marcas, self.sistemas.etapas[self.contadorEtapa])
                self.siguiente.setEnabled(True)
                self.siguiente.setDisabled(False)

        elif (self.sender().text().find("Siguiente") != -1):
            print("siguiente")
            self.contadorEtapa += 1
            self.etapa.setText(str(self.contadorEtapa + 1))
            print(str(self.contadorEtapa))
            if (self.contadorEtapa == (self.sistemas.n - 2)):
                self.setEtapa2(self.marcas, self.sistemas.etapas[self.contadorEtapa])
                self.siguiente.setEnabled(False)
                self.siguiente.setDisabled(True)
            else:
                self.setEtapa2(self.marcas, self.sistemas.etapas[self.contadorEtapa])
                self.siguiente.setEnabled(True)
                self.siguiente.setDisabled(False)
            if (self.contadorEtapa == 0):
                self.setEtapa2(self.marcas, self.sistemas.etapas[self.contadorEtapa])
                self.anterior.setEnabled(False)
                self.anterior.setDisabled(True)
            else:
                self.setEtapa2(self.marcas, self.sistemas.etapas[self.contadorEtapa])
                self.anterior.setEnabled(True)
                self.anterior.setDisabled(False)




