#####################################################
#Elaborado por: David Salazar y Pablo Ramirez       #
#Fecha: 09/09/19 5:34pm                             #
#Ultima modificación: 9:30am                       #
#ver: 3.7.3                                         #
#####################################################
#---------------------------------------------------------------------
import re

def verificarPedido(code):
    """
    Funcionamiento: Detecta si  el codigo que se introdujo es reposteria, Queque o Torta chilena
    Entradas: un codigo de 4 a 7 digitos
    Salidas: una llamada a la funcion dependiendo del pedido
    """
    if re.match("[RE]{1}",code[0:2]):
        return(pedirReposteria(code))
    elif re.match("\w{6}",code[0:]):
        return(pedirQueque(code))
    else:
        print("Codigo Invalido")
        return ""


def pedirReposteria(code):
    """
    Funcionamiento: Decodifica el codigo de reposteria
    Entradas: un codigo de 4 a 7 digitos
    Salidas: El tipo de reposteria que se solicito
    """
    if re.match("[RE]{1}",code[0:2]):
        if re.match("[D]{1}",code[2]):
            if re.match("[1]{1}",code[3:]):
                print("Usted solicitó reposteria dulce corresponde a un Nidito")
                return " "
            elif re.match("[3]{1}",code[3:]):
                print("Usted solicitó reposteria dulce corresponde a una Orejita")
                return " "
            elif re.match("[4]{1}",code[3:]):
                print("Usted solicitó reposteria dulce corresponde a un Bisquit")
                return " "
            elif re.match("[5]{1}",code[3:]):
                print("Usted solicitó reposteria dulce corresponde a un Crocante")
                return " "
            else:
                print("Codigo invalido")
                return " "

        elif re.match("[S]{1}",code[2]):
            if re.match("[6]{1}",code[3]):
                if re.match ("[1]{1}",code[4]):
                    print("Usted solicitó reposteria salada, corresponde a una enchilada de Carne")
                    return " "
                elif re.match ("[2]{1}",code[4]):
                    print("Usted solicitó reposteria salada, corresponde a una enchilada de Pollo ")
                    return " "
                else:
                    print("Codigo Invalido")
                    return " "

            elif re.match("[7]{1}",code[3]):
                if re.match("[1]{1}",code[4]):
                    if re.match("[GR]{1}",code[5:]):
                        print("Usted solicitó reposteria salada, corresponde a una Empanada de pollo Grande ")
                        return " "
                    elif re.match("[MD]{1}", code[5:]):
                        print("Usted solicitó reposteria salada, corresponde a una Empanada de pollo Mediana ")
                        return " "
                    elif re.match("[PQ]{1}", code[5:]):
                        print("Usted solicitó reposteria salada, corresponde a una Empanada de pollo Pequeña ")
                        return " "
                    else:
                        print("Codigo Invalido")
                        return " "
                    
                elif re.match("[2]{1}",code[4]):
                    if re.match("[GR]{1}",code[5:]):
                        print("Usted solicitó reposteria salada, corresponde a una Empanada de carne Grande ")
                        return " "
                    elif re.match("[MD]{1}", code[5:]):
                        print("Usted solicitó reposteria salada, corresponde a una Empanada de carne Mediana ")
                        return " "
                    elif re.match("[PQ]{1}", code[5:]):
                        print("Usted solicitó reposteria salada, corresponde a una Empanada de carne Pequeña ")
                        return " "
                    else:
                        print("Codigo Invalido")
                        return " "
                else:
                    print("Codigo Invalido")
                    return " "     
            else:
                print("Codigo Invalido")
                return " "
        else:
            print("Codigo Invalido")
            return " "

    elif re.match("[TCAGR]{1}", code):
            print("Usted Solicitó una torta chilena Grande")
            return ""
    else:
            print("Codigo Invalido")
            return " "
    
def pedirQueque(code):
    """
    Funcionamiento: Detecta que tipo de queque pidio el usuario
    Entradas: un codigo de 6 digitos
    Salidas: El tipo de Queque que se solicitó
    """
    if re.match("[QE]{1}",code[0:3]):
        if re.match("[GR]{1}",code[3:5]):
            if re.match("[VN]{1}",code[5:]):
                print("Usted Solicitó un Queque grande de Vainilla")
                return " "
            elif re.match("[CM]{1}",code[5:]):
                print("Usted Solicitó un Queque grande de Caramelo")
                return " "
            elif re.match("[CE]{1}",code[5:]):
                print("Usted Solicitó un Queque grande de Chocolate")
                return " "
            else:
                print("Usted Solicitó un Queque grande de Fresa")
                return " "
        if re.match("[PQ]{1}",code[3:5]):
            if re.match("[VN]{1}",code[5:]):
                print("Usted Solicitó un Queque pequeño de Vainilla")
                return " "
            elif re.match("[CM]{1}",code[5:]):
                print("Usted Solicitó un Queque pequeño de Caramelo")
                return " "
            elif re.match("[CE]{1}",code[5:]):
                print("Usted Solicitó un Queque pequeño de Chocolate")
                return " "
            else:
                print("Usted Solicitó un Queque pequeño de Fresa")
                return " "

def menu():
    """
    Funcionamiento: Muestra el menú al usuario.
    Entradas: NA
    Salidas: El codigo digitado resuelto
    """
    print("\n**************************\n")
    print("Opciones a Elegir"
          "\n×Reposteria"
          "\n     Tipos: "
          "\n             Dulce  "
          "\n          ---------------"  
          "\n          1) Nidito"
          "\n          2) Palito de Queso"
          "\n          3) Orejita"
          "\n          4) Biscuit"
          "\n          5) Crocante"
          "\n"
          "\n            Salada"
          "\n         ---------------"
          "\n          6) Enchilada"
          "\n          7) Empanada"
          "\n    "
          "\n     Sabores: Pollo o Carne"
          "\n  "
          "\n×Queques"
          "\n     Tamaño: GR = Grande, 12 porciones "
          "\n              PQ = pequeño 4 porciones  "
          "\n     "
          "\n     Sabores FR = Fresa"
          "\n               VN = Vainilla"
          "\n               CM = Caramelo"
          "\n               CE = Chocolate"
          "\n    "
          "\n×Torta Chilena ")
    print("\n**************************\n")
    print("Desea decodificar un codigo?")
    opcion = input("Digite su respuesta: ")
    si = "SI"
    no = "NO"
    if opcion.upper()== si:
        codigo = input("Favor digite el codigo del Producto: ")
        verificarPedido(codigo.upper())
        menu()
    elif opcion.upper()==no:
        return
    else:
        print("Favor digite unicamente Si o No")
        menu()

#PP
menu()


