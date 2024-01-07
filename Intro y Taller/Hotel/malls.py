############################
#Creado por: David Salazar y Sara Morales
#Fecha: 9/28/2019 4:40
#Modificacion: 
#Ver 3.7
###########################
#importaciones
import pickle

def crearMatriz(tamano):
    """
    Entradas: Entra la cantidad de estudiantes que hay en el grupo.
    Salidas: Sale la matriz creada aleatoriamente.
    Funcion: Crea una matriz aleatoria.
    """
    i=1
    matriz=[]
    while i<=tamano:
        fila=[]
        j=1
        while j<=tamano:
            num=0
            fila.append(num)
            j+=1
            
        matriz.append(fila)
        i+=1

    return matriz

def mostrarMatriz(matriz):
    """
    Entradas: La matriz
    Salidas: Un print de cada una de las filas de la matriz
    Funcion: Muestra la matriz de una manera ordenada.
    """
    for fila in matriz:
        print(fila)
    return ""

def alquilarlocal(piso,columna,matriz):
    """
    Entradas: El piso, la columna y la matriz
    Salidas: La matriz modificada
    Funcion: Se ubica el piso y la columna para reemplazar las coordenadas
    """
    precio=int(input("Digite el precio de alquiler: "))
    matriz[piso-1][columna-1]=precio
    return matriz

def eliminarlocal(piso,columna,matriz):
    """
    Entradas: El piso, la columna y la matriz
    Salidas: La matriz modificada
    Funcion: Se ubica el piso y la columna para reemplazar las coordenadas
    """
    matriz[piso-1][columna-1]=0
    return matriz

def revenuePiso(matriz,piso):
    """
    Entradas: Matriz
    Salidas: Acumulado del piso
    Funcion: Se saca el acumulado de todos los locales en el piso
    """
    acum=0
    for precio in matriz[piso-1]:
        acum+=precio
    return acum

def revenueColumna(matriz,columna):
    """
    Entradas: Matriz
    Salidas: Acumulado de la columna
    Funcion: Se saca el acumulado de todos los locales en la columna.
    """
    acum=0
    for fila in matriz:
        acum+=fila[columna-1]
    return acum
def revenueDiagonal(matriz):
    """
    Entradas: Matriz
    Salidas: acumulado de la diagonal 
    Funcion: Se saca el acumulado de la diagonal de izquierda arriba a la derecha
    """
    sec=0
    acum=0
    for fila in matriz:
        acum+=fila[sec]
        sec+=1
    return acum

def revenueInverso(matriz):
    """
    Entradas: Matriz
    Salidas: acumulado de la diagonal 
    Funcion: Se saca el acumulado de la diagonal de izquierda abajo a la derecha
    """
    sec=len(matriz)-1
    acum=0
    for fila in matriz:
        acum+=fila[sec]
        sec-=1
    return acum

def revenueTotal(matriz):
    """
    Entradas: Matriz
    Salidas: acumulado de la diagonal 
    Funcion: Se saca el acumulado de la diagonal de derecha a izquierda
    """
    acum=0
    for fila in matriz:
        for columna in fila:
            acum+=columna
    return acum

def revenueEsquinas(matriz):
    """
    Entradas: Matriz
    Salidas: acumulado de las esquinas
    Funcion: Se saca el acumulado de las esquinas
    """
    acum=0
    largo=len(matriz)-1
    acum+=matriz[0][0]
    acum+=matriz[0][largo]
    acum+=matriz[largo][0]
    acum+=matriz[largo][largo]
    return acum

def revenueVentana(matriz):
    """
    Entradas: Matriz
    Salidas: acumulado de los bordes
    Funcion: Se saca el acumulado de los bordes
    """
    acum=0
    largo=len(matriz)-1
    for fila in range(largo):
        if fila==0 or fila==largo:
            for columna in matriz[fila]:
                acum+=columna
        elif fila!=largo:
            acum+=matriz[fila][0]
            acum+=matriz[fila][largo]
    return acum
