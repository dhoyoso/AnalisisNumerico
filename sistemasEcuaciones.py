
from Sistemas import Sistemas
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi
from EliminacionGaussianaSimple import EliminacionGaussianaSimple
from EliminacionGaussianaParcial import EliminacionGaussianaParcial
from EliminacionGaussianaTotal import EliminacionGaussianaTotal
from ingSistemas import ingSistemas
from solucionsistemas import solucionsistemas

class sistemasEcuaciones(QDialog):
    def __init__(self):
        super(sistemasEcuaciones,self).__init__()
        loadUi('UI/sistemasecuaciones.ui',self)
        self.sistemaecuaciones = Sistemas()
        self.setWindowTitle('Sistemas de ecuaciones')
        self.continuar.clicked.connect(self.on_pushButton_clicked)
        self.ingsistema.clicked.connect(self.on_pushButton_clicked)

    def simpleShow(self):
        gausi = EliminacionGaussianaSimple()
        gausi.eliminacionGaussianaSimple(self.n.value(), self.sistemaecuaciones.AB)
        self.sistemaecuaciones.setAB(gausi.getAb())
        self.sistemaecuaciones.setLastAB(gausi.getAb())
        self.sistemaecuaciones.setXns(gausi.getXns())
        self.sistemaecuaciones.setEtapas(gausi.getEtapas())
        self.dialogue = solucionsistemas(self.sistemaecuaciones,gausi.unica,[])
        self.dialogue.show()

    def parcialShow(self):
        gausi = EliminacionGaussianaParcial()
        gausi.eliminacionGaussianaParcial(self.n.value(), self.sistemaecuaciones.AB)
        self.sistemaecuaciones.setAB(gausi.getAb())
        self.sistemaecuaciones.setLastAB(gausi.getAb())
        self.sistemaecuaciones.setXns(gausi.getXns())
        self.sistemaecuaciones.setEtapas(gausi.getEtapas())
        self.dialogue = solucionsistemas(self.sistemaecuaciones, gausi.unica,[])
        self.dialogue.show()


    def totalShow(self):
        gausi = EliminacionGaussianaTotal()
        gausi.eliminacionGaussianaTotal(self.n.value(), self.sistemaecuaciones.AB)
        self.sistemaecuaciones.setAB(gausi.getAb())
        self.sistemaecuaciones.setLastAB(gausi.getAb())
        self.sistemaecuaciones.setXns(gausi.getXns())
        self.dialogue = solucionsistemas(self.sistemaecuaciones, gausi.unica, gausi.marcas)
        self.dialogue.show()

    def ingsistemasShow(self):
        self.sistemaecuaciones.setN(self.n.value())
        self.dialogue = ingSistemas(self.sistemaecuaciones,self.n.value())
        self.dialogue.show()

    @pyqtSlot()
    def on_pushButton_clicked(self):
        if(self.sender().text() == "Continuar"):
            if(self.simple.isChecked()):
                print("simple")
                self.sistemaecuaciones.reset()
                self.simpleShow()
            elif(self.parcial.isChecked()):
                print("parcial")
                self.sistemaecuaciones.reset()
                self.parcialShow()
            elif (self.total.isChecked()):
                print("total")
                self.sistemaecuaciones.reset()
                self.totalShow()

        elif(self.sender().text().find("Ingresar") != -1):
            print("ingsistemas")
            self.ingsistemasShow()