from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi

from solucion import solucion


class paramBusquedas(QDialog):
    def __init__(self, funciones):
        super(paramBusquedas, self).__init__()
        loadUi('UI/busquedas.ui', self)
        self.setWindowTitle('Parámetros')
        self.funciones = funciones
        self.continuar.clicked.connect(self.on_pushButton_clicked)

    def solucionShow(self):
        self.dialogue = solucion(self.funciones)
        self.dialogue.show()
        self.dialogue.clearParameters()
        self.dialogue.setParametersForBusquedas(self.xi.value(),self.delta.value(),self.niter.value())

    @pyqtSlot()
    def on_pushButton_clicked(self):
        self.solucionShow()



