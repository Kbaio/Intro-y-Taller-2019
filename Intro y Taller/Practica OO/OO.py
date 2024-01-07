##########################################
#XXXXXXXXXXXX
#XXXXXXXXXXXXX
#XXXXXXXXXX
#XXXXXXXXXXXXXXX
#XXXXXXXXXXXXXXXXXXXXX
#########################################


class persona:
    def __init__(self,ced,no,fe,tipo):
        self.cedula=ced
        self.nombre=no
        self.fecha=fe
        self.tipo=ti

class estudiante:
    def __init__(self,cnet,car,ced,no,fe)
    self.carnet=cnet
    self.carrera=car
    persona.__init__(self,ced,no,fe,"est")

    def getest(self):
        print("======================")
        print(self.cedula)
        print(self.nombre)
        print(self.fecha)
        print(self.carnet)
        print(self.carrera)
        print("======================")

class profe:
    def __init__(self,pu,sal,ced,no,fe):
        self.puesto=pu
        self.salario=sal
        persona.__init__(self,ced,no,fe,"profe")

    def getprof(self):  
        print("======================")
        print(self.cedula)
        print(self.nombre)
        print(self.fecha)
        print(self.puesto)
        print(self.salario)
        print("======================")
