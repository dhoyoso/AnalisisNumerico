class Biseccion:
    def __init__(self):
        self.xis=[]
        self.fxis=[]
        self.xus = []
        self.fxus = []
        self.xms = []
        self.fxms = []
        self.errores = []

    def biseccion(self,xi,xu,tol,n, respuesta, funciones):
        def f(x):
            result = funciones.calculateFx(x)
            return result

        self.xis.append(xi)
        self.xus.append(xu)

       # respuesta = input("Escriba true si desea error absoluto, false si decea error relativo")

        yi = f(xi)
        self.fxis.append(yi)
        if (yi != 0):
            yu = f(xu)
            self.fxus.append(yu)
            if (yu != 0):
                if ((yi * yu) < 0):
                    xm = (xu + xi) / 2
                    self.xms.append(xm)
                    ym = f(xm)
                    self.fxms.append(ym)
                    error = tol + 1
                    self.errores.append(0)
                    cont = 1

                    while ((ym != 0) & (error > tol) & (cont < n)):

                        if (ym * yi < 0):
                            xu = xm
                            yu = ym
                        else:
                            xi = xm
                            yi = ym

                        xma = xm
                        xm = (xi + xu) / 2

                        if (respuesta == True):
                            error = float(abs(xma - xm))
                        else:
                            error = float(abs((xma - xm) / xma))

                        cont = cont + 1
                        ym = f(xm)
                        self.xms.append(xm)
                        self.xis.append(xi)
                        self.xus.append(xu)
                        self.fxis.append(yi)
                        self.fxus.append(yu)
                        self.fxms.append(ym)
                        self.errores.append(error)

                    if (ym == 0):
                        return "Xm es una raiz en: " + str(xm)
                    elif (error < tol):
                        return "Paro por la tolerancia, la raiz aproximada seria: " + str(xm)
                    else:
                        return "Paro por el # de iteraciones, la raiz aproximada seria: " + str(xm)
                else:
                    return "No hay raiz en el intervalo"
            else:
                return "Xu es una raiz y su valor es: " + str(xu)

        else:
            return "Xi es una raiz y su valor es: " + str(xi)
    def getXis(self):
        return self.xis
    def getFxis(self):
        return self.fxis
    def getXus(self):
        return self.xus
    def getFxus(self):
        return self.fxus
    def getXms(self):
        return self.xms
    def getFxms(self):
        return self.fxms
    def getErrores(self):
        return self.errores
    def reset(self):
        self.xis = []
        self.fxis = []
        self.xus = []
        self.fxus = []
        self.xms = []
        self.fxms = []
        self.errores = []