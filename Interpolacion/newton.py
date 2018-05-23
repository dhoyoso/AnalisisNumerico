class NewtonInterpolacion:
    def __init__(self):
        self.x = []
        self.y = []
        self.tabla = [[]]
        self.valor = 0
        self.n = 0
        self.pol = ""

    def newtonInterpolacion(self, nroPtos, x, y):
        self.x = x
        self.y = y
        self.n = nroPtos
        self.tabla = [[0] * (self.n) for i in range(self.n)]
        for i in range(0, self.n):
            self.tabla[i][0] = y[i]
        for i in range(1, self.n):
            for j in range(1, i + 1):
                self.tabla[i][j] = (self.tabla[i][j - 1] - self.tabla[i - 1][j - 1]) / (x[i] - x[i - j])
        print("Tabla de datos:")
        self.imprimirMatriz()
        print("Polinomio interpolante:")
        bi = self.tabla[0][0]
        pol =  str(bi)
        temp = ""
        aux = 1
        for i in range(1, self.n):
            temp = temp + "(x-" + str(x[i - 1]) + ")"
            if self.tabla[i][i] > 0:
                pol = pol  + "+" + str(round(self.tabla[i][i], 6)) + "*" + temp
            else:
                pol = pol  + str(round(self.tabla[i][i], 6)) + "*" + temp
            aux = aux * (self.valor - x[i - 1])
            bi = bi + self.tabla[i][i] * aux
        print(pol)
        self.pol = pol

    def imprimirMatriz(self):
        print('\n'.join(['     '.join(['{:4}'.format(round(item, 2)) for item in row]) for row in self.tabla]))

    def hallarvalor(self,valor):
        bi = self.tabla[0][0]
        aux = 1
        for i in range(1, self.n):
            aux = aux * (valor - self.x[i - 1])
            bi = bi + self.tabla[i][i] * aux
        return bi


    def reset(self):
        self.xns = []
        self.Ab = [[]]
        self.n = 0


#gausi = NewtonInterpolacion()

#x = [1, 1.2, 1.4, 1.6, 1.8]
#y = [-0.620907, 0.640927, 2.234099, 4.183599, 6.513606]

#gausi.newtonInterpolacion(5, x, y)
