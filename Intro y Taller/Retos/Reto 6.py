#############################
#Creador: David Salazar
#Fecha:8/13/2019 11:45am
#Modificacion: 8/13/2019
#Ver: 3.7.3
#############################
dah=0
dam=0
dhh=0
dhm=0
dch=0
dcm=0

cita=int(input("Cantidad de citas: "))

while cita!=0:
    print("-----------------------")
    print("Digite:")
    print("  1 = Dr.Araya")
    print("  2 = Dra.Harley")
    print("  3 = Dra.Cordero")
    doc=int(input("Ingrese su doctor: "))
    sexo=input("Digite su sexo: ")
    if doc==1:
        if sexo=="mujer":
            dam+=1
            cita-=1
        else:
            dah+=1
            cita-=1
    elif doc==2:
        if sexo=="mujer":
            dhm+=1
            cita-=1
        else:
            dhh+=1
            cita-=1
    else:
        if sexo=="mujer":
            dcm+=1
            cita-=1
        else:
            dch+=1
            cita-=1
print("------------------")
print("Desglose del Dia")
print("------------------")
print("Dr.Araya:")
print("   Hombres:",dah)
print("   Mujeres:",dam)
print("Dra.Harley:")
print("   Hombres:",dhh)
print("   Mujeres:",dhm)
print("Dra.Cordero:")
print("   Hombres:",dch)
print("   Mujeres:",dcm)
    
    
