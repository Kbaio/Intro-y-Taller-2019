#Elaborado por: Laura Coto
#Fecha de creación: 22 de agosto del 2019, 9:30 am
#Ultima modificación: 22 de agosto del 2019, 9:40 am
#Versión: 3.5.2
#Importación de librerías

#Definición de funciones
def sumarSerie(pn):
        serie=0
        i=1
        while i<=pn:
                print(i,"**",i)
                serie=serie+i**i
                print(serie)
                i+=1
        return serie

#Programa principal
n=int(input("Ingrese el valor de N: "))
print("El resultado es: ",sumarSerie(n))

        
