from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.rank
size = comm.size


def repartirEquitativamente(n, xs):
    numeroDeNucleos = comm.size
    filasPorNucleo = int(n / numeroDeNucleos)
    sobrantes = n % numeroDeNucleos
    filasDistribuidasPorNucleo = []
    for i in range(0, numeroDeNucleos):
        filasDeNucleoActual = []
        for j in range(filasPorNucleo * i, filasPorNucleo * i + filasPorNucleo):
            filasDeNucleoActual.append(xs[j])
        filasDistribuidasPorNucleo.append(filasDeNucleoActual)
    if sobrantes != 0:
        for x in range(0, sobrantes):
            filasDistribuidasPorNucleo[x].append(xs[numeroDeNucleos * filasPorNucleo + x])
    return filasDistribuidasPorNucleo


def lagrange(x, y):
    distribuidasX = []
    distribuidasY = []
    if rank == 0:
        distribuidasX = repartirEquitativamente(len(x), x)
        distribuidasY = repartirEquitativamente(len(y), y)
    myXs = comm.scatter(distribuidasX, root=0)
    myYs = comm.scatter(distribuidasY,root=0)
    terminos = []
    for i in range(len(myXs)):
        termino = ""
        numerador = ""
        denominador = ""
        for j in range(len(x)):
            if myXs[i] is not x[j]:
                numerador += "(x - " + str(x[j]) + ")"
                denominador += "(" + str(myXs[i]) + " - " + str(x[j]) + ")"
        termino = str(myYs[i])+" * " +numerador + "/" + denominador
        terminos.append(termino)
    arregloTerminos = comm.gather(terminos,root=0)
    if rank==0:
        newArr = [None] * len(x)
        for i in range(len(arregloTerminos)):
            for j in range(len(arregloTerminos[i])):
                newArr[i + (j * size)] = arregloTerminos[i][j]
        funcion = "p(x) = "
        funcion += " + ".join(newArr)
        print(funcion)
def hallarvalor(valor,n,x,y):
    resultado = 0
    for k in range(0, n):
        productoria = 1
        for i in range(0, n):
            if i is not k:
                productoria = productoria * (valor - x[i]) / (x[k] - x[i])

        resultado += productoria * y[k]
    return round(resultado,3)


x = [1, 1.2, 1.4, 1.6, 1.8]
y = [-0.620907, 0.640927, 2.234099, 4.183599, 6.513606]
lagrange(x,y)
if rank==0:
    print(hallarvalor(1.45,len(x),x,y))
