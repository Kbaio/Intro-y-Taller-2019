###########################################################
#Elaborado por: Laura Coto Sarmiento
#Fecha de Realización: 16/01/2016
#Ultima actualización: 16/01/2016 2:23pm
###########################################################
#importación de librerías
from MiArchivodeClases import Bicicleta
from MiArchivodeClases import Carro
#Definición de variables globales
listaVehiculos = []

#definición de funciones
def menu(listaVehiculos):
      
   while True:
      print ("---Registro de Vehículos---")
      print ("1 - Agregue Carro")
      print ("2 - Agregue Bicicleta")
      print ("3 - Ver Bicicleta")
      print ("4 - Ver Carro")          
      print ("5 - Salir")

      opcion = int(input("Indique la opción: "))

      if opcion == 1:
         print ("***Indique los datos de Carro***")
         marca = input("Marca: ")
         color = input("Color: ")
         frenos = input("Frenos: ")
         anno = int(input("Año: "))
         cilindraje = int(input("Cilindraje: "))
         motor = input("Motor: ")
         chasis = input("Chasis: ")
         potencia = int(input("Potencia: "))
         tipoCaja = input("Tipo de Caja: ")
         #instanciación de la variable
         nuevoVehiculo = Carro(anno,cilindraje,motor,chasis,potencia,tipoCaja,marca,color,frenos)
         #agrego la variable a la lista
         listaVehiculos.append(nuevoVehiculo)
         
      elif opcion == 2:
         print ("***Indique los datos de la Bicicleta***")
         marca = input("Marca: ")
         color = input("Color: ")
         frenos = input("Frenos: ")
         sistCambios = input("Sistema Cambios:")
         serial = input("Serial: ")         
         #instanciación de la variable
         nuevaBicicleta = Bicicleta(marca,color,frenos,sistCambios,serial)
         #agrego la variable a la lista
         listaVehiculos.append(nuevaBicicleta)

      elif opcion == 3:
         print ("***Indique el valor de búsqueda para obtener los datos de la Bicicleta***")
         serial = input("Serial: ")
         for vehiculo in listaVehiculos:
            if vehiculo.tipo == "Bicicleta":
               if vehiculo.serial == serial:
                  vehiculo.mostrar()

      elif opcion == 4:
         print ("***Indique el valor de búsqueda para obtener los datos del Carro***")
         motor = input("Motor: ")
         for vehiculo in listaVehiculos:
            if vehiculo.tipo == "Carro":
               if vehiculo.motor == motor:
                  vehiculo.mostrar()
                  
      elif opcion == 5:
         break

#Programa Principal
menu(listaVehiculos)
