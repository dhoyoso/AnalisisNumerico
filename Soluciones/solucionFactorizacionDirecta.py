from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog, QTableWidgetItem
from PyQt5.uic import loadUi

from ketapasFactorizacion import KetapasFactorizacion


class SolucionFactorizacionDirecta(QDialog):
    def __init__(self, sistemas, solunica, marcas):
        super(SolucionFactorizacionDirecta, self).__init__()
        loadUi('UI/solucionecuacionesfactorizaciondirecta.ui', self)
        self.setWindowTitle('Solución')
        self.sistemas = sistemas
        self.etapas.clicked.connect(self.on_pushButton_clicked)
        if (solunica):
            inicial = self.sistemas.inicialAB
            L = self.sistemas.etapasL[-1]
            U = self.sistemas.etapasU[-1]
            zns = self.sistemas.zns
            xns = self.sistemas.xns
            n = self.sistemas.n
            print("ini", inicial)
            # primera iter
            labels = []
            for x in range(0, n):
                labels.append("X" + str(x + 1))
            labels.append("B")
            for x in range(0, n + 1):
                self.tableWidget.insertColumn(x)
            self.tableWidget.setHorizontalHeaderLabels(labels)
            for x in range(0, n):
                self.tableWidget.insertRow(x)
            for i in range(0, n):
                for j in range(0, n + 1):
                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(inicial[i][j])))
            # L
            labels = []
            for x in range(0, n):
                labels.append(" " + str(x + 1))
            for x in range(0, n ):
                self.tableWidget_2.insertColumn(x)
            self.tableWidget_2.setHorizontalHeaderLabels(labels)
            for x in range(0, n):
                self.tableWidget_2.insertRow(x)
            for i in range(0, n):
                for j in range(0, n):
                    self.tableWidget_2.setItem(i, j, QTableWidgetItem(str(round(L[i][j], 2))))
            # U
            labels = []
            for x in range(0, n):
                labels.append(" " + str(x + 1))
            for x in range(0, n):
                self.tableWidget_4.insertColumn(x)
            self.tableWidget_4.setHorizontalHeaderLabels(labels)
            for x in range(0, n):
                self.tableWidget_4.insertRow(x)
            for i in range(0, n):
                for j in range(0, n):
                    self.tableWidget_4.setItem(i, j, QTableWidgetItem(str(round(U[i][j], 2))))

            print(xns)
            solucion = []
            for i in range(0, len(xns)):
                solucion.append(" X" + str(i + 1) + " = " + str(round(xns[i], 2)))
            self.label_7.setText("".join(solucion))

            print(zns)
            solucion = []
            for i in range(0, len(zns)):
                solucion.append(" Z" + str(i + 1) + " = " + str(round(zns[i], 2)))
            self.label_9.setText("".join(solucion))

        else:
            self.label_9.setText(" ")
            self.label_7.setText("No tiene solución unica")

    def clearParameters(self):
        self.tableWidget.clear()
        self.tableWidget_2.clear()

    def showEtapas(self):
        self.dialogue = KetapasFactorizacion(self.sistemas)
        self.dialogue.show()

    @pyqtSlot()
    def on_pushButton_clicked(self):
        if (self.sender().text().find("etapas") != -1):
            print("etapas")
            self.showEtapas()
