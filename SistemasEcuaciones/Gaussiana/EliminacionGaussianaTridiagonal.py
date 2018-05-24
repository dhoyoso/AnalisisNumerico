class EliminacionGaussianaTridiagonal:
    def __init__(self):
        self.a = []
        self.b = []
        self.c = []
        self.bb = []
        self.unica = True
        self.matrix = [[]]

    def eliminacionGaussianaTridiagonal(self, n, a, b, c, bb):
        self.a = a
        self.b = b
        self.c = c
        self.bb = bb
        self.n = n
        self.matrix = [[0.0] * n for i in range(self.n)]
        if(a.indexOf(0)!= -1) | (a.indexOf(0)!=-1) | (a.indexOf(0)!=1) | (a.indexOf(0)!=-1):
            self.unica = False
            print("No tiene solución única!")
            return
        for i in range(0, self.n):
            self.matrix[i][i] = b[i]
            if (n - i) != 1:
                self.matrix[i][i + 1] = c[i]
                self.matrix[i + 1][i] = a[i]

        print("Matriz A: ")
        self.imprimirMatriz()
        for k in range(0, (self.n - 1)):
            multiplicador = a[k] / b[k]
            b[k + 1] = b[k + 1] - multiplicador * c[k]
            bb[k + 1] = bb[k + 1] - multiplicador * bb[k]

        for i in range(0, self.n):
            for j in range(0, self.n):
                self.matrix[i][j] = 0

        for i in range(0, self.n):
            self.matrix[i][i] = b[i]
            if (n - i) != 1:
                self.matrix[i][i + 1] = c[i]

        x = self.sustitucionRegresiva()
        print(x)

    def sustitucionRegresiva(self):
        x = [1] * self.n

        for i in range((self.n - 1), -1, -1):
            suma = 0
            for j in range((i + 1), self.n):
                suma += self.matrix[i][j] * x[j]
            x[i] = (self.bb[i] - suma) / self.matrix[i][i]

        return x

    def imprimirMatriz(self):
        print('\n'.join(['     '.join(['{:4}'.format(round(item, 2)) for item in row]) for row in self.matrix]))


#gausi = EliminacionGaussianaTridiagonal()

a = [5, -3, 2, 4, 7]
b = [4, 8, 7, -5, 10, 15]
c = [3, 2, 2, 2, 2]
bb = [23, 18, 19, 2, 12, -50]

#gausi.eliminacionGaussianaTridiagonal(6, a, b, c, bb)
