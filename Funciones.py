import numpy as np
import math
import numpy as npy
import pylab as plb

class Funciones:
    Fx = ""
    Fpx = ""
    Fppx = ""
    Gx = ""

    def setFx(self,funcion):
        self.Fx = funcion
        print (self.Fx)

    def setFpx(self,funcion):
        self.Fpx = funcion

    def setFppx(self,funcion):
        self.Fppx = funcion

    def setGx(self,funcion):
        self.Gx = funcion

    def calculateFx(self,value):
        print(str(value) +" "+ self.Fx)
        x = value
        return eval(self.Fx)

    def calculateFpx(self,value):
        print(str(value) + " " + self.Fpx)
        x = value
        return eval(self.Fpx)

    def calculateFppx(self,value):
        x = value
        return eval(self.Fppx)

    def calculateGx(self,value):
        x = value
        return eval(self.Gx)

    def graficar(self):
        # Nos da un arreglo con 256 elementos en el intervalo [a,b] para graficarlos
        x = npy.linspace(-50,50, 1000, endpoint=True)
        # Funcion que vamos a graficar con los valores de x generados.
        if(self.Fx!=""):
            fx = eval(self.Fx)
            plb.plot(x, fx, color='purple', label='Fx')
        if (self.Fpx != ""):
            fpx = eval(self.Fpx)
            plb.plot(x, fpx, color='black', label="F\'x")
        if (self.Fppx != ""):
            fppx = eval(self.Fppx)
            plb.plot(x, fppx, color='orchid', label="F\'\'x")
        if (self.Gx != ""):
            gx = eval(self.Gx)
            plb.plot(x, gx, color='blueviolet', label='Gx')
        plb.grid(True)
        plb.xlabel("X")
        plb.ylabel("Y")
        # Valores sobre el eje X
        plb.legend(loc='best')
        #plb.plot(X, ejeX)

        plb.show()

#
# fun = Funciones()
# fun.setFx("(X ** 3) - 0.5")
# fun.setFpx("(X ** 2) - 0.5")
# fun.setFppx("(X ** 5) - 0.5")
# fun.setGx("(X ** 4) - 0.5")
# fun.graficar()

