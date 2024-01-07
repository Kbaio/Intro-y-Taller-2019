#Elaborado por: David Salazar Rodríguez y Luan Chaves Bermúdez
#Fecha de creación: 9 de octubre del 2019, 1:40 pm
#Ultima modificación: 9 de octubre del 2019, 4:20 pm
#Versión: 3.7.2

#Importación de librebrías

from tkinter import *
from tkinter import font

#Definición de variables globales

matrizJuego = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

player1 = ""

player2 = ""

turno = True

#Definicion de funciones

def ventanaLaunch():
    ventanaPlayerName = Tk()
    ventanaPlayerName.title("Ingrese su nombre")
    ventanaPlayerName.geometry("300x250")
    ventanaPlayerName.resizable(FALSE, FALSE)

    marcoPlayerName = Frame(ventanaPlayerName, bg = "White", width = 300, height = 250)
    marcoPlayerName.place(x = 0, y = 0)

    fontPlayerName = font.Font(family = "Helvetica", size = 12)

    labelPlayer1 = Label(marcoPlayerName, bg = "White", text = "Jugador 1:", font = fontPlayerName)
    labelPlayer1.place(x = 20, y = 40)

    entryPlayer1 = Entry(marcoPlayerName, bg = "White", width = 15, font = fontPlayerName)
    entryPlayer1.place(x = 120, y = 40)

    labelPlayer2 = Label(marcoPlayerName, bg = "White", text = "Jugador 2:", font = fontPlayerName)
    labelPlayer2.place(x = 20, y = 110)

    entryPlayer2 = Entry(marcoPlayerName, bg = "White", width = 15, font = fontPlayerName)
    entryPlayer2.place(x = 120, y = 110)

    buttonIniciar = Button(marcoPlayerName, bg = "#9ee663", text = "Iniciar Juego", width = 15, font = fontPlayerName)
    buttonIniciar.place(x = 80, y = 180)


#Programa principal

ventanaLaunch()