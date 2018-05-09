import numpy as np

class EliminacionGaussianaTotal:
    def __init__(self):
        self.xns = []
        self.Ab = [[]]
        self.n = 0
        self.unica = True  # Este bool cuando es verdad podemos calcular la solucion, cuando es falsa, no se puede calcular nada
        self.marcas = []

    def eliminacionGaussianaTotal(self, n, Ab):
        self.Ab = Ab
        self.n = n
        self.xns = [0] * n
        self.marcas = np.arange(1, n + 1)
        print("Matriz Original")
        self.imprimirMatriz()
        for k in range(1, n):
            print("Etapa " + str(k))
            print("Objetivo: Poner ceros debajo del elemento A" + str(k) + "," + str(k) + "= " + str(
                self.Ab[k - 1][k - 1]))
            print("Multiplicadores:")
            self.pivoteoTotal(k)
            if self.unica == False:
                return
            for i in range(k + 1, n + 1):
                multiplicador = self.Ab[i - 1][k - 1] / self.Ab[k - 1][k - 1]
                for j in range(k, n + 2):
                    self.Ab[i - 1][j - 1] = self.Ab[i - 1][j - 1] - multiplicador * self.Ab[k - 1][j - 1]
                print("Multiplicador" + str(i) + "," + str(k) + " : " + str(multiplicador))
            print(" ")
            self.imprimirMatriz()
        print("Sustitución Regresiva")
        for i in range(n, 0, -1):
            sumatoria = 0
            for p in range(i + 1, n + 1):
                sumatoria = sumatoria + self.Ab[i - 1][p - 1] * self.xns[p - 1]
            temp = (self.Ab[i - 1][n] - sumatoria) / self.Ab[i - 1][i - 1]
            print("ESTA ES I: ", i)
            self.xns[i - 1] = temp
            print("X" + str(self.marcas[i-1]) + " = " + str(self.xns[i - 1]))

    def pivoteoTotal(self, k):
        max = 0
        filaMax = k - 1
        colMax = k - 1
        for i in range(k - 1, self.n):
            for j in range(k - 1, self.n):
                if abs(self.Ab[i][j]) > max:
                    max = abs(self.Ab[i][j])
                    filaMax = i
                    colMax = j
        print("Elemento mayor: ", str(max), " en la fila: ", str(filaMax + 1), " y columna: ", str(colMax + 1))
        if max == 0:
            print("El sistema no tiene solución única!")
            self.unica = False
            return
        elif filaMax != k - 1:
            print("Cambio de fila: ", str(k), " con fila: ", str(filaMax + 1))
            for i in range(0, len(self.Ab[0])):
                aux = self.Ab[k - 1][i]
                self.Ab[k - 1][i] = self.Ab[filaMax][i]
                self.Ab[filaMax][i] = aux
            self.imprimirMatriz()
            if colMax != k - 1:
                for j in range(0, len(self.Ab[0])-1):
                    aux = self.Ab[j][k - 1]
                    self.Ab[j][k - 1] = self.Ab[j][colMax]
                    self.Ab[j][colMax] = aux
                aux2 = self.marcas[colMax]
                self.marcas[colMax] = self.marcas[k - 1]
                self.marcas[k - 1] = aux2
                print("")
                self.imprimirMatriz()

    def imprimirMatriz(self):
        # print('     '.join(str(self.marcas)))
        print('\n'.join(['     '.join(['{:4}'.format(round(item, 2)) for item in row]) for row in self.Ab]))

    def getXns(self):
        return self.xns

    def getAb(self):
        return self.Ab

    def reset(self):
        self.xns = []
        self.Ab = [[]]
        self.n = 0


#gausi = EliminacionGaussianaTotal()
a = [2, -3, 4, 1, 10]
b = [-4, 2, 1, -2, -10]
c = [1, 3, -5, 3, 32]
d = [-3, -1, 1, -1, -21]

e = [a, b, c, d]
#gausi.eliminacionGaussianaTotal(4, e)