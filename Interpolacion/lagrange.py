class Lagrange:
    def __init__(self):
        self.x = []
        self.y = []
        self.tabla = [[]]
        self.n = 0
        self.pol = ""
        self.Lxs = ""

    def lagrange(self, nroPtos, x, y):
        self.x = x
        self.y = y
        self.n = nroPtos
        self.pol = ""

        for k in range(0, self.n):
            numerador = ""
            denominador = ""
            for i in range(0, self.n):
                if i is not k:
                    numerador = numerador + "(x - " + str(self.x[i]) + ")"
                    denominador = denominador + "(" + str(self.x[k]) + " - " + str(self.x[i]) + ")"

            termino = numerador + " / " + denominador
            self.Lxs += "L" + str(k) + "(x): " + termino + "\n"
            if self.y[k] > 0:
                aux = " + "
                if(k == 0):
                    aux = ""
                self.pol = self.pol + aux + str(round(y[k],6)) + " * (" + termino + ") "
            else:
                self.pol = self.pol + "  " + str(round(y[k],6)) + " * (" + termino + ") "

        print(self.pol)
        print(self.Lxs)

    def imprimirMatriz(self):
        # print('     '.join(str(self.marcas)))
        print('\n'.join(['     '.join(['{:4}'.format(round(item, 2)) for item in row]) for row in self.tabla]))

    def hallarvalor(self,valor):
        resultado = 0
        for k in range(0, self.n):
            productoria = 1
            for i in range(0, self.n):
                if i is not k:
                    productoria = productoria * (valor - self.x[i]) / (self.x[k] - self.x[i])

            resultado += productoria * self.y[k]
        return round(resultado,3)

    def reset(self):
        self.xns = []
        self.Ab = [[]]
        self.n = 0


gausi = Lagrange()

x = [1, 1.2, 1.4, 1.6, 1.8]
y = [-0.620907, 0.640927, 2.234099, 4.183599, 6.513606]

gausi.lagrange(5, x, y)
print(gausi.hallarvalor(1.45))