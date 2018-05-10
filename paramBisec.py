from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi

from solucion import solucion


class paramBisec(QDialog):
    def __init__(self, funciones):
        super(paramBisec, self).__init__()
        loadUi('UI/biseccion.ui', self)
        self.funciones = funciones
        self.setWindowTitle('Parámetros')
        self.continuar.clicked.connect(self.on_pushButton_clicked)

    def solucionShow(self):
        self.dialogue = solucion(self.funciones)
        self.dialogue.show()
        self.dialogue.clearParameters()
        if(self.Eabs.isChecked()):
            self.dialogue.setParametersForBiseccion(self.xi.value(),self.xs.value(),self.tol.value(), self.niter.value(),True)
        elif(self.Erel.isChecked()):
            self.dialogue.setParametersForBiseccion(self.xi.value(),self.xs.value(),self.tol.value(), self.niter.value(),False)

    @pyqtSlot()
    def on_pushButton_clicked(self):
        self.solucionShow()



