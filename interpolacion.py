from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog, QTableWidgetItem, QTableWidget
from PyQt5.uic import loadUi
import numpy as np
from FuncionInterpolacion import FuncionInterpolacion

from Interpolacion.newton import NewtonInterpolacion
from Soluciones.solucionNewton import solucionNewton
from Soluciones.solucionCubico import solucionCubico
from Soluciones.solucionLagrange import solucionLagrange
from Interpolacion.lagrange import Lagrange
from Interpolacion.Trazadores.cubicoNatural import CubicoNatural
from Interpolacion.Trazadores.cudradoNatural import CuadradoNatural
from Interpolacion.Trazadores.lineal import Lineal
from Soluciones.solucionLineal import solucionLineal
from ayuda import ayuda


class Interpolacion(QDialog):
    def __init__(self):
        super(Interpolacion, self).__init__()
        loadUi('UI/interpolacion.ui', self)
        self.funcioninterpolacion = FuncionInterpolacion()
        self.setWindowTitle('Interpolación')
        self.continuar.clicked.connect(self.on_pushButton_clicked)
        self.ingpuntos.clicked.connect(self.on_pushButton_clicked)
        self.ayuda.clicked.connect(self.on_pushButton_clicked)

        labels = ["Xi", "Yi"]
        self.tableWidget.insertColumn(0)
        self.tableWidget.insertColumn(1)
        self.tableWidget.setHorizontalHeaderLabels(labels)

    def newtonShow(self):
        print("newtonShow")
        gausi = NewtonInterpolacion()
        #x = [1, 1.2, 1.4, 1.6, 1.8] #2
        #y = [0.6747,0.8491,1.1214,1.4921,1.9607] #2.5258
        #x = [2,2.5,3,3.6,4.2] #5
        #y = [2.45,6.78,8.75,9.83,10.98] #11.73
        #gausi.newtonInterpolacion(5, x, y)
        #self.funcioninterpolacion.setX(x)
        #self.funcioninterpolacion.setY(y)
        #self.funcioninterpolacion.setNpuntos(len(x))
        gausi.newtonInterpolacion(self.npuntos.value(), np.copy(self.funcioninterpolacion.x), np.copy(self.funcioninterpolacion.y))
        self.dialogue = solucionNewton(self.funcioninterpolacion, gausi)
        self.dialogue.show()
    def lagrangeShow(self):
        print("lagrangeShow")
        gausi = Lagrange()
        #x = [1, 1.2, 1.4, 1.6, 1.8]  # 2
        #y = [0.6747, 0.8491, 1.1214, 1.4921, 1.9607]  # 2.5258
        # x = [2,2.5,3,3.6,4.2] #5
        # y = [2.45,6.78,8.75,9.83,10.98] #11.73
        #gausi.lagrange(5, x, y)
        #self.funcioninterpolacion.setX(x)
        #self.funcioninterpolacion.setY(y)
        #self.funcioninterpolacion.setNpuntos(len(x))
        gausi.lagrange(self.npuntos.value(), np.copy(self.funcioninterpolacion.x), np.copy(self.funcioninterpolacion.y))
        self.dialogue = solucionLagrange(self.funcioninterpolacion, gausi)
        self.dialogue.show()

    def linealShow(self):
        print("lineal")
        print("cuadradoShow")
        gausi = Lineal()
        #x = [1.0, 3.0, 5.0]
        #y = [1.0, 6.0, 25.0]
        #self.funcioninterpolacion.setX(x)
        #self.funcioninterpolacion.setY(y)
        #self.funcioninterpolacion.setNpuntos(len(x))
        #gausi.lineal(3, x, y)
        gausi.lineal(self.npuntos.value(), np.copy(self.funcioninterpolacion.x), np.copy(self.funcioninterpolacion.y))
        self.dialogue = solucionLineal(self.funcioninterpolacion, gausi)
        self.dialogue.show()

    def cuadraticoShow(self):
        print("cuadradoShow")
        gausi = CuadradoNatural()
        #x = [3, 4.5, 7, 9]
        #y = [2.5, 1, 2.5, 0.5]
        #self.funcioninterpolacion.setX(x)
        #self.funcioninterpolacion.setY(y)
        #self.funcioninterpolacion.setNpuntos(len(x))
        #gausi.cuadradoNatural(4, x, y)
        gausi.cuadradoNatural(self.npuntos.value(), np.copy(self.funcioninterpolacion.x), np.copy(self.funcioninterpolacion.y))
        self.dialogue = solucionCubico(self.funcioninterpolacion, gausi)
        self.dialogue.show()
    def cubicoShow(self):
        print("cubicoShow")
        gausi = CubicoNatural()
        #x = [2, 3, 5]
        #y = [-1, 2, -7]
        #self.funcioninterpolacion.setX(x)
        #self.funcioninterpolacion.setY(y)
        #self.funcioninterpolacion.setNpuntos(len(x))
        #gausi.cubicoNatural(3,x,y)
        gausi.cubicoNatural(self.npuntos.value(), np.copy(self.funcioninterpolacion.x), np.copy(self.funcioninterpolacion.y))
        self.dialogue = solucionCubico(self.funcioninterpolacion, gausi)
        self.dialogue.show()

    def createTable(self):
        if len(self.funcioninterpolacion.x) == 0:
            while (self.tableWidget.rowCount() > 0):
                self.tableWidget.removeRow(0)
            for i in range(0, self.npuntos.value()):
                self.tableWidget.insertRow(i)
                self.tableWidget.setItem(i, 0, QTableWidgetItem(" "))
                self.tableWidget.setItem(i, 1, QTableWidgetItem(" "))
        else:
            while (self.tableWidget.rowCount() > 0):
                self.tableWidget.removeRow(0)
            for i in range(0, self.npuntos.value()):
                self.tableWidget.insertRow(i)
                if(i<len(self.funcioninterpolacion.x)):
                    self.tableWidget.setItem(i, 0, QTableWidgetItem(str(self.funcioninterpolacion.x[i])))
                    self.tableWidget.setItem(i, 1, QTableWidgetItem(str(self.funcioninterpolacion.y[i])))
                else:
                    self.tableWidget.setItem(i, 0, QTableWidgetItem(" "))
                    self.tableWidget.setItem(i, 1, QTableWidgetItem(" "))


    def getXsandYs(self):
        x = []
        y = []
        for i in range(0,self.npuntos.value()):
            x.append( float(self.tableWidget.item(i, 0).text()))
            y.append( float(self.tableWidget.item(i, 1).text()))
        self.funcioninterpolacion.setX(x)
        self.funcioninterpolacion.setY(y)
        self.funcioninterpolacion.setNpuntos(len(x))

    @pyqtSlot()
    def on_pushButton_clicked(self):
        if self.sender().text() == "Continuar":
            if self.newtondivididas.isChecked():
                print("newton")
                self.getXsandYs()
                self.newtonShow()
            elif self.lagrange.isChecked():
                print("lagrange")
                self.getXsandYs()
                self.lagrangeShow()
            elif self.lineal.isChecked():
                print("lineal")
                self.getXsandYs()
                self.linealShow()
            elif self.cuadratico.isChecked():
                print("cuadratico")
                self.getXsandYs()
                self.cuadraticoShow()
            elif self.cubico.isChecked():
                print("cubico")
                self.getXsandYs()
                self.cubicoShow()

        elif (self.sender().text().find("Ingresar") != -1):
            print("ing puntos")
            self.createTable()
        elif (self.sender().text() == "Ayuda"):
            if self.newtondivididas.isChecked():
                print("newton")
                self.dialogue = ayuda("newtondiferencias")
                self.dialogue.show()
            elif self.lagrange.isChecked():
                self.dialogue = ayuda("lagrange")
                self.dialogue.show()
            elif self.lineal.isChecked():
                print("lineal")
                self.dialogue = ayuda("lineal")
                self.dialogue.show()
            elif self.cuadratico.isChecked():
                print("cuadratico")
                self.dialogue = ayuda("cuadratico")
                self.dialogue.show()
            elif self.cubico.isChecked():
                print("cubico")
                self.dialogue = ayuda("cubico")
                self.dialogue.show()