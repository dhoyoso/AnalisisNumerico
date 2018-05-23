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
from ayuda import ayuda


class main(QDialog):
    def __init__(self):
        super(main,self).__init__()
        loadUi('UI/paginaprincipal.ui',self)
        self.funciones = Funciones()
        self.setWindowTitle('Página principal')
        self.continuar.clicked.connect(self.on_pushButton_clicked)
        self.ingfuncion.clicked.connect(self.on_pushButton_clicked)
        self.botongraficar.clicked.connect(self.on_pushButton_clicked)
        self.ayuda.clicked.connect(self.on_pushButton_clicked)



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
        elif (self.sender().text() == "Ayuda"):
            if (self.Busquedas.isChecked()):
                print("busquedas")
                self.dialogue = ayuda("unavariablebusquedas")
                self.dialogue.show()
            elif (self.Biseccion.isChecked()):
                print("biseccion")
                self.dialogue = ayuda("unavariablebiseccion")
                self.dialogue.show()
            elif (self.Regla.isChecked()):
                self.dialogue = ayuda("unavariablereglafalsa")
                self.dialogue.show()
                print("regla")
            elif (self.Punto.isChecked()):
                self.dialogue = ayuda("unavariablepuntofijo")
                self.dialogue.show()
                print("punto")
            elif (self.Newton.isChecked()):
                self.dialogue = ayuda("unavariablenewton")
                self.dialogue.show()
                print("newton")
            elif (self.Secante.isChecked()):
                self.dialogue = ayuda("unavariablesecante")
                self.dialogue.show()
                print("secante")
            elif (self.Raices.isChecked()):
                self.dialogue = ayuda("unavariableraicesmultiples")
                self.dialogue.show()
                print("raices")





            #app = QApplication(sys.argv)
#widget = main()
#widget.show()
#sys.exit(app.exec())