import numpy as np

from SistemasEcuaciones.Gaussiana.EliminacionGaussianaTotal import EliminacionGaussianaTotal


class CuadradoNatural:
    def __init__(self):
        self.x = []
        self.xs = []
        self.y = []
        self.tabla = [[0]]
        self.etapas = []
        self.marcas = []
        self.valor = 0
        self.A = [[]]
        self.b = []
        self.n = 0
        self.total = None
        self.solucion = []
        self.funcion = ""
        self.ecuaciones = ""
        self.xns = []
        self.marcasfinales = []

    def cuadradoNatural(self, nroPtos, x, y):
        self.x = x
        self.y = y
        self.total = EliminacionGaussianaTotal()
        self.n = nroPtos - 1
        self.tabla = [[0.0] * ((self.n * 3) + 1) for i in range(self.n * 3)]
        self.b = [0.0] * self.n * 3

        eqNumber = 1
        k = 0
        var = 0
        cont = 1
        print("Etapa 1")
        self.ecuaciones += "Etapa 1 \n"
        for i in range(0, (self.n * 2)):
            exp = 2
            eq = str(eqNumber) + ") "
            for j in range(0, 3):
                self.tabla[i][k + j] = pow(x[var], exp)
                if cont == 1:
                    eq += "a" + str(int(((k / 3) + 1))) + " * " + str(pow(x[var], exp))
                    eq += " + "
                    if self.marcas.count("a" + str(int(((k / 3) + 1)))) == 0:
                        self.marcas.append("a" + str(int(((k / 3) + 1))))
                elif cont == 2:
                    eq += "b" + str(int(((k / 3) + 1))) + " * " + str(pow(x[var], exp))
                    eq += " + "
                    if self.marcas.count("b" + str(int(((k / 3) + 1)))) == 0:
                        self.marcas.append("b" + str(int(((k / 3) + 1))))
                elif cont == 3:
                    eq += "c" + str(int(((k / 3) + 1)))
                    cont = 0
                    if self.marcas.count("c" + str(int(((k / 3) + 1)))) == 0:
                        self.marcas.append("c" + str(int(((k / 3) + 1))))

                cont += 1
                exp -= 1
            self.b[i] = y[var]
            eq += " = " + str(self.b[i])
            self.ecuaciones += eq + "\n"
            print(eq)
            eqNumber += 1
            if (i % 2 == 1):
                k += 3
            else:
                var += 1
        print()
        print("Etapa 2")
        self.ecuaciones += "Etapa 2 \n"
        k = 0
        kaux = k + 3
        m = self.n * 2
        var = 1
        cont2 = 1
        for i in range(0, self.n - 1):
            exp = 1
            eq = str(eqNumber) + ") "
            for j in range(0, 2):
                self.tabla[m + i][k + j] = (2 - j) * pow(x[var], exp)
                self.tabla[m + i][kaux + j] = -(2 - j) * pow(x[var], exp)

                if cont2 == 1:
                    eq += "a" + str(int(((k / 3) + 1))) + "*" + str((2 - j) * pow(x[var], exp))
                    eq += " + "
                    eq += " a" + str(int((kaux / 3) + 1)) + "*" + str((-(2 - j)) * pow(x[var], exp))
                    eq += " + "

                elif cont2 == 2:
                    eq += "b" + str(int((k / 3) + 1))
                    eq += " + "
                    eq += "-b" + str(int((kaux / 3) + 1))
                    cont2 = 0

                cont2 += 1
                exp -= 1

            k += 3
            kaux += 3
            self.b[m + i] = 0
            eq += " = " + str(self.b[m + i])
            self.ecuaciones += eq + "\n"
            print(eq)
            eqNumber += 1
            var += 1
        print()

        print("Etapa 3.")
        self.ecuaciones += "Etapa 3 \n"
        m = m + (self.n - 1)
        var = 0
        exp = 1
        eq = str(eqNumber) + ") "
        self.tabla[m][0] = 2 * pow(x[var], exp)
        eq += "2" + " * a1 "
        self.b[m] = 0
        eq += " = " + str(self.b[m])
        self.ecuaciones += eq + "\n"
        print(eq)

        print()

        for i in range(0, len(self.b)):
            self.tabla[i][3 * self.n] = self.b[i]

        self.total.eliminacionGaussianaTotal(self.n * 3, np.copy(self.tabla))
        self.xns = np.copy(self.total.xns)
        self.marcasfinales = np.copy(self.total.beforeordenar)
        self.solucion = np.copy(self.total.getXns())
        for i in range(0, self.n):
            self.funcion += str(round(self.solucion[i * 3], 2)) + "x^2 + " + str(
                round(self.solucion[(i * 3) + 1], 2)) + "x + " + str(round(self.solucion[(i * 3) + 2], 2))
            self.funcion += " si " + str(self.x[i]) + " ≤ x ≤ " + str(self.x[i + 1]) + "\n"

        self.etapas = np.copy(self.total.etapas)

    def hallarValor(self, valor):
        solucion = self.solucion
        x = self.x
        ind = 0.0
        if valor >= x[0]:
            if valor <= x[len(x) - 1]:
                for i in range(0, len(x) - 1):
                    if (valor >= x[i]) & (valor <= x[i + 1]):
                        ind = i
            else:
                ind = len(x) - 2

        resp = 0
        for i in range(0, 3):
            resp += solucion[(ind * 3) + i] * pow(valor, 2 - i)
        print(solucion)
        print("Resultado:")
        print("f(" + str(valor) + ") = " + str(resp))
        return resp


#cuadrado = CuadradoNatural()

#x = [3, 4.5, 7, 9]
#y = [2.5, 1, 2.5, 0.5]
#valor = 3
#cuadrado.cuadradoNatural(4, x, y)
#print(cuadrado.etapas[0])
#print(cuadrado.etapas[-1])
#print(cuadrado.marcas)
#print(cuadrado.n)
#print(cuadrado.hallarValor(8))
#print(cuadrado)
#print(cuadrado.funcion)
#print(type(cuadrado))