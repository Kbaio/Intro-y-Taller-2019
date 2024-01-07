##########################################
#XXXXXXXXXXXX
#XXXXXXXXXXXXX
#XXXXXXXXXX
#XXXXXXXXXXXXXXX
#XXXXXXXXXXXXXXXXXXXXX
#########################################
import pickle
import OO
#listaGob
listaper=[]

def menu(ulista):
    while True:
        print ("---------MENU----------")
        print ("1 - Insertar Estudiante")
        print ("2 - Insertar Profesor")
        print ("3 - Mostrar Estudiante")
        print ("4 - Mostrar Profesores")          
        print ("5 - Mostrar Todo")
        print ("6 - Salir")

        opt = int(input("Indique la opción: "))

        if opt==1:
            print ("***Indique los del estudiante***")
            ced=int(input("Cedula: "))
            nom=input("Nombre: ")
            fec=input("Fecha de nacimiento: ")
            cnet=input("Carnet: ")
            car=input("Carrera: ")
            nest=estudiante(cnet,car,ced,nom,fec)
            ulista.append(nest)

        if opt==2:
            print ("***Indique los datos del Profesor***")
            ced=int(input("Cedula: "))
            nom=input("Nombre: ")
            fec=input("Fecha de nacimiento: ")
            pu=input("Puesto: ")
            sal=float(input("Salario: "))
            nprof=profe(pu,sal,ced,no,fe)
            ulista.append(nprof)

        if opt==3:
            print ("***Indique el carnet a buscar***")
            car = input("Carnet: ")
            for per in ulista:
                if per.tipo=="est":
                    if per.carnet==car:
                        print(per.getest)

        if opt==4:
            print ("***Indique el puesto a buscar***")
            pu=input("Puesto: ")
            try:
                if per in ulista:
                    if per.tipo=="profe":
                        if per.puesto==pu:
                            print(per.getprof)
                            
    '''
        if opt==5:
            print("Todos los Registros")
            for per in ulista:
                if per.tipo=="est":
                    print(per.getest)
                else:
                    print(per.getprof)
        
        if opt==6:
            break
        '''

menu(listaper)
