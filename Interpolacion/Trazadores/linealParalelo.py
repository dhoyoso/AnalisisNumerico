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


def lineal(x, y):
    distribuidasX = []
    distribuidasY = []
    val = None
    funcion = []
    if rank == 0:
        xs = []
        ys = []
        for i in range((len(x) - 1)):
            xs.append([x[i], x[i + 1]])
            ys.append([y[i], y[i + 1]])
        distribuidasX = repartirEquitativamente(len(xs), xs)
        distribuidasY = repartirEquitativamente(len(ys), ys)
    myXs = comm.scatter(distribuidasX, root=0)
    myYs = comm.scatter(distribuidasY, root=0)
    myBs = []
    myMs = []
    for it in range(len(myXs)):
        mi = (myYs[it][1] - myYs[it][0]) / (myXs[it][1] - myXs[it][0])
        bi = -(mi * myXs[it][0]) + myYs[it][0]
        myBs.append(bi)
        myMs.append(mi)
        funcion.append(
            str(round(mi, 2)) + "X + " + str(round(bi, 2)) + " si " + str(round(myXs[it][0], 2)) + " ≤ x ≤ " + str(
                round(myXs[it][1], 2)) + "\n")
    arregloFx = comm.gather(funcion, root=0)
    arregloVal = comm.gather(val, root=0)
    bis = comm.gather(myBs, root=0)
    mis = comm.gather(myMs, root=0)
    m = []
    b = []
    if rank == 0:
        print(bis)
        print(mis)
        arregloVal = set(arregloVal)
        newArr = [None] * len(xs)
        for i in range(len(arregloFx)):
            for j in range(len(arregloFx[i])):
                newArr[i + (j * size)] = arregloFx[i][j]
        funcion = "".join(newArr)
        newArr = [None] * len(xs)
        for i in range(len(bis)):
            for j in range(len(bis[i])):
                newArr[i + (j * size)] = bis[i][j]
        b = newArr
        newArr1 = [None] * len(xs)
        for i in range(len(mis)):
            for j in range(len(mis[i])):
                newArr1[i + (j * size)] = mis[i][j]
        m = newArr1
        print(funcion)
    return (m, b)


def hallarValor(valor, x, m, b, n):
    print(m,b)
    for i in range(0, n):
        if (valor >= x[i]) & (valor <= x[i + 1]):
            return (m[i] * valor) + b[i]


x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
a, c = lineal(x, y)
if rank == 0:
    print(hallarValor(2, x, a, c, len(x)))
