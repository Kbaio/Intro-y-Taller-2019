#################
#Creado por: David Salazar Rodriguez
#Fecha de creacion:5/10/2019
#Modificacion
#Ver 3.7.3
#################
#importaciones
import pickle

#Diccionario
spotify={}

def save(spotify):
    f=open("Spotify.txt","wb")
    pickle.dump(spotify,f)
    f.close()

def load(spotify):
    f=open("Spotify.txt","rb+")
    try:
        spotify=pickle.load(f)
    except:
        break
    f.colse()

def insertAlbum(spotify):
    cancion=[]
    album=input("Digite el nombre del album: ")
    artista=input("Digite el nombre del artista: ")
    genero=input("Digite el genero del album: ")
    print("¿Desea agregar una canción al album? (Si o No)")
    sub=input("Respuesta: ")
    while sub.lower()=="si":
        if sub.lower()=="si":
            print("Digite el nombre de la canción:")
            song=input("Cancion: ")
            cancion.append(song.upper())
            print("¿Desea agregar otra cancion?")
            sub=input("Respuesta: ")
    if album not in spotify.keys():
        album.upper()
        spotify[album]=[artista.upper(),genero.upper(),cancion]
    else: 
        print("El album ya se encuentra registrado.")
    print(spotify)
    return spotify

def delAlbum(spotify):
    print("Digite el album que desea eliminar")
    album=input("Album: ")
    if album in spotify.keys():
        del spotify[album]
    else:
        print("No se encuentra el album especificado")
    return spotify

def findAlbum(spotify):
    print("Digite el nombre del album a buscar")
    buscar=input("Album: ")
    if buscar in spotify.keys():
        lista=spotify.get(buscar)
        print("=======================")
        print("Album:",buscar)
        print("Artista:",lista[0])
        print("Genero:",lista[1])
        print("Canciones:")
        for i in lista[2]:
            print("\t"+i)
        print("=======================")
        return""
    else:
        print("No se encuentra el album especificado")
        return""


def findGenres(spotify):
    llaves=spotify.keys()
    genalb=[]
    print("Digite el genero a buscar:")
    genero=input("Genero: ")
    for i in llaves:
        recibe=spotify.get(i)
        if recibe[1]==genero.upper():
            genalb.append(i)
    if genalb!=[]:
        print("Los albumes con de genero",genero,"son:")
        for i in genalb:
            print("\t"+i)
            return""
    else:
        print("No se encontraron albums del genero",genero,"registrados.")
        return""

def findCancion(spotify):
    llaves=spotify.keys()
    print("Digite la cancion a buscar:")
    cancion=input("Cación: ")
    for i in llaves:
        recibe=spotify.get(i)
        for cb in recibe[2]:
            if cb==cancion.upper():
                print("Album:",i)
                print("Artista:",recibe[0])
                print("Genero:",recibe[1])
                return""
    return "No se encontro la cancion especificada."