import numpy as np

class Secante:
    def __init__(self):
        self.xns = []
        self.fxns = []
        self.errores = []
        self.errores.append(0)
        self.errores.append(0)

    def secante(self, x0, x1, tol, n, respuesta, funciones):
        self.xns.append(x0)
        self.xns.append(x1)

        def f(x):
            #result = x ** 3 + 4 * x ** 2 - 10
            result = funciones.calculateFx(x)

            self.fxns.append(result)
            return result

        fx0 = f(x0)
        if fx0 == 0:
            return ("Xo es raiz")
        else:
            fx1 = f(x1)
            cont = 0
            err = tol + 1
            den = fx1 - fx0
            while (err > tol) & (fx1 != 0) & (den != 0) & (cont < n):
                x2 = x1 - fx1 * (x1 - x0) / den
                self.xns.append(x2)
                if respuesta == True:
                    err = float(abs(x2 - x1))
                else:
                    err = float(abs((x2 - x1) / x2))
                self.errores.append(err)
                x0 = x1
                fx0 = fx1
                x1 = x2
                fx1 = f(x1)
                den = fx1 - fx0
                cont = cont + 1

            if (fx1 == 0):
                return (str(x1) + " es raiz")
            elif (err < tol):
                return (str(x1) + "es aproximacion a una raiz con una tolerancia = " + str(tol))
            elif (den == 0):
                return ("Hay una posible raiz multiple")
            else:
                return ("fracaso en " + str(n) + "iteraciones")

    def getXns(self):
        return self.xns

    def getFxns(self):
        return self.fxns

    def getErrores(self):
        return self.errores

    def reset(self):
        self.xns = []
        self.fxns = []
        self.errores = []