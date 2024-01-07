#Elaborado por: Laura Coto
#Fecha de creación: 22 de agosto del 2019, 9:30 am
#Ultima modificación: 22 de agosto del 2019, 9:40 am
#Versión: 3.5.2
#Importación de librerías

#Definición de funciones

#Programa principal
mayor=0
n=int(input("Ingrese un valor numérico: "))
while n!=0:
        if (n%10)>mayor:
                mayor=n%10
        n=n//10
print("El número mayor es: ",mayor)
        

        
