#########################################
#Creador: David Salazar y Sara Morales
#Fecha 16/09/2019 9:50
#Mod:16/09/2019 9:50
#Ver 3.7
#########################################
#importaciones
#Funciones
#Reto 1-------------------
def listaAscendente(lista):
    i=0
    for j in lista:
        if i>j:
            return False
        else:
            i=j
    return True
#Reto 2-------------------
def replicarElementos(lista,n):
    lista2=[]
    for i in lista:
        for j in range(n):
            lista2.append(i)
    return lista2
#Reto 3-------------------
def diferenciaDeConjuntos(lista1,lista2):
    diferencia=[]
    for i in lista1:
        if i not in lista2:
            diferencia.append(i)
    return diferencia
#Reto 4-------------------
def sumaConjuntos(lista1,lista2):
    for i in lista2 :
        if i not in lista1:
            lista1.append(i)
    return lista1
#Reto 5-------------------
def interseccionConjuntos(lista1,lista2):
    interseccion=[]
    for i in lista2:
        interseccion.append(i)
    return interseccion
#Reto 6-------------------
def multiplicar(lista1,lista2):
    total=[]
    if len(lista1)==len(lista2):
        for i in range(len(lista1)):
            total.append(lista1[i]*lista2[i])
        return total
    else:
        return "Las listas no son de igual tamaño"
#Llamada a funcion#

print("Reto 1")
print("Lista Ascendente")
lista=[2,4,6,7]
print(listaAscendente(lista))
print("---------------------------")

print("Reto 2")
print("Replicar Elementos")
lista=[1,3,7]
n=2
print(replicarElementos(lista,n))
print("----------------------------")

print("Reto 3")
print("Dferencia de conjuntos")
A=[1,2,3,4,5,6]
B=[9,8,7,6,5]
print("La diferencia es:")
print(diferenciaDeConjuntos(A,B))
print("----------------------------")

print("Reto 4")
print("Union de Conjuntos")
A=[1,2,3,4,5,6]
B=[9,8,7,6,5]
print(sumaConjuntos(A,B))
print("----------------------------")

print("Reto 5")
print("Interseccion de Conjuntos")
l1=[1,2,3,4,5]
l2=[6,7,8,9,10]
print(interseccionConjuntos(l1,l2))
print("----------------------------")

print("Reto 6")
print("Multiplicacion de listas")
x1=[1,2,3]
x2=[4,5,6]
print(multiplicar(x1,x2))
print("----------------------------")
print("Fin")
