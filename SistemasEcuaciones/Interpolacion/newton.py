class NewtonInterpolacion:
    def __init__(self):
        self.x = []
        self.y = []
        self.tabla = [[]]
        self.valor = 0
        self.n = 0

    def newtonInterpolacion(self, nroPtos, x, y):
        self.x = x
        self.y = y
        self.n = nroPtos
        self.tabla = [[0] * (self.n) for i in range(self.n)]
        for i in range(0, self.n):
            self.tabla[i][0] = y[i]
        for i in range(1, self.n):
            for i in range(1, i + 1):
                self.tabla[i][i] = (self.tabla[i][i - 1] - self.tabla[i - 1][i - 1]) / (x[i] - x[i - i])
        print("Tabla de datos:")
        self.imprimirMatriz()
        print("Polinomio interpolante:")
        bi = self.tabla[0][0]
        pol = "P(x): " + str(bi)
        temp = ""
        aux = 1
        for i in range(1, self.n):
            temp = temp + "(x - " + str(x[i - 1]) + ")"
            if self.tabla[i][i] > 0:
                pol = pol + "\n" + "      + " + str(round(self.tabla[i][i], 2)) + " * " + temp
            else:
                pol = pol + "\n" + "       " + str(round(self.tabla[i][i], 2)) + " * " + temp
            aux = aux * (self.valor - x[i - 1])
            bi = bi + self.tabla[i][i] * aux
        print(pol)

    def imprimirMatriz(self):
        print('\n'.join(['     '.join(['{:4}'.format(round(item, 2)) for item in row]) for row in self.tabla]))

    def hallarvalor(self):
        bi = self.tabla[0][0]
        aux = 1
        for i in range(1, self.n):
            aux = aux * (self.valor - self.x[i - 1])
            bi = bi + self.tabla[i][i] * aux
        return bi


    def reset(self):
        self.xns = []
        self.Ab = [[]]
        self.n = 0


gausi = NewtonInterpolacion()

x = [1, 1.2, 1.4, 1.6, 1.8]
y = [-0.620907, 0.640927, 2.234099, 4.183599, 6.513606]

gausi.newtonInterpolacion(5, x, y)
