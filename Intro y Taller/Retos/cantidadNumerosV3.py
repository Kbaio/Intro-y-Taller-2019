#Elaborado por: Laura Coto
#Fecha de creación: 22 de agosto del 2019, 9:30 am
#Ultima modificación: 22 de agosto del 2019, 9:40 am
#Versión: 3.5.2
#Importación de librerías

#Definición de funciones
def contarDigitos(pn):
        contador=0
        while pn!=0:
                pn=pn//10
                contador+=1
        return contador


#Programa principal
n=int(input("Ingrese un valor numérico: "))
print("El número posee: ",contarDigitos(n)," digitos.")
        

        
