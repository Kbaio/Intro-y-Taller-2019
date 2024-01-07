#Elaborado por: Laura Coto
#Fecha de creación: 22 de agosto del 2019, 9:30 am
#Ultima modificación: 22 de agosto del 2019, 9:40 am
#Versión: 3.5.2

#Programa principal
serie=0
n=int(input("Ingrese el valor de N: "))
i=1
while i<=n:
        print(i,"**",i)
        serie=serie+i**i
        print(serie)
        i+=1
print("El resultado es: ",serie)

        
