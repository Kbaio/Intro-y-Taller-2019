#############################
#Creador: David Salazar
#Fecha:8/11/2019 10:24am
#Modificacion: 8/11/2019
#Ver: 3.7.3
#############################
numeroH=0
numeroM=0
mujerSM=0
hombreSB=0
empMay=0

empleado=int(input("Favor ingrese el numero de empleados: "))

for trail in range(1,empleado+1):
    print("---- Empleado",trail,"----")
    edad=int(input("Edad: "))
    sexo=str(input("Sexo: "))
    sueldo=int(input("Sueldo:"))
    batch=int(input("Numero de empleado: "))

    if sexo=="hombre":
        numeroH+=1
        if edad<40 and sueldo<1000:
            hombreSB+=1
        elif edad>=50:
            empMay+=1
    else:
        numeroM+=1
        if sueldo>1000:
            mujerSM+=1
            if edad>=50:
                empMay+=1
        elif edad>=50:
            empMay+=1
print("Número de hombres:",numeroH)
print("Número de mujeres:",numeroM)
print("Número de mujeres que ganan más de $1000:",mujerSM)
print("Número de hombres menores de 40 años que ganan menos de $1000:",hombreSB)
print("Número de empleados mayores de 50 años:",empMay)
            
                
            
            
        
    


      
