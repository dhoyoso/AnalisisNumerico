from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog, QTableWidgetItem, QTableWidget
from PyQt5.uic import loadUi
from ketapas import Ketapas

class solucionTridiagonal(QDialog):
    def __init__(self, gausi):
        super(solucionTridiagonal,self).__init__()
        loadUi('UI/soluciontridiagonal.ui',self)
        self.setWindowTitle('Solución')
        self.gausi = gausi
        if(gausi.unica):
                inicial = self.gausi.inicial
                final = self.gausi.matrix
                xns = self.gausi.xns
                n = self.gausi.n
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
                        if(j!=n):
                            self.tableWidget.setItem(i, j, QTableWidgetItem(str(inicial[i][j])))
                        else:
                            self.tableWidget.setItem(i,j, QTableWidgetItem(str(self.gausi.inicialBB[i])))
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
                        if (j != n):
                            self.tableWidget_2.setItem(i, j, QTableWidgetItem(str(final[i][j])))
                        else:
                            self.tableWidget_2.setItem(i, j, QTableWidgetItem(str(self.gausi.bb[i])))
                print (xns)
                solucion = []
                for i in range(0,n):
                    solucion.append( " X"+str(i+1)+" = "+ str(round(xns[i],2)))
                self.label_7.setText("".join(solucion))
        else:
            self.label_7.setText("No tiene solución unica")
