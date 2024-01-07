#############################
class TipoMotor:
   def __init__(self,po,tc):
      self.potencia = po
      self.tipoCaja = tc

   def mostrar(self):
       print(self.potencia)
       print(self.tipoCaja)
#############################      
class Vehiculo:
   def __init__(self,ma,co,fr,ti):
      self.marca = ma
      self.color = co
      self.frenos = fr
      self.tipo = ti

   def mostrar(self):
       print(self.marca)
       print(self.color)
       print(self.frenos)
       print(self.tipo)
#############################
#Con Herencia simple
class Bicicleta(Vehiculo):
   def __init__(self,ma,co,fr,sc,sr):
      self.sistCambios = sc
      self.serial = sr
      Vehiculo.__init__(self,ma,co,fr,"Bicicleta")

   def cambiarColor(self,nc):
      self.color = nc

   def mostrar(self):
       Vehiculo.mostrar(self)
       print(self.sistCambios)
       print(self.serial)
#############################
#Con Herencia Múltiple
class Carro(Vehiculo,TipoMotor):
   def __init__(self,an,ci,mo,ch,po,tc,marca,color,frenos):
      self.anno = an
      self.cilindraje = ci
      self.motor = mo
      self.chasis = ch
      Vehiculo.__init__(self,marca,color,frenos,"Carro")
      TipoMotor.__init__(self,po,tc)

   def mostrar(self):      
      Vehiculo.mostrar(self)
      TipoMotor.mostrar(self)
      print(self.anno)
      print(self.cilindraje)
      print(self.motor)
      print(self.chasis)
       
##class TipoMotor:
##   def __init__(self):
##      self.potencia = 0
##      self.tipoCaja = ""
##
##class Vehiculo:
##   def __init__(self):
##      self.marca = ""
##      self.color = ""
##      self.frenos = ""
##
##class Bicicleta(Vehiculo):
##   def __init__(self):
##      self.sistCambios = ""
##      Vehiculo.__init__(self)
##
##   def cambiarColor(self,nc):
##      self.color = nc
##
##class Carro(Vehiculo,TipoMotor):
##   def __init__(self):
##      self.anno = 0
##      self.cilindraje = 0
##      self.motor = ""
##      self.chasis = ""
##      Vehiculo.__init__(self)
##      TipoMotor.__init__(self)
