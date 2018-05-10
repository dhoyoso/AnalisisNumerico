from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog, QTableWidgetItem, QTableWidget
from PyQt5.uic import loadUi
from ketapas import Ketapas

class solucionsistemas(QDialog):
    def __init__(self, sistemas, solunica,marcas):
        super(solucionsistemas,self).__init__()
        loadUi('UI/solucionecuaciones.ui',self)
        self.setWindowTitle('Solución')
        self.sistemas = sistemas
        self.marcas = marcas
        self.pushButton_3.clicked.connect(self.on_pushButton_clicked)
        self.etapas.clicked.connect(self.on_pushButton_clicked)
        if(solunica):
            if(marcas==[]):
                inicial = self.sistemas.inicialAB
                final = self.sistemas.lastAB
                xns = self.sistemas.xns
                n = self.sistemas.n
                print("ini",inicial)
                # primera iter
                labels = []
                for x in range(0, n):
                    labels.append("X" + str(x + 1))
                labels.append("B")
                for x in range(0, n + 1):
                    self.tableWidget.insertColumn(x)
                self.tableWidget.setHorizontalHeaderLabels(labels)
                for x in range(0,n):
                    self.tableWidget.insertRow(x)
                for i in range(0,n):
                    for j in range(0,n+1):
                        self.tableWidget.setItem(i, j, QTableWidgetItem(str(inicial[i][j])))
                #k iter
                labels = []
                for x in range(0, n):
                    labels.append("X" + str(x + 1))
                labels.append("B")
                for x in range(0, n + 1):
                    self.tableWidget_2.insertColumn(x)
                self.tableWidget_2.setHorizontalHeaderLabels(labels)
                for x in range(0, n):
                    self.tableWidget_2.insertRow(x)
                for i in range(0, n):
                    for j in range(0, n + 1):
                        self.tableWidget_2.setItem(i, j, QTableWidgetItem(str(round(final[i][j],2))))
                print (xns)
                solucion = []
                for i in range(0,n):
                    solucion.append( " X"+str(i+1)+" = "+ str(round(xns[i],2)))
                self.label_7.setText("".join(solucion))
            else:
                inicial = self.sistemas.inicialAB
                final = self.sistemas.lastAB
                xns = self.sistemas.xns
                n = self.sistemas.n
                marcas = self.marcas[-1]
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
                # k iter
                labels = []
                for x in range(0, n):
                    labels.append("X" + str(marcas[x]))
                labels.append("B")
                for x in range(0, n + 1):
                    self.tableWidget_2.insertColumn(x)
                self.tableWidget_2.setHorizontalHeaderLabels(labels)
                for x in range(0, n):
                    self.tableWidget_2.insertRow(x)
                for i in range(0, n):
                    for j in range(0, n + 1):
                        self.tableWidget_2.setItem(i, j, QTableWidgetItem(str(round(final[i][j], 2))))
                print(xns)
                solucion = []

                for i in range(0, n):
                    solucion.append(" X" + str(marcas[i]) + " = " + str(round(xns[i], 2)))
                self.label_7.setText("".join(solucion))
                print(marcas)
        else:
            self.label_7.setText("No tiene solución unica")


    def clearParameters(self):
        self.tableWidget.clear()
        self.tableWidget_2.clear()

    def showEtapas(self):
        self.dialogue = Ketapas(self.sistemas, self.marcas)
        self.dialogue.show()

    @pyqtSlot()
    def on_pushButton_clicked(self):
        if (self.sender().text() == "Cancelar"):
            self.tableWidget.clear()
            self.tableWidget_2.clear()
        elif (self.sender().text().find("etapas") != -1):
            print("etapas")
            self.showEtapas()

