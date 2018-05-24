from SistemasEcuaciones.Gaussiana.EliminacionGaussianaTotal import EliminacionGaussianaTotal
import numpy as np

class CubicoNatural:
    def __init__(self):
        self.x = []
        self.y = []
        self.tabla = [[0]]
        self.etapas = []
        self.A = [[]]
        self.b = []
        self.n = 0
        self.total = None
        self.ecuaciones = ""
        self.funcion = ""

    def cubicoNatural(self, nroPtos, x, y):
        self.total = EliminacionGaussianaTotal()
        self.n = nroPtos - 1
        self.tabla = [[0.0] * (self.n * 4 + 1) for i in range((self.n * 4))]
        self.b = [0.0] * self.n * 4
        self.x = x
        self.y = y
        eqNumber = 1
        k = 0
        var = 0
        cont = 1
        print("Etapa 1")
        self.ecuaciones+="Etapa 1 \n"
        for i in range(0, (self.n * 2)):
            exp = 3
            eq = str(eqNumber) + ") "
            for j in range(0, 4):
                self.tabla[i][k + j] = pow(x[var], exp)
                if cont == 1:
                    eq += "a" + str(((k / 4) + 1)) + " * (" + str(x[var]) + ")^" + str(exp)
                    eq += " + "
                elif cont == 2:
                    eq += "b" + str(((k / 4) + 1)) + " * (" + str(x[var]) + ")^" + str(exp)
                    eq += " + "
                elif cont == 3:
                    eq += "c" + str(((k / 4) + 1)) + " * (" + str(x[var]) + ")"
                    eq += " + "
                elif cont == 4:
                    eq += "d" + str(((k / 4) + 1))
                    cont = 0
                cont += 1
                exp -= 1
            self.b[i] = y[var]
            eq += " = " + str(self.b[i])
            self.ecuaciones += eq + "\n"
            print(eq)
            eqNumber += 1
            if (i % 2 == 1):
                k += 4
            else:
                var += 1
        print()
        print("Etapa 2")
        self.ecuaciones+="Etapa 2 \n"
        k = 0
        kaux = k + 4
        m = self.n * 2
        var = 1
        cont2 = 1
        for i in range(0, self.n - 1):
            exp = 2
            eq = str(eqNumber) + ") "
            for j in range(0, 3):
                self.tabla[m + i][k + j] = (3 - j) * pow(x[var], exp)
                self.tabla[m + i][kaux + j] = -(3 - j) * pow(x[var], exp)
                if cont2 == 1:
                    eq += str((3 - j)) + " * a" + str(((k / 4) + 1)) + " * (" + str(x[var]) + ")^" + str(exp)
                    eq += " + "
                    eq += str(-(3 - j)) + " * a" + str(((kaux / 4) + 1)) + " * (" + str(x[var]) + ")^" + str(exp)
                    eq += " + "
                elif cont2 == 2:
                    eq += str((3 - j)) + " * b" + str(((k / 4) + 1)) + " * (" + str(x[var]) + ")"
                    eq += " + "
                    eq += str(-(3 - j)) + " * b" + str(((kaux / 4) + 1)) + " * (" + str(x[var]) + ")"
                    eq += " + "
                elif cont2 == 3:
                    eq += "c" + str(((k / 4) + 1))
                    eq += " + "
                    eq += "-c" + str(((kaux / 4) + 1))
                    cont2 = 0

                cont2 += 1
                exp -= 1

            k += 4
            kaux += 4
            self.b[m + i] = 0
            eq += " = " + str(self.b[m + i])
            print(eq)
            self.ecuaciones += eq + "\n"
            eqNumber += 1
            var += 1
        print()
        print("Etapa 3.")
        self.ecuaciones+="Etapa 3 \n"

        cont3 = 1
        k = 0
        kaux = k + 4
        m = m + (self.n - 1)
        var = 1
        for i in range(0, (self.n - 1)):
            exp = 1
            eq = str(eqNumber) + ") "
            for j in range(0, 2):
                self.tabla[m + i][k + j] = (6 - 4 * j) * pow(x[var], exp)
                self.tabla[m + i][kaux + j] = -(6 - 4 * j) * pow(x[var], exp)
                if cont3 == 1:
                    eq += str((6 - 4 * j)) + " * a" + str(((k / 4) + 1)) + " * (" + str(x[var]) + ")^" + str(exp)
                    eq += " + "
                    eq += str(-(6 - 4 * j)) + " * a" + str(((kaux / 4) + 1)) + " * (" + str(x[var]) + ")^" + str(exp)
                    eq += " + "
                elif cont3 == 2:
                    eq += str((6 - 4 * j)) + " * b" + str(((k / 4) + 1))
                    eq += " + "
                    eq += str(-(6 - 4 * j)) + " * b" + str(((kaux / 4) + 1))
                    cont3 = 0
                cont3 += 1
                exp -= 1
            k += 4
            kaux += 4
            self.b[m + i] = 0
            eq += " = " + str(self.b[m + i])
            print(eq)
            self.ecuaciones += eq + "\n"
            eqNumber += 1
            var += 1
        print()
        print("Etapa 4.")
        self.ecuaciones += "Etapa 4 \n"
        cont4 = 1
        k = 0
        m = m + (self.n - 1)
        var = 0
        for i in range(0, 2):
            exp = 1
            eq = str(eqNumber) + ") "
            for j in range(0, 2):
                self.tabla[m][k + j] = (6 - 4 * j) * pow(x[var], exp)
                if cont4 == 1:
                    eq += str((6 - 4 * j)) + " * a" + str(((k / 4) + 1)) + " * (" + str(x[var]) + ")^" + str(exp)
                    eq += " + "
                elif cont4 == 2:
                    eq += str((6 - 4 * j)) + " * b" + str(((k / 4) + 1))
                    cont4 = 0

                cont4 += 1
                exp -= 1

            self.b[m] = 0
            eq += " = " + str(self.b[m])
            print(eq)
            self.ecuaciones += eq + "\n"
            k = (self.n * 4) - 4
            eqNumber += 1
            m += 1
            var = len(x) - 1
        print()
        for i in range(0, len(self.b)):
            self.tabla[i][4 * self.n] = self.b[i]

        self.total.eliminacionGaussianaTotal(self.n * 4,  np.copy(self.tabla))
        self.etapas = np.copy(self.total.etapas)

    def hallarValor(self, valor):
        solucion = self.total.getXns()
        x = self.x
        ind = 0
        for i in range(1, self.n + 1):
            self.funcion += str(round(solucion[i - 1],2)) + "x^3 + " + str(round(solucion[i],2)) + "x^2 + " + str(round(solucion[i + 1],2)) + "x + " + str(round(solucion[i + 2],2)) + " si " + str(round(x[i - 1],2)) + " ≤ x ≤ " + str(round(x[i],2)) + "\n"
        if valor >= x[0]:
            if valor <= x[len(x) - 1]:
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
        return str(resp)

    def getEtapas(self):
        return self.etapas


cubico = CubicoNatural()


x = [2,3,5]
y = [-1,2,-7]
cubico.cubicoNatural(3,x,y)
print(cubico.hallarValor(2))
print(cubico.ecuaciones)
print(cubico.funcion)

