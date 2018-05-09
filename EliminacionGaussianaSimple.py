import numpy as np
class EliminacionGaussianaSimple:
    def __init__(self):
        self.xns = []
        self.Ab = [[]]
        self.n = 0
        self.etapas =[]

    def eliminacionGaussianaSimple(self, n, Ab):
        self.Ab = Ab
        self.n = n
        self.xns = [0] * n
        self.etapas = [0] * n
        print("Matriz Original")
        self.imprimirMatriz()
        for k in range(1, n):
            print("Etapa " + str(k))
            print("Objetivo: Poner ceros debajo del elemento Ab" + str(k) + "," + str(k) + "= " + str(
                self.Ab[k - 1][k - 1]))
            print("Multiplicadores:")
            for i in range(k + 1, n + 1):
                multiplicador = self.Ab[i - 1][k - 1] / self.Ab[k - 1][k - 1]
                for j in range(k, n + 2):
                    self.Ab[i - 1][j - 1] = self.Ab[i - 1][j - 1] - multiplicador * self.Ab[k - 1][j - 1]
                print("Multiplicador" + str(i) + "," + str(k) + " : " + str(multiplicador))
            print(" ")
            self.etapas[k-1] = np.copy(self.Ab)
            print("Etapa:  ", str(k))
            print(self.etapas[k-1])
            print("")
            self.imprimirMatriz()
        print("Sustitución Regresiva")
        for i in range(n, 0, -1):
            sumatoria = 0
            for p in range(i + 1, n + 1):
                sumatoria = sumatoria + self.Ab[i - 1][p - 1] * self.xns[p - 1]
            temp = (self.Ab[i - 1][n] - sumatoria) / self.Ab[i - 1][i - 1]
            print("ESTA ES I: ", i)
            self.xns[i - 1] = temp
            print("X" + str(i) + " = " + str(self.xns[i - 1]))


    def getXns(self):
        return self.xns

    def getAb(self):
        return self.Ab

    def getEtapas(self):
        return self.etapas

    def imprimirMatriz(self):
        print('\n'.join(['     '.join(['{:4}'.format(round(item, 2)) for item in row]) for row in self.Ab]))

    def imprimirMatrizEtapas(self):
        print('\n'.join(['     '.join(['{:4}'.format(round(item, 2)) for item in row]) for row in self.etapas]))

    def reset(self):
        self.xns = []
        self.Ab = [[]]
        self.n = 0
        self.etapas = []
