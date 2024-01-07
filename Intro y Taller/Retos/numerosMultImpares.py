#Elaborado por: Laura Coto
#Fecha de creación: 22 de agosto del 2019, 9:30 am
#Ultima modificación: 22 de agosto del 2019, 9:40 am
#Versión: 3.5.2
#Importación de librerías

#Definición de funciones

#Programa principal
mult=1
n=int(input("Ingrese un valor numérico: "))
while n!=0:
        if (n%2)==1:
                mult*=n%10
        n=n//10
print("la multiplicación de impares es: ",mult)
        

        
