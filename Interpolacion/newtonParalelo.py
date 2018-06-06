import numpy as np
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.rank
size = comm.size


def newtonInterpolacion(n, x, y):
    global tabla,globaln
    globaln = n
    valor = 0
    contador = 1
    if rank ==0:
        tabla = [[0.0] * (n) for i in range(n)]
        for i in range(0, n):
            tabla[i][0] = y[i]

    numeroDeNucleos = comm.size #2 3
    for it in range(1,n):
        filasPorNucleo = int((n - contador) / numeroDeNucleos)  # 2 1
        sobrantes = (n - contador) % numeroDeNucleos  # 1
        columna = [0.0] * filasPorNucleo
        for i in range(0, filasPorNucleo):#1-n
            columna[i] = (y[filasPorNucleo*rank+(i+1)+it-1] - y[filasPorNucleo*rank+i+it-1]) / (x[filasPorNucleo*rank+(i+1)-1+it] - x[filasPorNucleo*rank+(i+1)-1])
        for i in range(sobrantes):
            if rank == i:
                columna.append((y[n-sobrantes+rank] - y[n-sobrantes+rank-1]) / -(x[n-sobrantes+rank-it]-x[n-sobrantes+rank]))

        nuevasCol = comm.gather(columna,root=0)
        if rank ==0:
            col = [0.0] *contador
            for i in range(0, numeroDeNucleos):
                nuecleoActual = nuevasCol[i]
                for j in range(filasPorNucleo * i, filasPorNucleo * i + filasPorNucleo):
                    col.append(nuecleoActual[j - filasPorNucleo * i])
            for jo in range(0, sobrantes):
                col.append(nuevasCol[jo][-1])
            tabla = np.transpose(tabla)
            tabla[it]=col
            tabla = np.transpose(tabla).tolist()
            y = col
            imprimirMatriz(tabla)
            print(" ")
        y = comm.bcast(y,root=0)
        contador+=1

    if rank == 0:
        print("Polinomio interpolante:")
        bi = tabla[0][0]
        pol = str(bi)
        temp = ""
        aux = 1
        for i in range(1, n):
            temp = temp + "(x-" + str(x[i - 1]) + ")"
            if tabla[i][i] > 0:
                pol = pol + "+" + str(round(tabla[i][i], 6)) + "*" + temp
            else:
                pol = pol + str(round(tabla[i][i], 6)) + "*" + temp
            aux = aux * (valor - x[i - 1])
            bi = bi + tabla[i][i] * aux
        print(pol)

def imprimirMatriz(tabla):
    print('\n'.join(['     '.join(['{:4}'.format(round(item, 2)) for item in row]) for row in tabla]))


def repartirEquitativamente(n, Ab, k):
    numeroDeNucleos = comm.size #4
    filasPorNucleo = int((n-k)/numeroDeNucleos)
    sobrantes = (n-k)%numeroDeNucleos
    filasDistribuidasPorNucleo = []
    if(sobrantes==0):
        for i in range(0,numeroDeNucleos):
            filasDeNucleoActual = []
            for j in range(filasPorNucleo*i,filasPorNucleo*i+filasPorNucleo):
                filasDeNucleoActual.append(Ab[j+k])
            filasDistribuidasPorNucleo.append(filasDeNucleoActual)
    else:
        for i in range(0,numeroDeNucleos):
            filasDeNucleoActual = []
            for j in range(filasPorNucleo*i,filasPorNucleo*i+filasPorNucleo):
                filasDeNucleoActual.append(Ab[j+k])
            filasDistribuidasPorNucleo.append(filasDeNucleoActual)
        for x in range(0, sobrantes):
            filasDistribuidasPorNucleo[x].append(Ab[numeroDeNucleos*filasPorNucleo+x+k])
    return filasDistribuidasPorNucleo


def hallarvalor(valor):
    bi = tabla[0][0]
    aux = 1
    for i in range(1, globaln):
        aux = aux * (valor - x[i - 1])
        bi = bi + tabla[i][i] * aux
    return bi


x = [2,2.5,3,3.6,4.2,5]
y = [2.45,6.78,8.75,9.83,10.98,11.73]
newtonInterpolacion(6, x, y)
if rank==0:
    print(hallarvalor(2))

