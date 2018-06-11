import numpy as np

class PuntoFijo:
    def __init__(self):
        self.gxns = []
        self.fxns = []
        self.errores = []
        self.errores.append(0)

    def puntoFijo(self, x0, tol, n, respuesta,funciones):
        def f(x):
            x = float(x)
            y = funciones.calculateFx(x)
            self.fxns.append(y)
            return y
        def g(x):
            y = funciones.calculateGx(x)
            self.gxns.append(y)
            return y
        self.gxns.append(x0)
        xm = 0
        y0 = f(x0)
        if y0 != 0:
            err = tol + 1
            i = 0
            while (y0 != 0) & (err > tol) & (i < n):
                x1 = g(x0)
                if respuesta == True:
                    err = float(abs(x1 - x0))
                else:
                    err = float(abs((x1 - x0) / x1))

                self.errores.append(err)
                y0 = f(x1)
                x0 = x1
                i += 1
            if y0 == 0:
                return ("La raíz es: " + str(x0))
            elif err < tol:
                return "Termino por la tolerancia, la raiz aproximada seria: " + str(x0)
            else:
                return "se cumplio el # de iteraciones, la raíz aproximada sería: " + str(x0)
        else:
            return "La raíz es: " + str(x0)

    def getGxns(self):
        return self.gxns

    def getFxns(self):
        return self.fxns

    def getErrores(self):
        return self.errores

    def reset(self):
        self.gxns = []
        self.fxns = []
        self.errores = []