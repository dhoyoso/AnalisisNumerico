import numpy as np


class Lineal:
    def __init__(self):
        self.x = []
        self.y = []
        self.n = 0
        self.funcion = ""
        self.b = []
        self.m = []

    def lineal(self,nroPuntos, x, y):
        self.n = nroPuntos - 1
        self.x = x
        self.y = y
        for i in range(len(x) - 1):
            mi = (y[i + 1] - y[i]) / (x[i + 1] - x[i])
            bi = -(mi * x[i]) + y[i]
            self.b.append(np.copy(bi))
            self.m.append(np.copy(mi))
            self.funcion += str(round(mi, 2)) + "X + " + str(round(bi, 2))+ " si "+str(round(x[i], 2)) + " ≤ x ≤ "+ str(round(x[i+1], 2))+ "\n"

    def hallarValor(self, valor):
        for i in range(0,(self.n)):
            if (valor >= self.x[i]) & (valor <= self.x[i + 1]):
                print(self.m[i])
                return (self.m[i] * valor) + self.b[i]


x = [1.0, 3.0,5.0]
y = [1.0,6.0,25.0]

gausi = Lineal()
gausi.lineal(3,x, y)
print(gausi.hallarValor(5))
print(gausi.funcion)
