import numpy as np
class DiferenciacionNumerica:
    def __init__(self):
        self.x0 = 0
        self.funcion = ''

    def diferenciacionNumericaDosPuntos(self,funcion,x0,h):

        self.funcion = funcion
        print(self.funcion)
        print("Diferenciacion numerica de dos punto: ")
        print("X: ",str(x0))
        dif = DiferenciacionNumerica()
        resultado = (dif.calculateFx(x0+h,funcion) - dif.calculateFx(x0,funcion))/h
        print("Resulatado: ")
        print("f´(", str(x0), "): ", str(resultado))

    def diferenciacionNumericaTresPuntosAtras(self,funcion,x0,h):

        self.funcion = funcion
        print(self.funcion)
        print("Diferenciacion numerica de tres puntos atras: ")
        print("X: ",str(x0))
        dif = DiferenciacionNumerica()
        resultado = ((dif.calculateFx(x0-2*h,funcion)-4*dif.calculateFx(x0-h,funcion)+3*dif.calculateFx(x0,funcion))/(2*h))
        print("Resulatado: ")
        print("f´(", str(x0), "): ", str(resultado))

    def diferenciacionNumericaTresPuntosDelante(self,funcion,x0,h):

        self.funcion = funcion
        print(self.funcion)
        print("Diferenciación numérica con tres puntos adelante: ")
        print("X: ",str(x0))
        dif = DiferenciacionNumerica()
        resultado = ((-dif.calculateFx(x0+2*h,funcion)+4*dif.calculateFx(x0+h,funcion)-3*dif.calculateFx(x0,funcion))/(2*h))
        print("Resulatado: ")
        print("f´(", str(x0), "): ", str(resultado))

    def diferenciacionNumericaTresPuntosCentral(self,funcion,x0,h):

        self.funcion = funcion
        print(self.funcion)
        print("Diferenciación numérica con tres puntos central: ")
        print("X: ",str(x0))
        dif = DiferenciacionNumerica()
        resultado =  ((-dif.calculateFx(x0-h,funcion)+dif.calculateFx(x0+h,funcion))/(2*h))
        print("Resulatado: ")
        print("f´(", str(x0), "): ", str(resultado))

    def diferenciacionNumericaCincoPuntosCentrada(self,funcion,x0,h):

        self.funcion = funcion
        print(self.funcion)
        print("Diferenciación numérica con cinco puntos centrada: ")
        print("X: ",str(x0))
        dif = DiferenciacionNumerica()
        resultado =  ((dif.calculateFx(x0-2*h,funcion)-8*dif.calculateFx(x0-h,funcion)+8*dif.calculateFx(x0+h,funcion)
                       -dif.calculateFx(x0+2*h,funcion))/(12*h))
        print("f´(", str(x0), "): ", str(resultado))

    def diferenciacionNumericaCincoPuntosAdelante(self,funcion,x0,h):

        self.funcion = funcion
        print(self.funcion)
        print("Diferenciación numérica con cinco puntos adelante: ")
        print("X: ",str(x0))
        dif = DiferenciacionNumerica()
        resultado =  (-25*(dif.calculateFx(x0,funcion)+48*dif.calculateFx(x0+h,funcion)-36*dif.calculateFx(x0+2*h,funcion)
                           +16*dif.calculateFx(x0+3*h,funcion)-3*dif.calculateFx(x0+4*h,funcion))/(12*h))
        print("f´(", str(x0), "): ", str(resultado))

    def diferenciacionNumericaCincoPuntosAtras(self,funcion,x0,h):

        self.funcion = funcion
        print(self.funcion)
        print("Diferenciación numérica con cinco puntos atras: ")
        print("X: ",str(x0))
        dif = DiferenciacionNumerica()
        resultado =   (25*(dif.calculateFx(x0,funcion)-48*dif.calculateFx(x0-h,funcion)+36*dif.calculateFx(x0-2*h,funcion)
                           -16*dif.calculateFx(x0-3*h,funcion)+3*dif.calculateFx(x0-4*h,funcion))/(12*h))
        print("f´(", str(x0), "): ", str(resultado))


    def calculateFx(self, value,funcion):
        print(funcion)
        print(str(value), " " , funcion)
        x = value
        return  eval(funcion)


dif = DiferenciacionNumerica()

funcion = 'np.exp(-x)-6*x\r\n'
dif.diferenciacionNumericaDosPuntos(funcion,2.2,0.1)

