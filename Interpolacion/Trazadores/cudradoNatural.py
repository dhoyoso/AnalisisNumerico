from AnalisisNumerico.SistemasEcuaciones.Gaussiana.EliminacionGaussianaTotal import EliminacionGaussianaTotal
import numpy as np

class CuadradoNatural:
    def __init__(self):
        self.x = []
        self.y = []
        self.tabla = [[0]]
        self.valor = 0
        self.A = [[]]
        self.b = []
        self.n = 0
        self.total = None

    def cuadradoNatural(self, nroPtos, valor, x, y):
        self.total = EliminacionGaussianaTotal()
        self.n = nroPtos-1
        self.tabla = [[0] * ((self.n * 3) + 1) for i in range(self.n * 3)]
        self.b = [0] * self.n * 3

        eqNumber = 1
        k = 0
        var = 0
        cont = 1
        print("Etapa 1")
        for i in range(0, (self.n * 2)):
            exp = 2
            eq = str(eqNumber) + ") "
            for j in range(0, 3):
                self.tabla[i][k + j] = pow(x[var], exp)
                if cont == 1:
                    eq += "a" + str(((k / 3) + 1)) + str(pow(x[var], exp))
                    eq += " + "
                elif cont == 2:
                    eq += "b" + str(((k / 3) + 1)) + str(pow(x[var], exp))
                    eq += " + "
                elif cont == 3:
                    eq += "c" + str(((k / 3) + 1))
                    cont = 0

                cont += 1
                exp -= 1
            self.b[i] = y[var]
            eq += " = " + str(self.b[i])
            print(eq)
            eqNumber += 1
            if (i % 2 == 1):
                k += 3
            else:
                var += 1
        print()
        print("Etapa 2")
        k = 0
        kaux = k + 3
        m = self.n *2
        var = 1
        cont2 = 1
        for i in range(0, self.n - 1):
            exp = 1
            eq = str(eqNumber) + ") "
            for j in range(0, 2):
                self.tabla[m + i][k + j] = (2 - j) * pow(x[var], exp)
                self.tabla[m + i][kaux + j] = -(2 - j) * pow(x[var], exp)

                if cont2 == 1:
                    eq += "a" + str(((k / 2) + 1)) + "*" +str((2 - j) * pow(x[var], exp))
                    eq += " + "
                    eq += " a" + str(((kaux / 2) + 1)) +  "*" +str((-(2 - j)) * pow(x[var], exp))
                    eq += " + "
                elif cont2 == 2:
                    eq += "b" +  "*" +str(((k / 2) + 1))
                    eq += " + "
                    eq += "-b" +  "*" +str(((kaux / 2) + 1))
                    cont2 = 0

                cont2 += 1
                exp -= 1

            k += 3
            kaux += 3
            self.b[m + i] = 0
            eq += " = " + str(self.b[m + i])
            print(eq)
            eqNumber += 1
            var += 1
        print()

        print("Etapa 4.")
        m = m + (self.n - 1)
        var = 0
        exp = 1
        eq = "9" + ") "
        self.tabla[m][0] = 2 * pow(x[var], exp)
        eq += "2" + " * a1.0 "
        self.b[m] = 0
        eq += " = " + str(self.b[m])
        print(eq)

        print()

        for i in range(0, len(self.b)):
            self.tabla[i][3 * self.n] = self.b[i]

        self.total.eliminacionGaussianaTotal(self.n * 3,  np.copy(self.tabla))
        solucion = self.total.getXns()
        ind = 0
        if valor >= x[0]:
            if valor <= x[len(x)-1]:
                for i in range(0, len(x) - 1):
                    if (valor >= x[i]) & (valor < x[i + 1]):
                        ind = i
            else:
                ind = len(x) - 2

        resp = 0
        for i in range(0, 3):
            resp += solucion[(ind * 3) + i] * pow(valor, 2 - i)
        print (solucion)
        print("Resultado:")
        print("f(" + str(valor) + ") = " + str(resp))


cuadrado = CuadradoNatural()

x = [3,4.5,7,9]
y = [2.5,1,2.5,0.5]
valor = 5
cuadrado.cuadradoNatural(4, valor, x, y)
