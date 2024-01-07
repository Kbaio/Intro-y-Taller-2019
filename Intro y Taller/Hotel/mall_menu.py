############################
#Creado por: David Salazar y Sara Morales
#Fecha: 9/28/2019 4:40
#Modificacion: 
#Ver 3.7
###########################
#Imports
from malls import * 

#Matriz
matriz=[]

def menu(matriz):
    mvacio=[]
    if matriz==mvacio:
        print("Digite el tamaño del edificio:")
        tam=int(input("Tamaño: "))
        matriz=crearMatriz(tam)
    while True:
        try:
            print("Matriz")
            print(mostrarMatriz(matriz))
            print("1. Alquilar local")
            print("2. Eliminar contrato")
            print("3. Reporte")
            print("4. Salir")
            opt=int(input("Opcion:"))
            if 0 < opt < 4:
                if opt == 1:
                    print("Matriz")
                    print(mostrarMatriz(matriz))
                    print("Opcion alquilar local")
                    piso=int(input("Digite el piso: "))
                    columna=int(input("Digite la columna a alquilar:"))
                    alquilarlocal(piso,columna,matriz)
                    save("test",matriz)
                elif opt == 2:
                    print("Opcion eliminar local")
                    piso=int(input("Digite el piso: "))
                    columna=int(input("Digite la columna a alquilar:"))
                    eliminarlocal(piso,columna,matriz)
                elif opt == 3:
                    print("1. Ganancia por piso ")
                    print("2. Ganancia por columna ")
                    print("3. Ganancia diagonal (Derecha arriba hacia abajo)")
                    print("4. Ganancia diagonal (Derecha abajo hacia arriba)")
                    print("5. Ganancia total mensual")
                    print("6. Ganancia esquinas")
                    print("7. Ganancia Marco ")
                    sub=int(input("Opcion:"))
                    if 0 < sub < 8:
                        if sub==1:
                            piso=int(input("Digite el piso del cual quiere saber los ingresos: "))
                            if piso-1 in range(len(matriz)):
                                print("Los ingresos del piso",piso,"son:",revenuePiso(matriz,piso))
                            else:
                                print("El numero de piso no se encuentra.")
                        elif sub==2:
                            columna=int(input("Digite el columna de la cual quiere saber los ingresos: "))
                            if columna-1 in range(len(matriz)):
                                print("Los ingresos de la columna",columna,"son:",revenueColumna(matriz,columna))
                            else:
                                print("El numero de columna no se encuentra.")
                        elif sub==3:
                            print("Los ingresos de esta diagonal son:",revenueDiagonal(matriz))
                        elif sub==4:
                            print("Los ingresos de esta diagonal son:",revenueInverso(matriz))
                        elif sub==5:
                            print("Los ingresos Mensuales son:",revenueTotal(matriz))
                        elif sub==6:
                            print("Los ingresos de las esquinas son:",revenueEsquinas(matriz))
                        elif sub==7:
                            print("Los ingresos del cuadro son:",revenueVentana(matriz))
                elif opt == 4:
                    break
        except:
            print("Digite solo los numeros mostrados en el menu ")


menu(matriz)
