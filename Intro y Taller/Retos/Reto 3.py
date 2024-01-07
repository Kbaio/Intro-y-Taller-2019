#############################
#Creador: David Salazar
#Fecha:8/12/2019 9:00am
#Modificacion: 8/12/2019
#Ver: 3.7.3
#############################
numeroH=0
numeroM=0
mujerO=0
hombreO=0
estCR=0
deportista=int(input("Digite el numero de deportistas: "))

while (deportista!=0):
    print("       Deportistas         ")
    print("---------------------------")
    pais=input("País: ")
    edad=int(input("Edad: "))
    sexo=input("Sexo: ")
    medalla=int(input("Medallas: "))
    print("---------------------------")

    if sexo.upper()=="HOMBRE":
        numeroH+=1
        if edad>=25 and medalla>=2:
            hombreO+=1
            if pais.upper()=="COSTA RICA":
                estCR+=1
                deportista-=1
        else:
            if pais.upper()=="COSTA RICA":
                estCR+=1
                deportista-=1
            else:
                deportista-=1
    else:
        numeroM+=1
        if medalla>=1:
            mujerO+=1
            if pais.upper()=="COSTA RICA":
                estCR+=1
                deportista-=1
            else:
                deportista-=1
        else:
            if pais.upper()=="COSTA RICA":
                estCR+=1
                deportista-=1
            else:
                deportista-=1

print("Hombres:",numeroH)
print("Mujeres:",numeroM)
print("Mujeres con oro:",mujerO)
print("Hombres menos de 25 con 2 medallas:",hombreO)
print("Deportistas de Costa Rica:",estCR)
                
            
            
    
                
            
