from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog, QTableWidgetItem, QTableWidget
from PyQt5.uic import loadUi

class solucionInversa(QDialog):
    def __init__(self, inicial, n):
        super(solucionInversa,self).__init__()
        loadUi('UI/solucioninversa.ui',self)
        self.setWindowTitle('Inversa')
        labels = []
        for x in range(0, n):
            labels.append("X" + str(x + 1))
        for x in range(0, n):
            self.tableWidget.insertColumn(x)
        self.tableWidget.setHorizontalHeaderLabels(labels)
        for x in range(0,n):
            self.tableWidget.insertRow(x)
        for i in range(0,n):
            for j in range(0,n):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(inicial[i][j])))