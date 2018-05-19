class FuncionInterpolacion:
    x = []
    y = []
    npuntos = 0

    def setX(self,x):
        self.x = x
    def setY(self,y):
        self.y = y
    def setNpuntos(self,n):
        self.npuntos = n
    def addPunto(self,x,y):
        self.x.append(x)
        self.y.append(y)
        self.npuntos+=1

