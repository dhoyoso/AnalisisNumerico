from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog, QTableWidgetItem
from PyQt5.uic import loadUi
from Soluciones.solucionTridiagonal import solucionTridiagonal
from SistemasEcuaciones.Gaussiana.EliminacionGaussianaTridiagonal import EliminacionGaussianaTridiagonal

class paramTridiagonal(QDialog):
    def __init__(self, n):
        super(paramTridiagonal, self).__init__()
        loadUi('UI/parametrostridiagonal.ui', self)
        self.setWindowTitle('Parámetros')
        self.n = int(n)
        self.continuar.clicked.connect(self.on_pushButton_clicked)

        for x in range(0, n-1):
            self.a.insertColumn(x)
            self.c.insertColumn(x)
        self.a.insertRow(0)
        self.c.insertRow(0)
        for i in range(0, n-1):
            self.a.setItem(0, i, QTableWidgetItem(" "))
            self.c.setItem(0, i, QTableWidgetItem(" "))
        for x in range(0, n):
            self.b.insertColumn(x)
            self.bb.insertColumn(x)
        self.bb.insertRow(0)
        self.b.insertRow(0)
        for i in range(0, n):
            self.b.setItem(0, i, QTableWidgetItem(" "))
            self.bb.setItem(0, i, QTableWidgetItem(" "))


    def solucionShow(self):
        aa = [None] * (self.n-1)
        bbb = [None] * self.n
        cc = [None] * (self.n-1)
        bbbb = [None] * self.n
        for i in range(0, self.n):
            bbb[i] = float(self.b.item(0, i).text())
            bbbb[i] = float(self.bb.item(0, i).text())
        for i in range(0, self.n-1):
            aa[i] = float(self.a.item(0, i).text())
            cc[i] = float(self.c.item(0, i).text())
        gausi = EliminacionGaussianaTridiagonal()
        #aa = [5, -3, 2, 4, 7]
        #bbb = [4, 8, 7, -5, 10, 15]
        #cc = [3, 2, 2, 2, 2]
        #bbbb = [23, 18, 19, 2, 12, -50]
        #self.n = 6
        gausi.eliminacionGaussianaTridiagonal(self.n,aa,bbb,cc,bbbb)
        self.dialogue = solucionTridiagonal(gausi)
        self.dialogue.show()

    @pyqtSlot()
    def on_pushButton_clicked(self):
        self.solucionShow()



