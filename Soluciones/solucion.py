import math
import matplotlib.pyplot as plt
import numpy as np
from UnaVariable.Cerrados.Biseccion import Biseccion
from BusquedasIncrementales import BusquedasIncrementales
from UnaVariable.Abiertos.Newton import Newton
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog, QTableWidgetItem
from PyQt5.uic import loadUi
from UnaVariable.Abiertos.RaicesMultiples import RaicesMultiples
from UnaVariable.Cerrados.ReglaFalsa import ReglaFalsa
from UnaVariable.Abiertos.Secante import Secante
from decimal import Decimal

from UnaVariable.Abiertos.PuntoFijo import PuntoFijo


class solucion(QDialog):
    xi = float
    delta = float
    niter = int
    def __init__(self, funciones):
        super(solucion,self).__init__()
        loadUi('UI/solucion.ui',self)
        self.setWindowTitle('Solución')
        self.funciones = funciones

    def clearParameters(self):
        self.tableWidget.clear()

    def setParametersForBusquedas(self,xi,delta,niter):
        bi = BusquedasIncrementales()
        result = bi.busquedasIncrementales(xi,delta,niter, self.funciones)
        fxn = bi.getFxn()
        xn = bi.getXn()
        bi.reset()
        currentRowCount = self.tableWidget.rowCount()  # necessary even when there are no rows in the table
        self.tableWidget.insertColumn(currentRowCount)
        currentRowCount = self.tableWidget.rowCount()  # necessary even when there are no rows in the table
        self.tableWidget.insertColumn(currentRowCount)
        self.tableWidget.setHorizontalHeaderLabels(["Xn", "F(xn)"])
        for x in range(0, len(xn)):
            currentRowCount = self.tableWidget.rowCount()  # necessary even when there are no rows in the table
            self.tableWidget.insertRow(currentRowCount)
            self.tableWidget.setItem(currentRowCount, 0, QTableWidgetItem(str(xn.__getitem__(x))))
            self.tableWidget.setItem(currentRowCount, 1, QTableWidgetItem(str(fxn.__getitem__(x))))
        print(result+"joperra")
        self.label_5.setText(result)

    def getTol(self,tol):
        return math.pow(10, -1 * tol)

    def setParametersForBiseccion(self,xi , xs, tol, niter, eabs):
        biseccion = Biseccion()
        err = self.getTol(tol)
        result = biseccion.biseccion(xi,xs,err,niter, eabs, self.funciones)
        xi = biseccion.getXis()
        fxi = biseccion.getFxis()
        xs = biseccion.getXus()
        fxs = biseccion.getFxus()
        xm = biseccion.getXms()
        fxm = biseccion.getFxms()
        error = biseccion.getErrores()
        biseccion.reset()
        currentRowCount = self.tableWidget.rowCount()  # necessary even when there are no rows in the table
        self.tableWidget.insertColumn(currentRowCount)
        currentRowCount = self.tableWidget.rowCount()  # necessary even when there are no rows in the table
        self.tableWidget.insertColumn(currentRowCount)
        currentRowCount = self.tableWidget.rowCount()  # necessary even when there are no rows in the table
        self.tableWidget.insertColumn(currentRowCount)
        currentRowCount = self.tableWidget.rowCount()  # necessary even when there are no rows in the table
        self.tableWidget.insertColumn(currentRowCount)
        currentRowCount = self.tableWidget.rowCount()  # necessary even when there are no rows in the table
        self.tableWidget.insertColumn(currentRowCount)
        currentRowCount = self.tableWidget.rowCount()  # necessary even when there are no rows in the table
        self.tableWidget.insertColumn(currentRowCount)
        currentRowCount = self.tableWidget.rowCount()  # necessary even when there are no rows in the table
        self.tableWidget.insertColumn(currentRowCount)
        self.tableWidget.setHorizontalHeaderLabels(["Xi", "F(xi)", "Xu", "F(xu)", "Xm", "F(xm)", "error"])
        for x in range(0, len(xi)):
            currentRowCount = self.tableWidget.rowCount()  # necessary even when there are no rows in the table
            self.tableWidget.insertRow(currentRowCount)
            self.tableWidget.setItem(currentRowCount, 0, QTableWidgetItem(str(xi.__getitem__(x))))
            self.tableWidget.setItem(currentRowCount, 1, QTableWidgetItem(str(fxi.__getitem__(x))))
            self.tableWidget.setItem(currentRowCount, 2, QTableWidgetItem(str(xs.__getitem__(x))))
            self.tableWidget.setItem(currentRowCount, 3, QTableWidgetItem(str(fxs.__getitem__(x))))
            self.tableWidget.setItem(currentRowCount, 4, QTableWidgetItem(str(xm.__getitem__(x))))
            self.tableWidget.setItem(currentRowCount, 5, QTableWidgetItem(str(fxm.__getitem__(x))))
            self.tableWidget.setItem(currentRowCount, 6, QTableWidgetItem('%.2E' % Decimal(str(error.__getitem__(x)))))
        print(result)
        self.label_5.setText(result)

    def setParametersForReglaFalsa(self,xi , xs, tol, niter, eabs):
        reglafalsa = ReglaFalsa()
        err = self.getTol(tol)
        result = reglafalsa.reglaFalsa(xi,xs,err,niter, eabs, self.funciones)
        xi = reglafalsa.getXis()
        fxi = reglafalsa.getFxis()
        xs = reglafalsa.getXus()
        fxs = reglafalsa.getFxus()
        xm = reglafalsa.getXms()
        fxm = reglafalsa.getFxms()
        error = reglafalsa.getErrores()
        reglafalsa.reset()
        currentRowCount = self.tableWidget.rowCount()  # necessary even when there are no rows in the table
        self.tableWidget.insertColumn(currentRowCount)
        currentRowCount = self.tableWidget.rowCount()  # necessary even when there are no rows in the table
        self.tableWidget.insertColumn(currentRowCount)
        currentRowCount = self.tableWidget.rowCount()  # necessary even when there are no rows in the table
        self.tableWidget.insertColumn(currentRowCount)
        currentRowCount = self.tableWidget.rowCount()  # necessary even when there are no rows in the table
        self.tableWidget.insertColumn(currentRowCount)
        currentRowCount = self.tableWidget.rowCount()  # necessary even when there are no rows in the table
        self.tableWidget.insertColumn(currentRowCount)
        currentRowCount = self.tableWidget.rowCount()  # necessary even when there are no rows in the table
        self.tableWidget.insertColumn(currentRowCount)
        currentRowCount = self.tableWidget.rowCount()  # necessary even when there are no rows in the table
        self.tableWidget.insertColumn(currentRowCount)
        self.tableWidget.setHorizontalHeaderLabels(["Xi", "F(xi)", "Xu", "F(xu)", "Xm", "F(xm)", "error"])
        for x in range(0, len(xi)):
            currentRowCount = self.tableWidget.rowCount()  # necessary even when there are no rows in the table
            self.tableWidget.insertRow(currentRowCount)
            self.tableWidget.setItem(currentRowCount, 0, QTableWidgetItem(str(xi.__getitem__(x))))
            self.tableWidget.setItem(currentRowCount, 1, QTableWidgetItem(str(fxi.__getitem__(x))))
            self.tableWidget.setItem(currentRowCount, 2, QTableWidgetItem(str(xs.__getitem__(x))))
            self.tableWidget.setItem(currentRowCount, 3, QTableWidgetItem(str(fxs.__getitem__(x))))
            self.tableWidget.setItem(currentRowCount, 4, QTableWidgetItem(str(xm.__getitem__(x))))
            self.tableWidget.setItem(currentRowCount, 5, QTableWidgetItem(str(fxm.__getitem__(x))))
            self.tableWidget.setItem(currentRowCount, 6, QTableWidgetItem('%.2E' % Decimal(str(error.__getitem__(x)))))
        print(result)
        self.label_5.setText(result)

    def setParametersForPuntoFijo(self,x0, tol, niter, eabs):
        puntofijo = PuntoFijo()
        err = self.getTol(tol)
        result = puntofijo.puntoFijo(x0,err,niter, eabs, self.funciones)
        xns = puntofijo.getGxns()
        fxi = puntofijo.getFxns()
        error = puntofijo.getErrores()
        puntofijo.reset()
        currentRowCount = self.tableWidget.rowCount()  # necessary even when there are no rows in the table
        self.tableWidget.insertColumn(currentRowCount)
        currentRowCount = self.tableWidget.rowCount()  # necessary even when there are no rows in the table
        self.tableWidget.insertColumn(currentRowCount)
        currentRowCount = self.tableWidget.rowCount()  # necessary even when there are no rows in the table
        self.tableWidget.insertColumn(currentRowCount)

        self.tableWidget.setHorizontalHeaderLabels(["G(xi)", "F(xi)","error"])
        for x in range(0, len(xns)):
            currentRowCount = self.tableWidget.rowCount()  # necessary even when there are no rows in the table
            self.tableWidget.insertRow(currentRowCount)
            self.tableWidget.setItem(currentRowCount, 0, QTableWidgetItem(str(xns.__getitem__(x))))
            self.tableWidget.setItem(currentRowCount, 1, QTableWidgetItem(str(fxi.__getitem__(x))))
            self.tableWidget.setItem(currentRowCount, 2, QTableWidgetItem('%.2E' % Decimal(str(error.__getitem__(x)))))
        print(result)
        self.label_5.setText(result)

    def setParametersForNewton(self,x0, tol, niter, eabs):
        newton = Newton()
        err = self.getTol(tol)
        result = newton.newton(x0,err,niter, eabs, self.funciones)
        xns = newton.getXns()
        fxi = newton.getFxns()
        fpxi = newton.getFpxns()
        error = newton.getErrores()
        newton.reset()
        currentRowCount = self.tableWidget.rowCount()  # necessary even when there are no rows in the table
        self.tableWidget.insertColumn(currentRowCount)
        currentRowCount = self.tableWidget.rowCount()  # necessary even when there are no rows in the table
        self.tableWidget.insertColumn(currentRowCount)
        currentRowCount = self.tableWidget.rowCount()  # necessary even when there are no rows in the table
        self.tableWidget.insertColumn(currentRowCount)
        currentRowCount = self.tableWidget.rowCount()  # necessary even when there are no rows in the table
        self.tableWidget.insertColumn(currentRowCount)

        self.tableWidget.setHorizontalHeaderLabels(["Xn", "F(xn)","F'(xn)","error"])
        for x in range(0, len(xns)):
            currentRowCount = self.tableWidget.rowCount()  # necessary even when there are no rows in the table
            self.tableWidget.insertRow(currentRowCount)
            self.tableWidget.setItem(currentRowCount, 0, QTableWidgetItem(str(xns.__getitem__(x))))
            self.tableWidget.setItem(currentRowCount, 1, QTableWidgetItem(str(fxi.__getitem__(x))))
            self.tableWidget.setItem(currentRowCount, 2, QTableWidgetItem(str(fpxi.__getitem__(x))))
            self.tableWidget.setItem(currentRowCount, 3, QTableWidgetItem('%.2E' % Decimal(str(error.__getitem__(x)))))
        print(result)
        self.label_5.setText(result)

    def setParametersForSecante(self,x0,x1, tol, niter, eabs):
        secante = Secante()
        err = self.getTol(tol)
        result = secante.secante(x0,x1, err,niter, eabs, self.funciones)
        xns = secante.getXns()
        fxi = secante.getFxns()
        error = secante.getErrores()
        secante.reset()
        currentRowCount = self.tableWidget.rowCount()  # necessary even when there are no rows in the table
        self.tableWidget.insertColumn(currentRowCount)
        currentRowCount = self.tableWidget.rowCount()  # necessary even when there are no rows in the table
        self.tableWidget.insertColumn(currentRowCount)
        currentRowCount = self.tableWidget.rowCount()  # necessary even when there are no rows in the table
        self.tableWidget.insertColumn(currentRowCount)

        self.tableWidget.setHorizontalHeaderLabels(["Xn", "F(x)", "error"])
        for x in range(0, len(xns)):
            currentRowCount = self.tableWidget.rowCount()  # necessary even when there are no rows in the table
            self.tableWidget.insertRow(currentRowCount)
            self.tableWidget.setItem(currentRowCount, 0, QTableWidgetItem(str(xns.__getitem__(x))))
            self.tableWidget.setItem(currentRowCount, 1, QTableWidgetItem(str(fxi.__getitem__(x))))
            self.tableWidget.setItem(currentRowCount, 2, QTableWidgetItem('%.2E' % Decimal(str(error.__getitem__(x)))))
        print(result)
        self.label_5.setText(result)

    def setParametersForRaicesMultiples(self,x0, tol, niter, eabs):
        raicesmultiples = RaicesMultiples()
        err = self.getTol(tol)
        result = raicesmultiples.raicesMultiples(x0,err,niter, eabs, self.funciones)
        xns = raicesmultiples.getXns()
        fxi = raicesmultiples.getFxns()
        fpxi = raicesmultiples.getFpxns()
        fppxi = raicesmultiples.getFppxns()
        error = raicesmultiples.getErrores()
        raicesmultiples.reset()
        currentRowCount = self.tableWidget.rowCount()  # necessary even when there are no rows in the table
        self.tableWidget.insertColumn(currentRowCount)
        currentRowCount = self.tableWidget.rowCount()  # necessary even when there are no rows in the table
        self.tableWidget.insertColumn(currentRowCount)
        currentRowCount = self.tableWidget.rowCount()  # necessary even when there are no rows in the table
        self.tableWidget.insertColumn(currentRowCount)
        currentRowCount = self.tableWidget.rowCount()  # necessary even when there are no rows in the table
        self.tableWidget.insertColumn(currentRowCount)
        currentRowCount = self.tableWidget.rowCount()  # necessary even when there are no rows in the table
        self.tableWidget.insertColumn(currentRowCount)

        self.tableWidget.setHorizontalHeaderLabels(["Xn", "F(xn)","F'(xn)","F''(xn)","error"])
        for x in range(0, len(xns)):
            currentRowCount = self.tableWidget.rowCount()  # necessary even when there are no rows in the table
            self.tableWidget.insertRow(currentRowCount)
            self.tableWidget.setItem(currentRowCount, 0, QTableWidgetItem(str(xns.__getitem__(x))))
            self.tableWidget.setItem(currentRowCount, 1, QTableWidgetItem(str(fxi.__getitem__(x))))
            self.tableWidget.setItem(currentRowCount, 2, QTableWidgetItem(str(fpxi.__getitem__(x))))
            self.tableWidget.setItem(currentRowCount, 3, QTableWidgetItem(str(fppxi.__getitem__(x))))
            self.tableWidget.setItem(currentRowCount, 4, QTableWidgetItem('%.2E' % Decimal(str(error.__getitem__(x)))))
        print(result)
        self.label_5.setText(result)






