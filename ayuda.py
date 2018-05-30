from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi
ayudas = dict()
ayudas["unavariablepuntofijo"] = "El método del punto fijo es un método iterativo que permite resolver sistemas de ecuaciones no necesariamente lineales.\n"" \
""En particular se puede utilizar para determinar raíces de una función de la forma f(x), siempre y cuando se cumplan los criterios de convergencia.\n" \
                                 "El procedimiento empieza con una estimación de  x, que es mejorada por iteración hasta alcanzar la convergencia.\n " \
                                 "Para que converja, la derivada (dg/dx) debe ser menor que 1 en magnitud (al menos para los valores x que se encuentran durante las iteraciones).\n " \
                                 "La convergencia será establecida mediante el requisito de que el cambio en x de una iteración a la siguiente no sea mayor en magnitud que alguna pequeña cantidad ε.\n\n " \
                                 "Descripcion del método:\n " \
                                 "Paso 0: Elegimos una aproximacion inicial Xo \n" \
                                 "Paso 1: Sustituimos X0 en g para calcular X1, es decir X1 = g(X0)\n" \
                                 "Paso 2: Sustituimos X1 en g para calcular X2, es decir X2 = g(X1)\n" \
                                 "Paso n: Sustituimos X n-1 em g para calcular Xn, es decir Xn = g (X n-1)\n"
ayudas["unavariablenewton"] ="Objetivo \n" \
                             "Buscar una raíz de una función a partir de un valor inicial, una tolerancia y un número de iteraciones, para este caso no es necesario tener un intervalo.\n\n" \
                             "Generalidades\n" \
                             "El método de newton por su rapidez y efectividad, es uno de los métodos más utilizados; este método es una variable del método de punto fijo, por lo cual se debe calcular una función g , esta función g se puede calcular de la forma:\n" \
                             "g(X) = X – (f(X)/f ‘ (x))\n\n" \
                             "Una vez definida la función g, se debe realizar los siguientes pasos, como en el método de punto fijo.\n" \
                             "- Se debe elegir una aproximación inicial Xo \n" \
                             "- Se calcula X1=g(Xo)\n" \
                             "- Se calcula X2=g(X1) \n" \
                             "- .............. \n " \
                             "- Xn=g(Xn-1) \n" \
                             "Y se repite el paso anterior hasta llegar a una aproximación de la raiz. \n"
ayudas["unavariablesecante"] ="El método de la secantes una variación del método de Newton, es un método abierto que permite encontrar los ceros o raíces de una función.\n " \
                              "En vez de usar la derivada, se intenta encontrar un punto de la recta sécate a la curva que tiene una pendiente similar a la recta tangente. "
ayudas["unavariableraicesmultiples"] ="El método de raíces múltiples es muy similar a metodo de Newton-Raphson para resolver ecuaciones que tienen raíces con valores críticos (mínimo, máximo o punto de inflexión), con la particularidad de que en la estructura se debe de hallar la segunda deriva de la función a la cual se le está hallando la raíz." \
                                      "Esto permite tener una mayor seguridad y rapidez en la convergencia. "
ayudas["unavariablebiseccion"] ="El método nos ayuda a encontrar una raíz (punto de corte con el eje X) de una función; Este parte de un intervalo en la función, se debe garantizar que la función sea continúa en todo el intervalo y exista un cambio de signo al evaluar ambos valores iniciales, luego se pasa a calcular el punto medio usando la media aritmetica xm=(xi+xs)/2 y" \
                                "se analiza sí entre el punto xi y xm hay un cambio de signo quiere decir que puedo acotar el intervalo cambiando xs por xm en caso contrario reemplazo xi por xm y vuelvo a calcular el punto medio del intervalo, y asi hasta cumplir al menos una de las siguientes opciones: \n\n" \
                                "- El error es menor a la tolerancia permitida (establecida por el usuario) \n" \
                                "- Llegar a un máximo de iteraciones \n " \
                                "- Alguno de los puntos hallados (xi,xs,xm) es raíz de la función "
ayudas["unavariablereglafalsa"] ="El método consiste en dividir el intervalo dado, que contiene una raiz, en dos subintervalos.\n" \
                                 "Posee todas las características y condiciones del método de la bisección, excepto por la forma de calcular el punto medio del intervalo. \n\n" \
                                 "Cálculo del intervalo: xm = xi- (f(xi)-(xi-xu))/(f(xi)-f(xu)\n" \
                                 "Se calcula el punto medio y se itera hata encontrar un intervalo que posea la raiz con una tolerancia determinada. \n\n" \
                                 "Para aplicar el método se debe tener en cuenta:\n" \
                                 "Si se tiene dos puntos (a, f(a)) y(b, f(b)) y se traza la recta que une a estos dos puntos, se puede observar que un punto esta por debajo del eje x y otro por encima de este, y un punto intermedio (Xm,0), con este punto intermedio se puede comparar los limites y obtener un nuevo intervalo \n\n" \
                                 "- Si f(A) y f(B)<0, entonces la raíz se encuentra al lado izquierdo del intervalo. \n" \
                                 "- Si f(A) y f(B)>0, entonces la raíz se encuentra al lado derecho del intervalo. \n" \
                                 "El método de Regla Falsa converge más rápidamente que el de bisección porque al permanecer uno de sus valores iniciales fijo el número de cálculos se reduce mientras que el otro valor inicial converge hacia la raíz."
ayudas["unavariablebusquedas"] ="Este método se utiliza principalmente como una introducción al método de la bisección con el fin de encontrar un intervalo que contenga una raíz. \nConsiste en empezar en un extremo del intervalo de interés y evaluar la función con pequeños incrementos a lo largo de dicho intervalo.\n" \
                                "Este método se basa en el teorema del valor intermedio, el cual dice si f es una función continua en el intervalo (a,b) y K es cualquier número entre f(a) y f(b), entonces existe un número C en el intervalo (a,b) tal que f(c) = k. \n" \
                                "Es importante tener que para poder aplicar este método la función f(x) debe ser real y continua en el intervalo dado y que si el incremento es muy pequeño se corre el riesgo de volver el proceso muy dispendioso mientras que si es muy grande se corre el riesgo de no detectar todos los intervalos donde existen raíces.\n\n" \
                                "Paso a paso:\n" \
                                "1.   La continuidad de f se debe verificar con argumentos teóricos \n" \
                                "2.   Elegimos un valor Xo de partida y un deltaX que exprese el tamaño del intervalo que deseamos encontrar \n" \
                                "3.   Generamos una sucesión de valores X0,X1, … , Xn tal que Xn = Xn-1 + deltaX \n" \
                                "4.   Cada que se genera un valor de Xn, hallamos el valor de f(Xn) \n" \
                                "5.   Observamos los signos de f(Xn) y f (xn-1) \n" \
                                "6.   Se suspende el proceso cuando haya un cambio de signo en f(xn) y f(Xn-1) o cuando se llegue a cierto número de iteraciones.\n"
ayudas["gaussianasimple"] ="El método de eliminación gaussiana simple es un método directo que se descompone en 2 partes " \
                                      "principales que son: \n\n" \
                                      "- La transformación del sistema de ecuaciones de ecuaciones utilizando las operaciones elementales hasta obtener un sistema de ecuaciones equivalente cuya matriz de coeficientes es una matriz triangular superior.\n" \
                                      "- La sustitución regresiva para hallar la solución.\n\n" \
                                      "El objetivo de este método es iterar sobre la diagonal de la matriz haciendo las operaciones matemáticas correspondientes en cada paso para hacer 0 las posiciones inferiores a la diagonal, resultando en una matriz triangular superior."
ayudas["pivoteototal"] ="En el método de Eliminación Gaussiana con pivoteo total, en cada etapa K, se busca el mayor en valor absoluto de los elementos de la submatriz resultante de eliminar las filas F1 hasta Fk y las columnas C1 hasta Ck-1. Al encontrar el mayor, se realiza el intercambio de filas y columnas para ubicarlo en la posición Abkk. \n" \
                        "Al realizar el cambio de columnas se debe tener en cuenta que se altera el orden de las variables en el sistema. \n" \
                        "El pivoteo total coloca sobre la diagonal los valores mayores posibles de cada submatriz. Los multiplicadores conservan la misma propiedad del pivoteo parcial. \n" \
                        "Esto con el fin de que el valor de los multiplicadores sea el más pequeño posible y se reduzca considerablemente el efecto del error de redondeo. \n"
ayudas["pivoteoparcial"] ="Este metodo es una modificacion a la eliminacion Gaussiana simple utilizando intercambios de filas para evitar que los elementos de la diagonal sean cero." \
                                     "En cada etapa K, se busca que el mayor (en valor absoluto) de los elementos de la columna K que ocupan posiciones mayores o iguales que k, ocupen la posicion de la diagonal, es decir se busca el mayor de los elementos en la columna y luego se intercambian las filas para ubicar este valor en la fila k.\n" \
                                     "Al realizar esto se logra que los multiplicadores cumplan la siguiente propiedad:\n" \
                                     "|Mik| <= 1     ; k+1 < = i < = n \n" \
                                     "Si se realiza el proceso de eliminacion y se cumple la condicion antes mensionada, logramos que los multiplicadores sean pequeños y que con esto se reduzcan los efectos del error de redondeo"
ayudas["cholesky"] ="La factorización de Cholesky es una derivación de la factorización LU. En este caso se descompone una matriz A en dos matrices, una triangular inferior (L) y una trinagular superior (U), donde la diagonal de U es igual a la diagonal de L. \n" \
                               "Se dice que este método puede llegar a ser dos veces más eficiente que Crout y Doolittle cuando se descompone una matriz A positiva definida con los elementos de su diagonal mayores a 0.\n" \
                               "A= LLt"
ayudas["crout"] ="El método de factorización de crout, es un método de factorización directa LU, donde se factoriza una matriz A en dos matrices, L que es una matriz triangular inferior, y U que es una matriz triangular superior con su diagonal compuesta únicamente por unos." \
                            "El método descompone la matriz, para luego resolver el sistema por medio de las ecuaciones Lz = b y Ux = Z. Se resuelve el sistema por medio de sustitución progresiva y luego una sustitución regresiva."
ayudas["doolittle"] ="El método de factorización de Doolittle, es una variación del método de Doolittle. Es un método de factorización directa LU, donde se factoriza una matriz A en dos matrices, pero en este caso, L que es una matriz triangular inferior, y U que es una matriz triangular superior con su diagonal compuesta únicamente por unos.\n" \
                                "El método descompone la matriz, para luego resolver el sistema por medio de las ecuaciones Lz = b y Ux = Z.\n Se resuelve el sistema por medio de sustitución progresiva y luego una sustitución regresiva."
ayudas["gauss-seidel"] ="El método de Gauss Seidel es una variación del método de Jacobi, por lo que es un método iterativo basado en punto fijo.\n" \
                                   "En Gauss Seidel, se varía la forma como se sustituyen las variables que permiten calcular los próximos valores. El criterio supone que al conocer el nuevo valor de una de las variables, este valor nuevo se utiliza para determinar el valor de las que faltan.\n\n" \
                                   "Esto es:\n" \
                                   "- Para determinar x´1 utilizamos los valores previos de x2, x3,x4.\n" \
                                   "- Para determinar x´2 utilizamos los valores previos de x3,x4 y el valor actual x´1.\n" \
                                   "- Para determinar x´3 utilizamos el valor previo de x4 y los valores actuales x´1 y x´2.\n" \
                                   "- Para determinar x´4 utilizamos los valores actuales x´1, x´2 y x´3.\n"
ayudas["jacobi"] ="El método de Jacobi es un método iterativo basado en punto fijo, por lo que se pretende resolver el sistema de ecuaciones lineales Ax = b a partir de un vector inicial x0 que sirve como aproximación al vector solución x. Del mismo modo, con x0 se genera x1, con x1 se genera x2, y así sucesivamente  de la forma:\n" \
                             "Xn+1= G(xn)\n" \
                             "De este modo, se pretende que el vector aproximado Xn+1 converja a la solución del sistema"

ayudas["newtondiferencias"] = "Este método se basa en la utilización de las diferencias divididas. Se utiliza para determinar un polinomio de a lo sumo grado n con n+1 puntos. \n" \
                              "Es una alternativa más eficiente a la utilización de la matriz de vandermonde, ya que esta se obtiene por recurrencia utilizando resultados obtenidos en las recurrencias anteriores. \n" \
                              "Se usa en el caso que los puntos en el eje x se encuentran espaciados de forma arbitraria y provienen de una función desconocida pero supuestamente diferenciable.\n" \
                              "Las diferencias sirven para evaluar los coeficientes y obtener el polinomio de interpolacion:\n" \
                              "fn(x) = f(x0) + (x – x0) f[x1, x0] + (x – x0)(x – x1) f[x2, x1, x0]" \
                              "+ · · · + (x – x0)(x – x1)· · ·(x – xn–1) f[xn, xn–1,· · ·, x0] \n"

ayudas["lagrange"] = "El método de Lagrange es una reformulación del polinomio de Newton con el que se evita el cálculo de las diferencias divididas. \n" \
                     "Se busca construir el polinomio interpolador de grado n que pasa por n+1 puntos. \n" \
                     "El polinomio está dado de la forma P(x) = f(x0)Ln0(x)+…..+F(xn)Lnn(x) \n" \
                     "Donde  para cada k=0,1…..,n \n"

ayudas["lineal"] = "Este es el caso más sencillo. En él, vamos a interpolar una función f(x) de la que se nos dan un número N de pares (x,f(x)) por los que tendrá que pasar nuestra función polinómica P(x). Esta serie de funciones nuestras van a ser lineales, esto es, con grado 1: de la forma P(x) = ax + b. \ n" \
                   "Definiremos una de estas funciones por cada par de puntos adyacentes, hasta un total de (N-1) funciones, haciéndolas pasar obligatoriamente por los puntos que van a determinarlas, es decir, la función P(x) será el conjunto de segmentos que unen nudos consecutivos; es por ello que nuestra función será continua en dichos puntos, pero no derivable en general. "
ayudas["cuadratico"] = "En este caso, los polinomios P(x) a través de los que construimos el Spline tienen grado 2. Esto quiere decir, que va a tener la forma P(x) = ax² + bx + c \n" \
                       "Como en la interpolación segmentaria lineal, vamos a tener N-1 ecuaciones (donde N son los puntos sobre los que se define la función). La interpolación cuadrática nos va a asegurar que la función que nosotros generemos a trozos con los distintos P(x) va a ser continua, ya que para sacar las condiciones que ajusten el polinomio, vamos a determinar como condiciones: \n\n" \
                       "- Que las partes de la función a trozos P(x) pasen por ese punto. Es decir, que las dos Pn(x) que rodean al f(x) que queremos aproximar, sean igual a f(x) en cada uno de estos puntos. \n" \
                       "- Que la derivada en un punto siempre coincida para ambos \"lados\" de la función definida a trozos que pasa por tal punto común. \nEsto sin embargo no es suficiente, y necesitamos una condición más. ¿Por qué?. Tenemos 3 incógnitas por cada P(x). En un caso sencillo con f(x) definida en tres puntos y dos ecuaciones P(x) para aproximarla, vamos a tener seis incógnitas en total. Para resolver esto necesitaríamos seis ecuaciones, pero vamos a tener tan sólo cinco: cuatro que igualan el P(x) con el valor de f(x) en ese punto (dos por cada intervalo), y la quinta al igualar la derivada en el punto común a las dos P(x). \n" \
                       "Se necesita una sexta ecuación,¿de dónde se extrae? Esto suele hacerse con el valor de la derivada en algún punto, al que se fuerza uno de los P(x).  \n"
ayudas["cubico"] = "En este caso, cada polinomio P(x) a través del que construimos los Splines en [m,n] tiene grado 3. Esto quiere decir, que va a tener la forma P(x) = ax³ + bx² + cx + d \n\n" \
                   "En este caso vamos a tener cuatro variables por cada intervalo (a,b,c,d), y una nueva condición para cada punto común a dos intervalos, respecto a la derivada segunda: \n" \
                   "- Que las partes de la función a trozos P(x) pasen por ese punto. Es decir, que las dos Pn(x) que rodean al f(x) que queremos aproximar, sean igual a f(x) en cada uno de estos puntos. \n" \
                   "- Que la derivada en un punto siempre coincida para ambos \"lados\" de la función definida a trozos que pasa por tal punto común. \n" \
                    "-Que la derivada segunda en un punto siempre coincida para ambos \"lados\" de la función definida a trozos que pasa por tal punto común. \n" \
                    "Como puede deducirse al compararlo con el caso de splines cuadráticos, ahora no nos va a faltar una sino dos ecuaciones (condiciones) para el número de incógnitas que tenemos. \n"

ayudas["tridiagonal"] = "En las matrices banda, los elementos se organizan en diagonales alrededor de la diagonal principal, y los que están por fuera de la zona que delimitan dichas diagonales son 0. \n\n" \
                        "En una matriz banda tridiagonal, todos los elementos son cero a excepción de los elementos de la diagonal principal y de las dos diagonales que se encuentran arriba y abajo. \n\n" \
                        "Para resolver una matriz banda, en cada etapa se calculan solo 3 cosas: \n\n" \
                        "    - Un multiplicador, ya que solo un elemento por debajo de la diagonal principal es 0.\n" \
                        "    - Un cambio en un elemento del vector b  (diagonal principal)\n" \
                        "    - Un cambio en un elemento del vector d (términos independientes)\n \n" \
                        "Se sabe que el valor del elemento en el vector a será 0 al finalizar la etapa, por lo que no se calcula y simplemente se le asigna el valor de 0, y el vector c no se modifica ya que el elemento con el que se realiza la eliminación gaussiana en la fila pivote es siempre 0."


ayudas["escalonada"] = "El pivoteo escalonado es una estrategia intermedia entre el pivoteo parcial y el pivoteo total.\n" \
                       "Antes de comenzar con la eliminación, se carga un vector con los mayores elementos de cada fila. Se obtienen unos cocientes con los elementos de la columna de la etapa k y los elementos del vector de mayores en valor absoluto de su respectiva fila. Se elige la fila con el mayor cociente y se intercambia esta fila con la fila Fk."


ayudas["neville"] = "Este método presenta similitudes con Lagrange, la diferencia radica en que este aprovecha los cálculos previos para generar nuevas versiones del polinomio, es decir, los polinomios interpolantes son generados de manera recursiva. Aunque Neville arroja polinomios en su ejecución, este es el método más adecuado para calcular una aproximación al valor numérico de una función al ser evaluada en un punto; proceso que se realiza luego de haber calculado el polinomio interpolante utilizando los métodos de Newton o Lagrange.\n\n" \
                    "Para comenzar, se asume que cada valor de f(xi) es un polinomio de grado 0 que interpola al punto (xi,f(xi)), el cual se denota como Pi."


class ayuda(QDialog):

    def __init__(self, ayudade):
        super(ayuda, self).__init__()
        loadUi('UI/ayuda.ui', self)
        self.setWindowTitle('Ayuda')
        self.ayuda.setText(ayudas[ayudade])