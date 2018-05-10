from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog, QTableWidgetItem
from PyQt5.uic import loadUi


class ingSistemas(QDialog):

    def __init__(self, sistema, n):
        super(ingSistemas, self).__init__()
        loadUi('UI/ingresarsistema.ui', self)
        self.setWindowTitle('Ingresar sistema de ecuaciones')
        self.sistema = sistema
        self.n = n
        self.guardar.clicked.connect(self.on_pushButton_clicked)
        labels = []
        for x in range(0, n):
            labels.append("X" + str(x + 1))
        labels.append("B")
        for x in range(0, n + 1):
            currentRowCount = self.tableWidget.rowCount()  # necessary even when there are no rows in the table
            self.tableWidget.insertColumn(currentRowCount)
            if (x != n):
                currentRowCount = self.tableWidget.rowCount()  # necessary even when there are no rows in the table
                self.tableWidget.insertRow(currentRowCount)
                for y in range(0, n):
                    self.tableWidget.setItem(currentRowCount, y, QTableWidgetItem(" "))

        self.tableWidget.setHorizontalHeaderLabels(labels)

    def getA(self):
        # print(self.tableWidget.item(0,0).text())
        a = [[None for i in range(self.n)] for j in range(self.n)]
        for i in range(0, self.n):
            for j in range(0, self.n):
                a[i][j] = float(self.tableWidget.item(i, j).text())
        return a
        # print(a)

    def getB(self):
        b = [None] * self.n
        for i in range(0, self.n):
            b[i] = float(self.tableWidget.item(i, self.n).text())
        return b
        # print(b)

    def getAB(self):
        ab = [[None for i in range(self.n + 1)] for j in range(self.n)]
        for i in range(0, self.n):
            for j in range(0, self.n + 1):
                ab[i][j] = float(self.tableWidget.item(i, j).text())
        return ab  # print(ab)

    @pyqtSlot()
    def on_pushButton_clicked(self):
        self.sistema.setA(self.getA())
        self.sistema.setB(self.getB())
        self.sistema.setAB(self.getAB())
        self.sistema.setInicialAB(self.getAB())
        self.close()
