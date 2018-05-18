from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi

from Soluciones.solucion import solucion


class paramRaices(QDialog):
    def __init__(self,funciones):
        super(paramRaices, self).__init__()
        loadUi('UI/Newton.ui', self)
        self.funciones = funciones
        self.setWindowTitle('Parámetros')
        self.continuar.clicked.connect(self.on_pushButton_clicked)

    def solucionShow(self):
        self.dialogue = solucion(self.funciones)
        self.dialogue.show()
        self.dialogue.clearParameters()
        if(self.Eabs.isChecked()):
            self.dialogue.setParametersForRaicesMultiples(self.x0.value(),self.tol.value(), self.niter.value(),True)
        elif(self.Erel.isChecked()):
            self.dialogue.setParametersForRaicesMultiples(self.x0.value(), self.tol.value(), self.niter.value(), False)

    @pyqtSlot()
    def on_pushButton_clicked(self):
        self.solucionShow()



