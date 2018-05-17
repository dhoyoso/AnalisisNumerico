class Lagrange:
    def __init__(self):
        self.x = []
        self.y = []
        self.tabla = [[]]
        self.valor = 0
        self.n = 0

    def lagrange(self, nroPtos, valor, x, y):
        self.x = x
        self.y = y
        self.valor = valor
        self.n = nroPtos

        print("Construcion L(x):")
        resultado = 0
        pol = "p(x) "
        for k in range(0, self.n):
            productoria = 1
            numerador = ""
            denominador = ""
            for i in range(0, self.n):
                if i is not k:
                    productoria = productoria * (valor - self.x[i]) / (self.x[k] - self.x[i])
                    numerador = numerador + "(x - " + str(self.x[i]) + ")"
                    denominador = denominador + "(" + str(self.x[k]) + " - " + str(self.x[i]) + ")"

            termino = numerador + " / " + denominador
            print("L" + str(k) + "(x): " + termino)
            if self.y[k] > 0:
                pol = pol + "      + " + str(round(y[k],2)) + " * [" + termino + "]\n"
            else:
                pol = pol + "  " + str(round(y[k],2)) + " * [" + termino + "]\n"
            resultado += productoria * y[k]
        print("Polinomio interpolante: ")
        print(pol)
        print("Resultado:")
        print("f(" + str(valor) + ") = " + str(round(resultado,2)))

    def imprimirMatriz(self):
        # print('     '.join(str(self.marcas)))
        print('\n'.join(['     '.join(['{:4}'.format(round(item, 2)) for item in row]) for row in self.tabla]))

    def reset(self):
        self.xns = []
        self.Ab = [[]]
        self.n = 0


gausi = Lagrange()

x = [1, 1.2, 1.4, 1.6, 1.8]
y = [-0.620907, 0.640927, 2.234099, 4.183599, 6.513606]

gausi.lagrange(5, 2, x, y)
