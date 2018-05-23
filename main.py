from Funciones import Funciones
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi
from Params.paramBisec import paramBisec
from Params.paramBusquedas import paramBusquedas
from Params.paramNewton import paramNewton
from Params.paramPunto import paramPunto
from Params.paramRaices import paramRaices
from Params.paramRegla import paramRegla
from Params.paramSecante import paramSecante
from Datos import datos


class main(QDialog):
    def __init__(self):
        super(main,self).__init__()
        loadUi('UI/paginaprincipal.ui',self)
        self.funciones = Funciones()
        self.setWindowTitle('Página principal')
        self.continuar.clicked.connect(self.on_pushButton_clicked)
        self.ingfuncion.clicked.connect(self.on_pushButton_clicked)
        self.botongraficar.clicked.connect(self.on_pushButton_clicked)


    def paramBusquedasShow(self):
        self.dialogue = paramBusquedas(self.funciones)
        self.dialogue.show()
        #self.solucionWindow.show()

    def paramBiseccionShow(self):
        self.dialogue = paramBisec(self.funciones)
        self.dialogue.show()

    def paramReglaFalsaShow(self):
        self.dialogue = paramRegla(self.funciones)
        self.dialogue.show()

    def paramPuntoFijoShow(self):
        self.dialogue = paramPunto(self.funciones)
        self.dialogue.show()

    def paramNewtonShow(self):
        self.dialogue = paramNewton(self.funciones)
        self.dialogue.show()

    def paramSecanteShow(self):
        self.dialogue = paramSecante(self.funciones)
        self.dialogue.show()

    def paramRaicesShow(self):
        self.dialogue = paramRaices(self.funciones)
        self.dialogue.show()

    def datosShow(self):
        self.dialogue = datos(self.funciones)
        self.dialogue.show()

    @pyqtSlot()
    def on_pushButton_clicked(self):
        if(self.sender().text() == "Continuar"):
            if(self.Busquedas.isChecked()):
                print("busquedas")
                self.paramBusquedasShow()
            elif(self.Grafico.isChecked()):
                #TODO
                print("grafico")
            elif (self.Biseccion.isChecked()):
                print("biseccion")
                self.paramBiseccionShow()
            elif (self.Regla.isChecked()):
                self.paramReglaFalsaShow()
                print("regla")
            elif (self.Punto.isChecked()):
                self.paramPuntoFijoShow()
                print("punto")
            elif (self.Newton.isChecked()):
                self.paramNewtonShow()
                print("newton")
            elif (self.Secante.isChecked()):
                self.paramSecanteShow()
                print("secante")
            elif (self.Raices.isChecked()):
                self.paramRaicesShow()
                print("raices")
        elif(self.sender().text().find("Ingresar") != -1):
            self.datosShow()
        elif (self.sender().text().find("Graficar") != -1):
            self.funciones.graficar()





            #app = QApplication(sys.argv)
#widget = main()
#widget.show()
#sys.exit(app.exec())