import numpy as np
class Neville:
    def __init__(self):
        self.x = []
        self.y = []
        self.tabla = [[]]
        self.valor = 0
        self.n = 0
        self.resultado = 0

    def interpolacion_neville(self,num_puntos, valor, x, y):
        self.tabla = np.zeros((num_puntos, num_puntos))
        self.x = x
        self.y = y
        for i in range(num_puntos):
            self.tabla[i][0] = self.y[i]

        for i in range(num_puntos):
            for j in range(1, i + 1):
                self.tabla[i][j] = ((valor - self.x[i - j]) * self.tabla[i][j - 1] - ((valor - self.x[i]) * self.tabla[i - 1][j - 1])) / (
                self.x[i] - self.x[i - j])

        self.resultado = self.tabla[num_puntos - 1][num_puntos - 1]

    def imprimirMatriz(self):
        print('\n'.join(['     '.join(['{:4}'.format(round(item, 2)) for item in row]) for row in self.tabla]))

    def reset(self):
        self.xns = []
        self.Ab = [[]]
        self.n = 0

gausi = Neville()

x = [2,3,5]
y = [-1,2,-7]

gausi.interpolacion_neville(3,4, x, y)
gausi.imprimirMatriz()
print(gausi.resultado)
