import numpy as np


class EliminacionGaussianaTotal:
    def __init__(self):
        self.xns = []
        self.Ab = [[]]
        self.n = 0
        self.unica = True  # Este bool cuando es verdad podemos calcular la solucion, cuando es falsa, no se puede calcular nada
        self.marcas = []
        self.arregloMarcas = []
        self.etapas = []

    def eliminacionGaussianaTotal(self, n, Ab):
        self.Ab = Ab
        self.n = n
        self.marcas = np.arange(1, n + 1)
        self.arregloMarcas.append(np.copy(self.marcas))
        self.etapas.append(np.copy(self.Ab))
        self.xns = [0] * n
        # self.arregloMarcas.append(np.arange(1,n+1).tolist())
        print("Matriz Original")
        self.imprimirMatriz()
        for k in range(1, n):
            print("Etapa " + str(k))
            print("Objetivo: Poner ceros debajo del elemento A" + str(k) + "," + str(k) + "= " + str(
                self.Ab[k - 1][k - 1]))
            print("Multiplicadores:")
            self.pivoteoTotal(k)
            print(self.arregloMarcas)
            if self.unica == False:
                return
            for i in range(k + 1, n + 1):
                multiplicador = self.Ab[i - 1][k - 1] / self.Ab[k - 1][k - 1]
                for j in range(k, n + 2):
                    self.Ab[i - 1][j - 1] = self.Ab[i - 1][j - 1] - multiplicador * self.Ab[k - 1][j - 1]
                print("Multiplicador" + str(i) + "," + str(k) + " : " + str(multiplicador))
            print(" ")
            self.etapas.append(np.copy(self.Ab))
            self.arregloMarcas.append(np.copy(self.marcas).tolist())
            self.imprimirMatriz()
        print("Sustitución Regresiva")
        for i in range(n, 0, -1):
            sumatoria = 0
            for p in range(i + 1, n + 1):
                sumatoria = sumatoria + self.Ab[i - 1][p - 1] * self.xns[p - 1]
            temp = (self.Ab[i - 1][n] - sumatoria) / self.Ab[i - 1][i - 1]
            print("ESTA ES I: ", i)
            self.xns[i - 1] = temp
            print("X" + str(self.marcas[i - 1]) + " = " + str(self.xns[i - 1]))
        self.ordenarX()

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
                print("CAMBIO COL: ", str(k), " con COL: ", str(colMax + 1))
                for j in range(0, len(self.Ab[0]) - 1):
                    aux = self.Ab[j][k - 1]
                    self.Ab[j][k - 1] = self.Ab[j][colMax]
                    self.Ab[j][colMax] = aux
                aux2 = self.marcas[colMax]
                self.marcas[colMax] = self.marcas[k - 1]
                self.marcas[k - 1] = aux2
                print("")
                self.imprimirMatriz()

    def imprimirMatriz(self):
        print('\n'.join(['     '.join(['{:4}'.format(round(item, 2)) for item in row]) for row in self.Ab]))

    def imprimirMatrizEtapas(self):
        for i in self.etapas:
            print('\n'.join(['     '.join(['{:4}'.format(round(item, 2)) for item in row]) for row in i]))
            print(" ")

    def getXns(self):
        return self.xns

    def getAb(self):
        return self.Ab

    def getEtapas(self):
        return self.etapas

    def getArregloMarcas(self):
        return self.arregloMarcas

    def ordenarX(self):
        for index, s in enumerate(self.marcas):
            print(index, s)
            s -= 1
            temp = self.xns[index]
            temp1 = self.marcas[index]
            self.marcas[index] = self.marcas[s]
            self.xns[index] = self.xns[s]
            self.marcas[s] = temp1
            self.xns[s] = temp



    def reset(self):
        self.xns = []
        self.Ab = [[]]
        self.n = 0
        self.arregloMarcas = []
        self.etapas = []


gausi = EliminacionGaussianaTotal()
a = [1, -2, 0.5, -5]
b = [-2, 5, -1.5, 0]
c = [-0.2, 1.75, -1, 10]

e = [a, b, c]

gausi.eliminacionGaussianaTotal(3, e)
print("JOCO")
print(gausi.arregloMarcas)
