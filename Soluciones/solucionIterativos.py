from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog, QTableWidgetItem
from PyQt5.uic import loadUi


class SolucionIterativos(QDialog):
    def __init__(self, sistemas):
        super(SolucionIterativos,self).__init__()
        loadUi('UI/solucionecuacionesiterativas.ui',self)
        self.setWindowTitle('Solucion')
        self.sistemas = sistemas
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


