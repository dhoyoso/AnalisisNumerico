from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi
import numpy as np
from DiferenciacionNumerica import DiferenciacionNumerica
from ayuda import ayuda


class diferenciacion(QDialog):
    def __init__(self):
        super(diferenciacion, self).__init__()
        loadUi('UI/diferenciacion.ui', self)
        self.setWindowTitle('Diferenciación')
        self.evaluar.clicked.connect(self.on_pushButton_clicked)
        self.ayuda.clicked.connect(self.on_pushButton_clicked)

    @pyqtSlot()
    def on_pushButton_clicked(self):
        if self.sender().text() == "Evaluar":
            diferenciacion = DiferenciacionNumerica()

            if self.dos.isChecked():
                self.resultado.setText(diferenciacion.diferenciacionNumericaDosPuntos(self.Fx.text(),self.xi.value(),self.h.value()))

            elif self.tresadelante.isChecked():
                self.resultado.setText(diferenciacion.diferenciacionNumericaTresPuntosDelante(self.Fx.text(),self.xi.value(),self.h.value()))

            elif self.tresatras.isChecked():
                self.resultado.setText(diferenciacion.diferenciacionNumericaTresPuntosAtras(self.Fx.text(),self.xi.value(),self.h.value()))

            elif self.trescentrado.isChecked():
                self.resultado.setText(diferenciacion.diferenciacionNumericaTresPuntosCentral(self.Fx.text(),self.xi.value(),self.h.value()))

            elif self.cincoadelante.isChecked():
                self.resultado.setText(diferenciacion.diferenciacionNumericaCincoPuntosAdelante(self.Fx.text(),self.xi.value(),self.h.value()))

            elif self.cincoatras.isChecked():
                self.resultado.setText(diferenciacion.diferenciacionNumericaCincoPuntosAtras(self.Fx.text(),self.xi.value(),self.h.value()))

            elif self.cincocentrado.isChecked():
                self.resultado.setText(diferenciacion.diferenciacionNumericaCincoPuntosCentrada(self.Fx.text(),self.xi.value(),self.h.value()))
        elif (self.sender().text() == "Ayuda"):
            self.dialogue = ayuda("diferenciacion")
            self.dialogue.show()