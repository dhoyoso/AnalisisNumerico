from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog, QTableWidgetItem
from PyQt5.uic import loadUi



class KetapasFactorizacion(QDialog):
    def __init__(self, sistemas):
        super(KetapasFactorizacion, self).__init__()
        loadUi('UI/ketapasFactorizacion.ui', self)
        self.setWindowTitle('Etapas')
        self.sistemas = sistemas
        self.siguiente.clicked.connect(self.on_pushButton_clicked)
        self.anterior.clicked.connect(self.on_pushButton_clicked)
        self.contadorEtapa = 0
        self.n = self.sistemas.n
        n = self.n
        inicial = self.sistemas.inicialAB

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

        self.setEtapa(self.n,self.sistemas.etapasL[self.contadorEtapa],self.sistemas.etapasU[self.contadorEtapa])

        if (self.contadorEtapa == len(self.sistemas.etapasU)):
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


    def setEtapa(self, n, L, U):
        # L
        labels = []
        for x in range(0, n):
            labels.append(" " + str(x + 1))
        for x in range(0, n):
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


    def setEtapa2(self, n, L, U):
        # L
        labels = []
        for x in range(0, n):
            labels.append(" " + str(x + 1))
        self.tableWidget_2.setHorizontalHeaderLabels(labels)
        for i in range(0, n):
            for j in range(0, n):
                self.tableWidget_2.setItem(i, j, QTableWidgetItem(str(round(L[i][j], 2))))
        # U
        labels = []
        for x in range(0, n):
            labels.append(" " + str(x + 1))
        self.tableWidget_4.setHorizontalHeaderLabels(labels)
        for i in range(0, n):
            for j in range(0, n):
                self.tableWidget_4.setItem(i, j, QTableWidgetItem(str(round(U[i][j], 2))))


    def clearParameters(self):
        self.tableWidget.clear()
        self.tableWidget_2.clear()


    @pyqtSlot()
    def on_pushButton_clicked(self):
        if (self.sender().text() == "Anterior"):
            print("anterior")
            self.contadorEtapa -= 1
            print(str(self.contadorEtapa))
            if(self.contadorEtapa == 0):
                self.setEtapa2(self.n,self.sistemas.etapasL[self.contadorEtapa],self.sistemas.etapasU[self.contadorEtapa])
                self.anterior.setEnabled(False)
                self.anterior.setDisabled(True)
            else:
                self.setEtapa2(self.n,self.sistemas.etapasL[self.contadorEtapa],self.sistemas.etapasU[self.contadorEtapa])
                self.anterior.setEnabled(True)
                self.anterior.setDisabled(False)

            if (self.contadorEtapa == len(self.sistemas.etapasU)-1):
                self.setEtapa2(self.n,self.sistemas.etapasL[self.contadorEtapa],self.sistemas.etapasU[self.contadorEtapa])
                self.siguiente.setEnabled(False)
                self.siguiente.setDisabled(True)
            else:
                self.setEtapa2(self.n,self.sistemas.etapasL[self.contadorEtapa],self.sistemas.etapasU[self.contadorEtapa])
                self.siguiente.setEnabled(True)
                self.siguiente.setDisabled(False)

        elif (self.sender().text().find("Siguiente") != -1):
            print("siguiente")
            self.contadorEtapa += 1
            print(str(self.contadorEtapa))
            if (self.contadorEtapa == len(self.sistemas.etapasU)-1):
                self.setEtapa2(self.n,self.sistemas.etapasL[self.contadorEtapa],self.sistemas.etapasU[self.contadorEtapa])
                self.siguiente.setEnabled(False)
                self.siguiente.setDisabled(True)
            else:
                self.setEtapa2(self.n,self.sistemas.etapasL[self.contadorEtapa],self.sistemas.etapasU[self.contadorEtapa])
                self.siguiente.setEnabled(True)
                self.siguiente.setDisabled(False)
            if (self.contadorEtapa == 0):
                self.setEtapa2(self.n,self.sistemas.etapasL[self.contadorEtapa],self.sistemas.etapasU[self.contadorEtapa])
                self.anterior.setEnabled(False)
                self.anterior.setDisabled(True)
            else:
                self.setEtapa2(self.n,self.sistemas.etapasL[self.contadorEtapa],self.sistemas.etapasU[self.contadorEtapa])
                self.anterior.setEnabled(True)
                self.anterior.setDisabled(False)
