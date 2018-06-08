from mpi4py import MPI

import SistemasEcuaciones.Paralelos as eliminacion

comm = MPI.COMM_WORLD
rank = comm.rank
size = comm.size

def repartirEquitativamente(n, Ab, k):
    numeroDeNucleos = comm.size
    filasPorNucleo = int((n - k) / numeroDeNucleos)
    sobrantes = (n - k) % numeroDeNucleos
    filasDistribuidasPorNucleo = []
    for i in range(0, numeroDeNucleos):
        filasDeNucleoActual = []
        for j in range(filasPorNucleo * i, filasPorNucleo * i + filasPorNucleo):
            filasDeNucleoActual.append(Ab[j + k])
        filasDistribuidasPorNucleo.append(filasDeNucleoActual)
    if sobrantes != 0:
        for x in range(0, sobrantes):
            filasDistribuidasPorNucleo[x].append(Ab[numeroDeNucleos * filasPorNucleo + x + k])
    return filasDistribuidasPorNucleo

def cuadradoNatural(n, x, y):
    tabla = []
    n = n - 1
    marcas = set()
    xDistribuidas = []
    yDistribuidas = []
    if rank == 0:
        xDistribuidas = repartirEquitativamente(len(x), x, 0)
        yDistribuidas = repartirEquitativamente(len(y), y, 0)

    misXs = comm.scatter(xDistribuidas, root=0)
    misYs = comm.scatter(yDistribuidas, root=0)
    filas = []

    for i in range(len(misXs)):
        fila = [0.0] * (n * 3 + 1)
        fila1 = None

        if (x.index(misXs[i]) != 0) & (x.index(misXs[i]) != n):
            k = (x.index(misXs[i]) - 1) * 3
            exp = 2
            for j in range(0, 3):
                fila[k + j] = pow(misXs[i], exp)
                exp -= 1
            exp = 2
            fila1 = [0.0] * (n * 3 + 1)
            for j in range(0, 3):
                fila1[k + j + 3] = pow(misXs[i], exp)
                exp -= 1
            fila1[-1] = misYs[i]
        elif (x.index(misXs[i]) == n):
            k = (n * 3) - 3
            exp = 2
            for j in range(0, 3):
                fila[k + j] = pow(misXs[i], exp)
                exp -= 1
        else:
            k = 0
            exp = 2
            for j in range(0, 3):
                fila[k + j] = pow(misXs[i], exp)
                exp -= 1

        fila[-1] = misYs[i]
        filas.append(fila)
        filas.append(fila1)
    arregloFilas = comm.gather(filas)
    if rank == 0:
        for i in range(len(arregloFilas)):
            for j in range(len(arregloFilas[i])):
                if arregloFilas[i][j] is not None:
                    tabla.append(arregloFilas[i][j])
        etapa2x = x[1:-1]
        xDistribuidas = repartirEquitativamente(len(etapa2x), etapa2x, 0)
    misXs = comm.scatter(xDistribuidas, root=0)

    filas = []
    exp = 1
    # Etapa 2
    for i in range(len(misXs)):
        fila = [0.0] * (n * 3 + 1)
        k = (x.index(misXs[i]) - 1) * 3
        for j in range(0, 2):
            fila[k + j] = (2 - j) * pow(misXs[i], exp)
            exp -= 1
        exp = 1

        for j in range(0, 2):
            fila[k + j + 3] = -(2 - j) * pow(misXs[i], exp)
            exp -= 1
        filas.append(fila)
    arregloFilas = comm.gather(filas)

    if rank == 0:
        for i in range(len(arregloFilas)):
            for j in range(len(arregloFilas[i])):
                if arregloFilas[i][j] is not None:
                    tabla.append(arregloFilas[i][j])

    filas = []
    exp = 1
    # Etapa 3
    if len(misXs) > 0:
        for i in range(len(misXs)):
            fila = [0.0] * (n * 3 + 1)
            k = (x.index(misXs[i]) - 1) * 3
            fila[k + 0] = 2 * pow(misXs[i], exp)
            filas.append(fila)

    arregloFilas = comm.gather(filas)

    if rank == 0:
        for i in range(len(arregloFilas)):
            for j in range(len(arregloFilas[i])):
                if arregloFilas[i][j] is not None:
                    tabla.append(arregloFilas[i][j])

    Ab = comm.bcast(tabla, root=0)
    xns = eliminacion.eliminacionGaussianaTotal((n * 3), Ab)
    if rank == 0:
        m = [chr(97 + j) + str(i) for i in range(1, n + 1) for j in range(3)]
        for i in range(len(m)):
            print(str(m[i]) + " = " + str(xns[i]))
    return xns


def hallarValor(x, vars, valor):
    solucion = vars
    ind = 0
    if valor >= x[0]:
        if valor <= x[len(x) - 1]:
            for i in range(0, len(x) - 1):
                if (valor >= x[i]) & (valor <= x[i + 1]):
                    ind = i
        else:
            ind = len(x) - 2
    resp = 0.0
    for i in range(0, 4):
        resp += solucion[(ind * 4) + i] * pow(valor, 3 - i)
    print("Resultado:")
    print("f(" + str(valor) + ") = " + str(resp))
    return resp

x = [2, 3, 5,6]
y = [-1, 2, -7,8]
vars = cuadradoNatural(4, x, y)