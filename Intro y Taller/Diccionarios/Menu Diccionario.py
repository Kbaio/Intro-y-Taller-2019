############################
#Creado por: David Salazar y Sara Morales
#Fecha: 9/28/2019 4:40
#Modificacion: 
#Ver 3.7
###########################
#Imports
from Spot import * 

#Diccionario
spotify={}

def menu(spotify):
    while True:
        try:
            print("======MENU======")
            print("1. Insertar Album")
            print("2. Buscar Album")
            print("3. Buscar Album por genero")
            print("4. Buscar Cancion")
            print("5. Eliminar Album")
            print("6. Salir")
            opt=int(input("Opcion:"))
            if 0 < opt < 7:
                if opt == 1:
                    print("Opcion Insertar Album")
                    print(insertAlbum(spotify))
                    save("Spotify.txt",spotify)
                elif opt == 2:
                    print("Opcion Buscar Album")
                    print(findAlbum(spotify))
                    print("Opcion eliminar Album")
                    print(delAlbum(spotify))
                    save("Spotify.txt",spotify)
                elif opt == 3:
                    print("Buscar Album por gener")
                    print(findGenres(spotify))
                elif opt == 4:
                    print("Opcion Buscar Cancion")
                    print(findCancion(spotify))
                else:
                    False
        except:
            print("Digite solo los numeros mostrados en el menu ")


menu(spotify)
