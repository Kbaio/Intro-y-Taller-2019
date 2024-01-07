#############################
#Creador: David Salazar
#Fecha:8/11/2019 10:24pm
#Modificacion: 8/12/2019
#Ver: 3.7.3
#############################

ventaQuinientos=0 
ventaMasquinientos=0 
ventaArribaochocientos=0 
totalQuinientos=0  
totalmasQ=0  
totalmayor=0
state=True

while state==True:
    venta=input("¿Hay alguna venta si o no?: ")
    if venta=="si":
        precio=int(input("Digite el precio del producto: "))
        if precio<500:
            ventaQuinientos+=1
            totalQuinientos+=precio
        elif precio<800:
            ventaMasquinientos+=1
            totalmasQ+=precio
        else:
            ventaArribaochocientos+=1
            totalmayor+=precio
    else:
        print("Ventas menores a 500:",ventaQuinientos)
        print("Ventas entre 500 y 800:",ventaMasquinientos)
        print("Ventas mayores a 800:",ventaArribaochocientos)
        print("Total Ingresos:",(totalmayor+totalmasQ+totalQuinientos))
        state=False
            
    
