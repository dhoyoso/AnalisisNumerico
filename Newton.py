import numpy as np

class Newton:
    def __init__(self):
        self.xns = []
        self.fxns = []
        self.fpxns = []
        self.errores = []
        self.errores.append(0)

    def newton(self, x0, tol, n, respuesta, funciones):
        self.xns.append(x0)

        def f(x):
            x = float(x)
            # Se debe poner la funcion que corresponda
            y = funciones.calculateFx(x)
            self.fxns.append(y)
            return y

        def fp(x):
            # Se debe poner la funcion que corresponda
            y = funciones.calculateFpx(x)
            self.fpxns.append(y)
            return y

        xm = 0

        y0 = f(x0)
        yp0 = fp(x0)

        if y0 != 0:
            err = tol + 1
            i = 0
            while (y0 != 0) & (err > tol) & (i < n) & (yp0 != 0):
                x1 = x0 - (y0 / yp0)
                if respuesta == True:
                    err = float(abs(x1 - x0))
                else:
                    err = float(abs((x1 - x0) / x1))
                self.errores.append(err)
                y0 = f(x1)
                yp0 = fp(x1)
                x0 = x1
                self.xns.append(x0)
                i += 1
            if y0 == 0:
                return("La raíz es: " + str(x0))
            elif err < tol:
                return("se cumplio la tolerancia, la raiz aproximada seria: " + str(x0))
            elif yp0 == 0:
                return ("la derivada es cero.")
            else:
                return ("paro por # de iteraciones maximas, la raíz aproximada sería: " + str(x0))
        else:
            return ("La raíz es: " + str(x0))

    def getXns(self):
        return self.xns

    def getFxns(self):
        return self.fxns

    def getFpxns(self):
        return self.fpxns

    def getErrores(self):
        return self.errores

    def reset(self):
        self.xns = []
        self.fxns = []
        self.fpxns = []
        self.errores = []