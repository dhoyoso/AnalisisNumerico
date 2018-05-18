from copy import deepcopy


class Sistemas:
    A = [[]]  # matriz
    B = []  # vector independiente b.
    AB = [[]]  # matriz aumentada.
    lastAB = [[]]
    xns = []
    n = 0
    inicialAB = [[]]
    etapas = []
    etapasL = []
    etapasU = []
    zns = []
    xceros = []
    iteraciones = []
    lamb = None
    numiter = 0
    tol = 0

    def setInicialAB(self, a):
        self.inicialAB = a

    def setA(self, a):
        self.A = a

    def setB(self, b):
        self.B = b

    def setAB(self, ab):
        self.AB = deepcopy(ab)

    def setLastAB(self, x):
        self.lastAB = x

    def setIteraciones(self, x):
        self.iteraciones = x

    def setXns(self, x):
        self.xns = x

    def setZns(self, z):
        self.zns = z

    def setN(self, n):
        self.n = n

    def setLamb(self,x):
        self.lamb = x

    def setNumiter(self,x):
        self.numiter = x

    def setTol(self,x):
        self.tol = x

    def setEtapas(self, etapas):
        self.etapas = etapas

    def setEtapasL(self, etapas):
        self.etapasL = etapas

    def setEtapasU(self, etapas):
        self.etapasU = etapas

    def setXceros(self,x):
        self.xceros = x

    def reset(self):
        self.AB = deepcopy(self.inicialAB)  # matriz aumentada.
        self.lastAB = [[]]
        self.xns = []
        self.etapas = []
        self.etapasL = []
        self.etapasU = []
        self.zns = []
