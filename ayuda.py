from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi
ayudas = dict()
ayudas["unavariablepuntofijo"] = "El método del punto fijo es un método iterativo que permite resolver sistemas de ecuaciones no necesariamente lineales." \
                                 " En particular se puede utilizar para determinar raíces de una función de la forma f(x), siempre y cuando se cumplan los criterios de convergencia." \
                                 " El procedimiento empieza con una estimación de  x, que es mejorada por iteración hasta alcanzar la convergencia. " \
                                 "Para que converja, la derivada {\displaystyle (dg/dx)} debe ser menor que 1 en magnitud (al menos para los valores x que se encuentran durante las iteraciones). " \
                                 "La convergencia será establecida mediante el requisito de que el cambio en x de una iteración a la siguiente no sea mayor en magnitud que alguna pequeña cantidad ε. " \
                                 "Descripcion del metodo: " \
                                 "Paso 0: Elegimos una aproximacion inicial Xo" \
                                 "Paso 1: Sustituimos X0 en g para calcular X1, es decir X1 = g(X0)\
                                  Paso 2: Sustituimos X1 en g para calcular X2, es decir X2 = g(X1)" \
                                 "Paso n: Sustituimos X n-1 em g para calcular Xn, es decir Xn = g (X n-1)"
ayudas["unavariablenewton"] ="Objetivo" \
                             "Buscar una raíz de una función a partir de un valor inicial, una tolerancia y un número de iteraciones, para este caso no es necesario tener un intervalo." \
                             "Generalidades" \
                             "El método de newton por su rapidez y efectividad, es uno de los métodos más utilizados; este método es una variable del método de punto fijo, por lo cual se debe calcular una función g , esta función g se puede calcular de la forma:" \
                             "g(X) = X – (f(X)/f ‘ (x))" \
                             "Una vez definida la función g, se debe realizar los siguientes pasos, como en el método de punto fijo." \
                             " Se debe elegir una aproximación inicial Xo" \
                             "Se calcula X1=g(Xo)" \
                             "Se calcula X2=g(X1)" \
                             "..............   " \
                             "Xn=g(Xn-1)" \
                             "Y se repite el paso anterior hasta llegar a una aproximación de la raiz."
ayudas["unavariablesecante"] ="El método de la secantes una variación del método de Newton, es un método abierto que permite encontrar los ceros o raíces de una función. " \
                              "En vez de usar la derivada, se intenta encontrar un punto de la recta sécate a la curva que tiene una pendiente similar a la recta tangente. "
ayudas["unavariableraicesmultiples"] ="El método de raíces múltiples es muy similar a metodo de Newton-Raphson para resolver ecuaciones que tienen raíces con valores críticos (mínimo, máximo o punto de inflexión), con la particularidad de que en la estructura se debe de hallar la segunda deriva de la función a la cual se le está hallando la raíz." \
                                      " Esto permite tener una mayor seguridad y rapidez en la convergencia. "
ayudas["unavariablebiseccion"] ="El método nos ayuda a encontrar una raíz (punto de corte con el eje X) de una función; Este parte de un intervalo en la función, se debe garantizar que la función sea continúa en todo el intervalo y exista un cambio de signo al evaluar ambos valores iniciales, luego se pasa a calcular el punto medio usando la media aritmetica xm=(xi+xs)/2 y" \
                                " se analiza sí entre el punto xi y xm hay un cambio de signo quiere decir que puedo acotar el intervalo cambiando xs por xm en caso contrario reemplazo xi por xm y vuelvo a calcular el punto medio del intervalo, y asi hasta cumplir al menos una de las siguientes opciones:" \
                                " El error es menor a la tolerancia permitida (establecida por el usuario)" \
                                "Llegar a un máximo de iteraciones " \
                                "Alguno de los puntos hallados (xi,xs,xm) es raíz de la función"
ayudas["unavariablereglafalsa"] ="El método consiste en dividir el intervalo dado, que contiene una raiz, en dos subintervalos." \
                                 " Posee todas las características y condiciones del método de la bisección, excepto por la forma de calcular el punto medio del intervalo." \
                                 "Cálculo del intervalo: xm=xi-  (f(xi)-(xi-xu))/(f(xi)-f(xu)" \
                                 "Se calcula el punto medio y se itera hata encontrar un intervalo que posea la raiz con una tolerancia determinada." \
                                 "Para aplicar el método se debe tener en cuenta:" \
                                 " Si se tiene dos puntos (a, f(a)) y(b, f(b)) y se traza la recta que une a estos dos puntos, se puede observar que un punto esta por debajo del eje x y otro por encima de este, y un punto intermedio (Xm,0), con este punto intermedio se puede comparar los limites y obtener un nuevo intervalo" \
                                 "Si f(A) y f(B)<0, entonces la raíz se encuentra al lado izquierdo del intervalo." \
                                 "Si f(A) y f(B)>0, entonces la raíz se encuentra al lado derecho del intervalo." \
                                 "El método de Regla Falsa converge más rápidamente que el de bisección porque al permanecer uno de sus valores iniciales fijo el número de cálculos se reduce mientras que el otro valor inicial converge hacia la raíz."
ayudas["unavariablebusquedas"] ="Este método se utiliza principalmente como una introducción al método de la bisección con el fin de encontrar un intervalo que contenga una raíz. Consiste en empezar en un extremo del intervalo de interés y evaluar la función con pequeños incrementos a lo largo de dicho intervalo." \
                                "Este método se basa en el teorema del valor intermedio, el cual dice si f es una función continua en el intervalo (a,b) y K es cualquier número entre f(a) y f(b), entonces existe un número C en el intervalo (a,b) tal que f(c) = k." \
                                " Es importante tener que para poder aplicar este método la función f(x) debe ser real y continua en el intervalo dado y que si el incremento es muy pequeño se corre el riesgo de volver el proceso muy dispendioso mientras que si es muy grande se corre el riesgo de no detectar todos los intervalos donde existen raíces." \
                                "Paso a paso:" \
                                "1.   La continuidad de f se debe verificar con argumentos teóricos" \
                                "2.    Elegimos un valor Xo de partida y un deltaX que exprese el tamaño del intervalo que deseamos encontrar" \
                                "3.    Generamos una sucesión de valores X0,X1, … , Xn tal que Xn = Xn-1 + deltaX" \
                                "4.    Cada que se genera un valor de Xn, hallamos el valor de f(Xn)" \
                                "5.    Observamos los signos de f(Xn) y f (xn-1)" \
                                "6.    Se suspende el proceso cuando haya un cambio de signo en f(xn) y f(Xn-1) o cuando se llegue a cierto número de iteraciones."
ayudas["gaussianasimple"] ="El método de eliminación gaussiana simple es un método directo que se descompone en 2 partes" \
                                      "principales que son:" \
                                      "La transformación del sistema de ecuaciones de ecuaciones utilizando las operaciones elementales hasta obtener un sistema de ecuaciones equivalente cuya matriz de coeficientes es una matriz triangular superior." \
                                      "La sustitución regresiva para hallar la solución." \
                                      "El objetivo de este método es iterar sobre la diagonal de la matriz haciendo las operaciones matemáticas correspondientes en cada paso para hacer 0 las posiciones inferiores a la diagonal, resultando en una matriz triangular superior."
ayudas["pivoteototal"] ="En el método de Eliminación Gaussiana con pivoteo total, en cada etapa K, se busca el mayor en valor absoluto de los elementos de la submatriz resultante de eliminar las filas F1 hasta Fk y las columnas C1 hasta Ck-1. Al encontrar el mayor, se realiza el intercambio de filas y columnas para ubicarlo en la posición Abkk." \
                                   "Esto con el fin de que el valor de los multiplicadores sea el más pequeño posible y se reduzca considerablemente el efecto del error de redondeo."
ayudas["pivoteoparcial"] ="Este metodo es una modificacion a la eliminacion Gaussiana simple utilizando intercambios de filas para evitar que los elementos de la diagonal sean cero." \
                                     "En cada etapa K, se busca que el mayor (en valor absoluto) de los elementos de la columna K que ocupan posiciones mayores o iguales que k, ocupen la posicion de la diagonal, es decir se busca el mayor de los elementos en la columna y luego se intercambian las filas para ubicar este valor en la fila k." \
                                     "Al realizar esto se logra que los multiplicadores cumplan la siguiente propiedad:" \
                                     " |Mik| <= 1     ; k+1 < = i < = n" \
                                     "Si se realiza el proceso de eliminacion y se cumple la condicion antes mensionada, logramos que los multiplicadores sean pequeños y que con esto se reduzcan los efectos del error de redondeo"
ayudas["cholesky"] ="La factorización de Cholesky es una derivación de la factorización LU. En este caso se descompone una matriz A en dos matrices, una triangular inferior (L) y una trinagular superior (U), donde la diagonal de U es igual a la diagonal de L." \
                               "Se dice que este método puede llegar a ser dos veces más eficiente que Crout y Doolittle cuando se descompone una matriz A positiva definida con los elementos de su diagonal mayores a 0." \
                               "A= LLt"
ayudas["crout"] ="El método de factorización de crout, es un método de factorización directa LU, donde se factoriza una matriz A en dos matrices, L que es una matriz triangular inferior, y U que es una matriz triangular superior con su diagonal compuesta únicamente por unos." \
                            "El método descompone la matriz, para luego resolver el sistema por medio de las ecuaciones Lz = b y Ux = Z. Se resuelve el sistema por medio de sustitución progresiva y luego una sustitución regresiva."
ayudas["doolittle"] ="El método de factorización de Doolittle, es una variación del método de Doolittle. Es un método de factorización directa LU, donde se factoriza una matriz A en dos matrices, pero en este caso, L que es una matriz triangular inferior, y U que es una matriz triangular superior con su diagonal compuesta únicamente por unos." \
                                "El método descompone la matriz, para luego resolver el sistema por medio de las ecuaciones Lz = b y Ux = Z. Se resuelve el sistema por medio de sustitución progresiva y luego una sustitución regresiva."
ayudas["gauss-seidel"] ="El método de Gauss Seidel es una variación del método de Jacobi, por lo que es un método iterativo basado en punto fijo." \
                                   "En Gauss Seidel, se varía la forma como se sustituyen las variables que permiten calcular los próximos valores. El criterio supone que al conocer el nuevo valor de una de las variables, este valor nuevo se utiliza para determinar el valor de las que faltan." \
                                   "Esto es:" \
                                   "Para determinar x´1 utilizamos los valores previos de x2, x3,x4." \
                                   "Para determinar x´2 utilizamos los valores previos de x3,x4 y el valor actual x´1." \
                                   "Para determinar x´3 utilizamos el valor previo de x4 y los valores actuales x´1 y x´2." \
                                   "Para determinar x´4 utilizamos los valores actuales x´1, x´2 y x´3."
ayudas["jacobi"] ="El método de Jacobi es un método iterativo basado en punto fijo, por lo que se pretende resolver el sistema de ecuaciones lineales Ax = b a partir de un vector inicial x0 que sirve como aproximación al vector solución x. Del mismo modo, con x0 se genera x1, con x1 se genera x2, y así sucesivamente  de la forma:" \
                             "Xn+1= G(xn)" \
                             "De este modo, se pretende que el vector aproximado Xn+1 converja a la solución del sistema"
class ayuda(QDialog):

    def __init__(self, ayudade):
        super(ayuda, self).__init__()
        loadUi('UI/ayuda.ui', self)
        self.setWindowTitle('Ayuda')
        self.ayuda.setText(ayudas[ayudade])