#############################
#Creador: David Salazar
#Fecha:8/12/2019 8:27pm
#Modificacion: 8/12/2019
#Ver: 3.7.3
#############################
aguja=0
ficha=0
guarda=0
state=True
while state==True:
    estado=input("¿Los portones estan abiertos si o no?: ")
    if estado=="si":
        carnet=input("¿Tiene carnet si o no?: ")
        if carnet=="si":
            aguja+=1
        else:
            motivo=input("¿Viene de visita si o no?: ")
            if motivo=="si":
                ficha+=1
            else:
                guarda+=1
    else:
        total=(aguja+ficha+guarda)
        PA=(total*aguja)/100
        PV=(total*ficha)/100
        PG=(total*guarda)/100

        print("Ingresos de Aguja: "+str(PA)+"%")
        print("Ingresos de Visita: "+str(PV)+"%")
        print("Ingresos con guarda: "+str(PG)+"%")
        state=False
