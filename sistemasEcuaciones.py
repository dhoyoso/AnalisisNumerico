from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi
import numpy as np
from SistemasEcuaciones.Gaussiana.EliminacionGaussianaParcial import EliminacionGaussianaParcial
from SistemasEcuaciones.Gaussiana.EliminacionGaussianaSimple import EliminacionGaussianaSimple
from SistemasEcuaciones.Gaussiana.EliminacionGaussianaTotal import EliminacionGaussianaTotal
from Sistemas import Sistemas
from SistemasEcuaciones.FactorizacionDirecta.factorizacionLUCholesky import FactorizacionLUCholesky
from SistemasEcuaciones.FactorizacionDirecta.factorizacionLUCrout import FactorizacionLUCrout
from SistemasEcuaciones.FactorizacionDirecta.factorizacionLUDoolittle import FactorizacionLUDoolittle
from ingSistemas import ingSistemas
from SistemasEcuaciones.Iterativos.jacobi import Jacobi
from SistemasEcuaciones.Iterativos.seidel import Seidel
from Soluciones.solucionFactorizacionDirecta import SolucionFactorizacionDirecta
from Soluciones.solucionIterativos import SolucionIterativos
from Soluciones.solucionsistemas import solucionsistemas
from valoresIniciales import ValoresIniciales
from ayuda import ayuda


class sistemasEcuaciones(QDialog):
    def __init__(self):
        super(sistemasEcuaciones, self).__init__()
        loadUi('UI/sistemasecuaciones.ui', self)
        self.sistemaecuaciones = Sistemas()
        self.setWindowTitle('Sistemas de ecuaciones')
        self.continuar.clicked.connect(self.on_pushButton_clicked)
        self.ingsistema.clicked.connect(self.on_pushButton_clicked)
        self.ayuda.clicked.connect(self.on_pushButton_clicked)
        self.valores_iniciales.clicked.connect(self.on_pushButton_clicked)
        self.valores_iniciales.setEnabled(False)
        self.valores_iniciales.setDisabled(True)

    def simpleShow(self):
        gausi = EliminacionGaussianaSimple()
        gausi.eliminacionGaussianaSimple(self.n.value(), np.copy(self.sistemaecuaciones.AB))
        self.sistemaecuaciones.setAB(gausi.getAb())
        self.sistemaecuaciones.setLastAB(gausi.getAb())
        self.sistemaecuaciones.setXns(gausi.getXns())
        self.sistemaecuaciones.setEtapas(gausi.getEtapas())
        self.dialogue = solucionsistemas(self.sistemaecuaciones, gausi.unica, [])
        self.dialogue.show()

    def parcialShow(self):
        gausi = EliminacionGaussianaParcial()
        gausi.eliminacionGaussianaParcial(self.n.value(), np.copy(self.sistemaecuaciones.AB))
        self.sistemaecuaciones.setAB(gausi.getAb())
        self.sistemaecuaciones.setLastAB(gausi.getAb())
        self.sistemaecuaciones.setXns(gausi.getXns())
        self.sistemaecuaciones.setEtapas(gausi.getEtapas())
        self.dialogue = solucionsistemas(self.sistemaecuaciones, gausi.unica, [])
        self.dialogue.show()

    def totalShow(self):
        gausi = EliminacionGaussianaTotal()
        gausi.eliminacionGaussianaTotal(self.n.value(), np.copy(self.sistemaecuaciones.AB))
        self.sistemaecuaciones.setAB(gausi.getAb())
        self.sistemaecuaciones.setLastAB(gausi.getAb())
        self.sistemaecuaciones.setXns(gausi.getXns())
        self.sistemaecuaciones.setEtapas(gausi.getEtapas())
        self.dialogue = solucionsistemas(self.sistemaecuaciones, gausi.unica, gausi.getArregloMarcas())
        self.dialogue.show()

    def doolittleShow(self):
        gausi = FactorizacionLUDoolittle()
        gausi.factorizacionLUDoolittle(np.copy(self.sistemaecuaciones.A), np.copy(self.sistemaecuaciones.B), self.n.value())
        self.sistemaecuaciones.setXns(gausi.getXns())
        self.sistemaecuaciones.setEtapasL(gausi.getEtapasL())
        self.sistemaecuaciones.setEtapasU(gausi.getEtapasU())
        self.sistemaecuaciones.setZns(gausi.getZns())
        self.dialogue = SolucionFactorizacionDirecta(self.sistemaecuaciones, gausi.unica, [])
        self.dialogue.show()

    def croutShow(self):
        gausi = FactorizacionLUCrout()
        gausi.factorizacionLUCrout(np.copy(self.sistemaecuaciones.A), np.copy(self.sistemaecuaciones.B), self.n.value())
        self.sistemaecuaciones.setXns(gausi.getXns())
        self.sistemaecuaciones.setEtapasL(gausi.getEtapasL())
        self.sistemaecuaciones.setEtapasU(gausi.getEtapasU())
        self.sistemaecuaciones.setZns(gausi.getZns())
        self.dialogue = SolucionFactorizacionDirecta(self.sistemaecuaciones, gausi.unica, [])
        self.dialogue.show()

    def choleskyShow(self):
        gausi = FactorizacionLUCholesky()
        gausi.factorizacionLUCholesky(np.copy(self.sistemaecuaciones.A), np.copy(self.sistemaecuaciones.B), self.n.value())
        self.sistemaecuaciones.setXns(gausi.getXns())
        self.sistemaecuaciones.setEtapasL(gausi.getEtapasL())
        self.sistemaecuaciones.setEtapasU(gausi.getEtapasU())
        self.sistemaecuaciones.setZns(gausi.getZns())
        self.dialogue = SolucionFactorizacionDirecta(self.sistemaecuaciones, gausi.unica, [])
        self.dialogue.show()

    def jacobiShow(self):
        gausi = Jacobi()
        print("ceros "+str(self.sistemaecuaciones.xceros)+" "+str(self.sistemaecuaciones.numiter)+" "+str(self.sistemaecuaciones.tol)+' '+str(self.sistemaecuaciones.lamb))
        gausi.jacobi(np.copy(self.sistemaecuaciones.A), np.copy(self.sistemaecuaciones.B), self.n.value(),
                     np.copy(self.sistemaecuaciones.xceros), self.sistemaecuaciones.numiter, self.sistemaecuaciones.tol,
                     self.sistemaecuaciones.lamb)
        print(gausi.getEtapas())
        self.sistemaecuaciones.setIteraciones(gausi.getEtapas())
        print('ETAPAS' + str(self.sistemaecuaciones.iteraciones))
        self.dialogue = SolucionIterativos(self.sistemaecuaciones)
        self.dialogue.show()

    def seidelShow(self):
        gausi = Seidel()
        print("ceros "+str(self.sistemaecuaciones.xceros)+" "+str(self.sistemaecuaciones.numiter)+" "+str(self.sistemaecuaciones.tol)+' '+str(self.sistemaecuaciones.lamb))
        gausi.seidel(np.copy(self.sistemaecuaciones.A), np.copy(self.sistemaecuaciones.B), self.n.value(),
                     np.copy(self.sistemaecuaciones.xceros), self.sistemaecuaciones.numiter, self.sistemaecuaciones.tol,
                     self.sistemaecuaciones.lamb)
        print(gausi.getEtapas())
        self.sistemaecuaciones.setIteraciones(gausi.getEtapas())
        print('ETAPAS' + str(self.sistemaecuaciones.iteraciones))
        self.dialogue = SolucionIterativos(self.sistemaecuaciones)
        self.dialogue.show()

    def valoresShow(self):
        self.dialogue = ValoresIniciales(self.sistemaecuaciones)
        self.dialogue.show()

    def ingsistemasShow(self):
        self.sistemaecuaciones.setN(self.n.value())
        self.dialogue = ingSistemas(self.sistemaecuaciones, self.n.value())
        self.dialogue.show()
        self.valores_iniciales.setEnabled(True)
        self.valores_iniciales.setDisabled(False)

    @pyqtSlot()
    def on_pushButton_clicked(self):
        if self.sender().text() == "Continuar":
            if self.simple.isChecked():
                print("simple")
                self.sistemaecuaciones.reset()
                self.simpleShow()
            elif self.parcial.isChecked():
                print("parcial")
                self.sistemaecuaciones.reset()
                self.parcialShow()
            elif self.total.isChecked():
                print("total")
                self.sistemaecuaciones.reset()
                self.totalShow()
            elif self.doolittle.isChecked():
                print("doolittle")
                self.sistemaecuaciones.reset()
                self.doolittleShow()
            elif self.crout.isChecked():
                print("crout")
                self.sistemaecuaciones.reset()
                self.croutShow()
            elif self.cholesky.isChecked():
                print("cholesky")
                self.sistemaecuaciones.reset()
                self.choleskyShow()
            elif self.seidel.isChecked():
                print("seidel")
                self.sistemaecuaciones.reset()
                self.seidelShow()
            elif self.jacobi.isChecked():
                print("jacobi")
                self.sistemaecuaciones.reset()
                self.jacobiShow()

        elif (self.sender().text().find("Valores") != -1):
            print("valoresIniciales")
            self.valoresShow()
        elif (self.sender().text().find("Ingresar") != -1):
            print("ingsistemas")
            self.ingsistemasShow()
        elif (self.sender().text() == "Ayuda"):
            if self.simple.isChecked():
                print("simple")
                self.dialogue = ayuda("gaussianasimple")
                self.dialogue.show()
            elif self.parcial.isChecked():
                print("parcial")
                self.dialogue = ayuda("pivoteoparcial")
                self.dialogue.show()
            elif self.total.isChecked():
                print("total")
                self.dialogue = ayuda("pivoteototal")
                self.dialogue.show()
            elif self.doolittle.isChecked():
                print("doolittle")
                self.dialogue = ayuda("doolittle")
                self.dialogue.show()
            elif self.crout.isChecked():
                print("crout")
                self.dialogue = ayuda("crout")
                self.dialogue.show()
            elif self.cholesky.isChecked():
                print("cholesky")
                self.dialogue = ayuda("cholesky")
                self.dialogue.show()
            elif self.seidel.isChecked():
                print("seidel")
                self.dialogue = ayuda("gauss-seidel")
                self.dialogue.show()
            elif self.jacobi.isChecked():
                print("jacobi")
                self.dialogue = ayuda("jacobi")
                self.dialogue.show()
