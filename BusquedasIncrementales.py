import numpy as np
class BusquedasIncrementales:
    def __init__(self):
        self.xn = []
        self.fxn = []
    def busquedasIncrementales(self,x0, xdelta, i, funciones):
        self.xn.append(x0)
        def funcion(x):
            result = funciones.calculateFx(x)
            self.fxn.append(result)
            return result

        y0 = funcion(x0)
        if y0 != 0:
            x1 = np.float64(x0 + xdelta)
            y1 = funcion(x1)
            cont = 1
            self.xn.append(x1)
            while (y1*y0 > 0) & (cont < i):
                x0 = x1
                y0 = y1
                x1 = x0 + xdelta
                y1 = funcion(x1)
                cont += 1
                self.xn.append(x1)
            if y1 == 0:
                result = str(x1) + " es una raiz"
            elif y0*y1 < 0:
                result = "La raiz esta entre " + str(x0) + " y " + str(x1)
            else:
               result = "No se encontro una raiz"
        else:
            result = str(x0) + " es una raiz"
        return result

    def getXn(self):
        return self.xn
    def getFxn(self):
        return self.fxn
    def reset(self):
        self.xn = []
        self.fxn = []
