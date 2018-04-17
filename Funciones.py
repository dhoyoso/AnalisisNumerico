import numpy as np
import math

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

# TODO no se guarda fx!!!