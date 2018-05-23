from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi


class datos(QDialog):

    def __init__(self, funciones):
        super(datos, self).__init__()
        loadUi('UI/datos.ui', self)
        self.setWindowTitle('Datos')
        self.funciones = funciones
        self.continuar.clicked.connect(self.on_pushButton_clicked)
        if(funciones.Fx!=""):
            self.Fx.setText(self.funciones.Fx)
        if (funciones.Fpx != ""):
            self.Fpx.setText(self.funciones.Fpx)
        if (funciones.Fppx != ""):
            self.Fppx.setText(self.funciones.Fppx)
        if (funciones.Gx != ""):
            self.Gx.setText(self.funciones.Gx)



    @pyqtSlot()
    def on_pushButton_clicked(self):
        self.funciones.setFx(self.Fx.text())
        self.funciones.setFpx(self.Fpx.text())
        self.funciones.setFppx(self.Fppx.text())
        self.funciones.setGx(self.Gx.text())
        self.close()

