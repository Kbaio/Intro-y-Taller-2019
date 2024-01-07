#Creado por David Salazar
#Fecha de creacion: 5/11/2019 6:36pm
#Modificacion
#Ver 3.7
###########################################
#importaciones
from tkinter import *
import tkinter.messagebox
from tkinter import ttk
import tkinter as tk
import xml.etree.ElementTree as ET
import random
from faker import Faker
import pickle
from os import startfile
import os
import webbrowser


#VARIABLES GLOBALES
pack=[]
litaObjetos=[]
direccion="""<img src="C:/Users/David/Desktop/THECC/Semestre II 2019/Intro y Taller/TP3/GO.png"width="100" height="50">"""
#FUNCIONES

def save():
    """
    Entradas: N/A
    Salidas: N/A
    Funcion: Guarda en una un archivo la lista de objetos
    """
    global litaObjetos
    f=open("CartaSanta.txt","wb")
    pickle.dump(litaObjetos,f)
    f.close()
    
def load():
    """
    Entradas: N/A
    Salidas: N/A
    Funcion: Carga en una lista global el archiivo seleccionado
    """
    global litaObjetos
    while True:
        try:
            f=open("CartaSanta.txt","rb+")
            litaObjetos=pickle.load(f)
            break
        except :
            litaObjetos=[]
            break
        
def espar(num):
    """
    Entradas: Un numero entero
    Salida: Un booleano
    Funcion es par devuelve True si la entrada es par o no
    """
    if num%2==0:
        return True
    else:
        return False
#HTMLS
#=============================================
def HTML_Kid(boi):
    """
    Entradas: N/A
    Salidas: Una tabla en HTML con la informacion requeridas
    Funcion: Crear la tabla de HTML y mostrarlo
    """
    global litaObjetos,pack,direccion
    kid=""
    juguete=""
    contador=0
    for carta in litaObjetos:
        if carta.getNombre()==boi:
            texto = """<tr style=background-color:#4682B4><td style="border: 1px solid black;"><fn style="font-size:25px;">"""+carta.getNombre()+"""</td>
            <td style="border: 1px solid black;"><fn style="font-size:25px;">""" + str(carta.getEdad()) + """</td>
            <td style="border: 1px solid black;"><fn style="font-size:25px;">""" + carta.getSexo() + """</td></tr></fn>"""
            kid= kid + texto
            for toy in carta.getJuguetes():
                for fila in pack:
                    if toy==fila[0]:
                        if espar(contador):
                            text="""<tr style=background-color:#4682B4><td style="border: 1px solid black;"><fn style="font-size:25px;">"""+fila[2]+"""</td></fn>
                            <td style="border: 1px solid black;"><fn style="font-size:25px;">""" + fila[0] + """</td></fn>
                            <td style="border: 1px solid black;">"""+direccion+"""</td></tr></fn>"""
                            contador+=1
                            juguete=juguete+text
                        else:
                            text="""<tr style=background-color:#008080><td style="border: 1px solid black;"><fn style="font-size:25px;">"""+fila[2]+"""</td></fn>
                            <td style="border: 1px solid black;"><fn style="font-size:25px;">""" + fila[0] + """</td></fn>
                            <td style="border: 1px solid black;">"""+direccion+"""</td></tr></fn>"""
                            juguete=juguete+text
                            contador+=1
                            
            break

            
    setup = """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <meta name="description" content="Solicitante por Nombre ">
        <title>Solicitantes de dos o mas juguetes</title>
    <head>
    <body style="width:100%; display:flex; justify-content: center;">
        <table style="border: 1px solid black;">
                <caption><h2>Solicitante por Nombre</h2></caption>
                <thead>
                <tr>
                    <th style="border: 1px solid black;"><fn style="font-size:25px;">Nombre</th></fn>
                    <th style="border: 1px solid black;"><fn style="font-size:25px;">Edad</th></fn>
                    <th style="border: 1px solid black;"><fn style="font-size:25px;">Sexo</th></fn>
                </tr>
                </thead>
                <tbody>
                """+ kid +"""
                </tbody>
                <thead>
                <tr>
                    <th style="border: 1px solid black;"><fn style="font-size:25px;">ID</th></fn>
                    <th style="border: 1px solid black;"><fn style="font-size:25px;">Nombre</th></fn>
                    <th style="border: 1px solid black;"><fn style="font-size:25px;">Foto</th></fn>
                </tr>
                </thead>
                <tbody>
                """+ juguete +"""
                </tbody>
        </table>
    </body>
    </html>
    """
    f = open('Carta_Unica.html','w')
    f.write(setup)
    filename = 'file:///'+os.getcwd()+'/'+'Carta_Unica.html'
    webbrowser.open(filename)


def HTML_Sexo():
    """
    Entradas: N/A
    Salidas: Una tabla en HTML con la informacion requeridas
    Funcion: Crear la tabla de HTML y mostrarlo
    """
    global litaObjetos
    mujeres=""
    hombres=""
    contador=0
    for carta in litaObjetos:
        if carta.getSexo()=="Mujer":
            if espar(contador):
                texto = """<tr style=background-color:#4682B4><td style="border: 1px solid black;"><fn style="font-size:25px;">"""+carta.getSexo()+"""</td>
                <td style="border: 1px solid black;"><fn style="font-size:25px;">""" + str(carta.getEdad()) + """</td>
                <td style="border: 1px solid black;"><fn style="font-size:25px;">""" + carta.getNombre() + """</td>
                <td style="border: 1px solid black;"><fn style="font-size:25px;">""" + str(carta.getJuguetes()) + """</td></tr></fn>"""
                mujeres= mujeres + texto
                contador+=1
            else:
                texto = """<tr style=background-color:#008080><td style="border: 1px solid black;"><fn style="font-size:25px;">"""+carta.getSexo()+"""</td>
                <td style="border: 1px solid black;"><fn style="font-size:25px;">""" + str(carta.getEdad()) + """</td>
                <td style="border: 1px solid black;"><fn style="font-size:25px;">""" + carta.getNombre() + """</td>
                <td style="border: 1px solid black;"><fn style="font-size:25px;">""" + str(carta.getJuguetes())+ """</td></tr></fn>"""
                mujeres= mujeres + texto
                contador+=1
        else:
            if espar(contador):
                texto = """<tr style=background-color:#4682B4><td style="border: 1px solid black;"><fn style="font-size:25px;">"""+carta.getSexo()+"""</td>
                <td style="border: 1px solid black;"><fn style="font-size:25px;">""" + str(carta.getEdad()) + """</td>
                <td style="border: 1px solid black;"><fn style="font-size:25px;">""" + carta.getNombre() + """</td>
                <td style="border: 1px solid black;"><fn style="font-size:25px;">""" + str(carta.getJuguetes()) + """</td></tr></fn>"""
                hombres= hombres + texto
                contador+=1
            else:
                texto = """<tr style=background-color:#008080><td style="border: 1px solid black;"><fn style="font-size:25px;">"""+carta.getSexo()+"""</td>
                <td style="border: 1px solid black;"><fn style="font-size:25px;">""" + str(carta.getEdad()) + """</td>
                <td style="border: 1px solid black;"><fn style="font-size:25px;">""" + carta.getNombre() + """</td>
                <td style="border: 1px solid black;"><fn style="font-size:25px;">""" + str(carta.getJuguetes())+ """</td></tr></fn>"""
                hombres= hombres + texto
                contador+=1
                
    segunSexo = """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <meta name="description" content="Solicitante por Sexo">
        <title>Solicitantes de dos o mas juguetes</title>
    <head>
    <body style="width:100%; display:flex; justify-content: center;">
        <table style="border: 1px solid black;">
                <caption><h2>Solicitante por Sexo</h2></caption>
                <thead>
                <tr>
                    <th style="border: 1px solid black;"><fn style="font-size:25px;">Sexo</th></fn>
                    <th style="border: 1px solid black;"><fn style="font-size:25px;">Edad</th></fn>
                    <th style="border: 1px solid black;"><fn style="font-size:25px;">Nombre</th></fn>
                    <th style="border: 1px solid black;"><fn style="font-size:25px;">Juguetes</th></fn>
                </tr>
                </thead>
                <tbody>
                """+ mujeres +"""
                """+hombres+"""
                </tbody>
        </table>
    </body>
    </html>
    """
    f = open('Segun_Sexo.html','w')
    f.write(segunSexo)
    filename = 'file:///'+os.getcwd()+'/'+'Segun_Sexo.html'
    webbrowser.open(filename)


def HTML_Inventario():
    """
    Entradas: N/A
    Salidas: Una tabla en HTML con la informacion requeridas
    Funcion: Crear la tabla de HTML y mostrarlo
    """
    global pack,direccion
    informacion=""
    contador=0
    for lista in pack:
        if espar(contador):
            texto = """<tr style=background-color:#4682B4><td style="border: 1px solid black;"><fn style="font-size:25px;">"""+lista[2]+"""</td></fn>
            <td style="border: 1px solid black;"><fn style="font-size:25px;">""" + lista[0] + """</td></fn>
            <td style="border: 1px solid black;"><fn style="font-size:25px;">""" + lista[1]+ """</td></fn>
            <td style="border: 1px solid black;">"""+direccion+"""</td></tr></fn>"""
            informacion= informacion + texto
            contador+=1
        else:
            texto = """<tr style=background-color:#008080><td style="border: 1px solid black;"><fn style="font-size:25px;">"""+lista[2]+"""</td></fn>
            <td style="border: 1px solid black;"><fn style="font-size:25px;">""" + lista[0] + """</td></fn>
            <td style="border: 1px solid black;"><fn style="font-size:25px;">""" + lista[1] + """</td></fn>
            <td style="border: 1px solid black;">"""+direccion+"""</td></tr></fn>"""
            informacion= informacion + texto
            contador+=1
            
    htmlvarios = """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <meta name="description" content="Inventario">
        <title>Solicitantes de dos o mas juguetes</title>
    <head>
    <body style="width:100%; display:flex; justify-content: center;">
        <table style="border: 1px solid black;">
                <caption><h2>Solicitantes de Varios Juguetes</h2></caption>
                <thead>
                <tr>
                    <th style="border: 1px solid black;"><fn style="font-size:25px;">ID</th></fn>
                    <th style="border: 1px solid black;"><fn style="font-size:25px;">Nombre</th></fn>
                    <th style="border: 1px solid black;"><fn style="font-size:25px;">Descripcion</th></fn>
                    <th style="border: 1px solid black;"><fn style="font-size:25px;">Foto</th></fn>
                </tr>
                </thead>
                <tbody>
                """+ informacion +"""
                </tbody>
        </table>
    </body>
    </html>
    """
    f = open('Inventario.html','w')
    f.write(htmlvarios)
    filename = 'file:///'+os.getcwd()+'/'+'Inventario.html'
    webbrowser.open(filename)


def HTML_VariosJuguetes():
    """
    Entradas: N/A
    Salidas: Una tabla en HTML con la informacion requeridas
    Funcion: Crear la tabla de HTML y mostrarlo
    """
    global litaObjetos,pack
    informacion =""
    contador=0
    for carta in litaObjetos:
        if len(carta.getJuguetes())>1:
            if espar(contador):
                texto = """<tr style=background-color:#4682B4><td style="border: 1px solid black;"><fn style="font-size:25px;">"""+carta.getNombre()+"""</td>
                <td style="border: 1px solid black;"><fn style="font-size:25px;">""" + str(carta.getEdad()) + """</td>
                <td style="border: 1px solid black;"><fn style="font-size:25px;">""" + str(carta.getJuguetes())[1:-1]+ """</td>
                <td style="border: 1px solid black;"><fn style="font-size:25px;">""" + carta.getSexo() + """</td></tr></fn>"""
                informacion= informacion + texto
                contador+=1
            else:
                texto = """<tr style=background-color:#008080><td style="border: 1px solid black;"><fn style="font-size:25px;">"""+carta.getNombre()+"""</td>
                <td style="border: 1px solid black;"><fn style="font-size:25px;">""" + str(carta.getEdad()) + """</td>
                <td style="border: 1px solid black;"><fn style="font-size:25px;">""" + str(carta.getJuguetes())[1:-1] + """</td>
                <td style="border: 1px solid black;"><fn style="font-size:25px;">""" + carta.getSexo() + """</td></tr></fn>"""
                informacion= informacion + texto
                contador+=1

    htmlvarios = """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <meta name="description" content="Solicitantes de Varios Juguetes">
        <title>Solicitantes de dos o mas juguetes</title>
    <head>
    <body style="width:100%; display:flex; justify-content: center;">
        <table style="border: 1px solid black;">
                <caption><h2>Solicitantes de Varios Juguetes</h2></caption>
                <thead>
                <tr>
                    <th style="border: 1px solid black;"><fn style="font-size:25px;">Nombre</th></fn>
                    <th style="border: 1px solid black;"><fn style="font-size:25px;">Edad</th></fn>
                    <th style="border: 1px solid black;"><fn style="font-size:25px;">Juguetes</th></fn>
                    <th style="border: 1px solid black;"><fn style="font-size:25px;">Sexo</th></fn>
                </tr>
                </thead>
                <tbody>
                """+ informacion +"""
                </tbody>
        </table>
    </body>
    </html>
    """
        
    f = open('mostrarVariosJuguetes.html','w')
    f.write(htmlvarios)
    filename = 'file:///'+os.getcwd()+'/'+'mostrarVariosJuguetes.html'
    webbrowser.open(filename)
    

def HTML_Solicitantes(juguete):
    """
    Entradas: El jugete seleccionado en el combobox()
    Salidas: El archivo HTML en un browser
    Funcion: Crea y abre el HTML
    """
    global litaObjetos,pack
    informacion =""
    contador=0
    for carta in litaObjetos:
        for muneco in carta.getJuguetes():
            if muneco==juguete:
                if espar(contador):
                    texto ="""<tr style=background-color:#4682B4><td style="border: 1px solid black;"><fn style="font-size:25px;">"""+carta.getNombre()+"""
                    <td style="border: 1px solid black;"><fn style="font-size:25px;">""" + str(carta.getEdad()) + """</td></tr></fn>"""
                    informacion = informacion + texto
                    contador+=1
                    break
                
                else:
                    texto ="""<tr style=background-color:#008080><td style="border: 1px solid black;"><fn style="font-size:25px;">"""+carta.getNombre()+"""
                    <td style="border: 1px solid black;"><fn style="font-size:25px;">""" + str(carta.getEdad()) + """</td></tr></fn>"""
                    informacion = informacion + texto
                    contador+=1
                    break

    strTable = """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <meta name="description" content="Solicitantes por Juguetes">
        <title>Solicitantes por juguete</title>
    <head>
    <body style="width:100%; display:flex; justify-content: center;">
        <table style="border: 1px solid black;">
                <caption><h2>Solicitantes por juguete</h2></caption>
                <thead>
                <tr>
                    <th style="border: 1px solid black;"><fn style="font-size:25px;">Nombre</th></fn>
                    <th style="border: 1px solid black;"><fn style="font-size:25px;">Edad</th></fn>
                </tr>
                </thead>
                <tbody>
                """+ informacion +"""
                </tbody>
        </table>
    </body>
    </html>
    """
            
    html=strTable
    f = open('mostrarPorJuguete.html','w')
    f.write(html)
    filename = 'file:///'+os.getcwd()+'/'+'mostrarPorJuguete.html'
    webbrowser.open(filename)
#HTMLS
#=============================================
    
class Carta():
    """
    Entradas: Nombre,Sexo,Edad y cantidad de juguetes que se pidieron
    Salidas: Un objeto
    Funcion: Crea un objeto con los requisitos recibidos
    """
    def __init__(self, name, sex, age,juguetes):
        self.nombre=name
        self.sexo=sex
        self.edad=age
        self.juguetes=juguetes

    def getNombre(self):
        return self.nombre
    def getSexo(self):
        return self.sexo
    def getEdad(self):
        return self.edad
    def getJuguetes(self):
        return self.juguetes
      

def generarCartas(reps):
    """
    Entradas: Candidad de cartas a generar
    Salidas: Se agrega a la lista de cartas las cartas generadas
    Funcion: Se agrega a la lista de cartas las cartas generadas
    """
    global pack,listaObjetos
    faker = Faker()
    listasex=["Hombre","Mujer"]
    for i in range(reps):
        x=random.randint(1,3)
        juguetes=[]
        age=random.randint(1,12)
        sex=listasex[random.randint(0,1)]
        if sex=="Hombre":
            nombre=faker.name_male() +" "+ faker.last_name()
        else:
            nombre=faker.name_female() +" "+ faker.last_name()
            
        for cant in range(x):
            juguetes.append(pack[random.randint(0,len(pack)-1)][0])
        nino=Carta(nombre,sex,age,juguetes)
        litaObjetos.append(nino)

    if litaObjetos!=[]:
        generarReporte.config(state=NORMAL)


def cargarInventario():
    """
    Entradas: N/A
    Salidas: N/A
    Funcion: Carga en memoria el archivo xml y separa los elementos que tiene por nombre y decripcion en una matriz,
    tambien habilita el boton de generarCarta y carga la lista de objetos en memoria
    """
    global pack,litaObjetos
    load()
    tree=ET.parse('juguetes.xml')
    root=tree.getroot()
    lista=[]
    matriz=[]
    for child in root:
        if child.tag == 'juguete':
            for attr in child:
                var=attr.text
                lista.append(var[0:var.find('\n')])
            lista.append(child.attrib["ID"])
            matriz.append(lista)
            lista=[]
    pack=matriz
    generarCarta.config(state=NORMAL)
    
    if litaObjetos!=[]:
        generarReporte.config(state=NORMAL)

def ventana_una_carta(toor):
    toor.destroy()
    global litaObjetos,pack

    ppa=Tk()
    ppa.geometry("250x150")
    ppa.title("Solicitantes por Juguete")
    ppa.configure(background='#222222')
    ppa.resizable(FALSE, FALSE)

    kids=[]
    for i in litaObjetos:
        kids.append(i.getNombre())
        
    selectKid=ttk.Combobox(ppa,values=kids,width=30)
    selectKid.place(x=25,y=50)
    selectKid.set(kids[0])

    botonShow=Button(ppa,text="Mostrar",width=20,bg="#444444",fg="white",font=("arial",10,"bold"),command=lambda:HTML_Kid(selectKid.get()))
    botonShow.place(x=40,y=90)
    

def ventana_solicitantes_juguete(toor):
    """
    Entradas: La ventana anterior
    Salidas: N/A
    Funcion:Destruye la ventana anterior y crea la ventana con un combobox
    """
    toor.destroy()
    global pack,litaObjetos
    
    app=Tk()
    app.geometry("250x150")
    app.title("Solicitantes por Juguete")
    app.configure(background='#222222')
    app.resizable(FALSE, FALSE)
    
    toys=[]
    for i in pack:
        toys.append(i[0])

    selectJug=ttk.Combobox(app,values=toys,width=30)
    selectJug.place(x=25,y=50)
    selectJug.set(toys[0])

    botonMostrar=Button(app,text="Mostrar",width=20,bg="#444444",fg="white",font=("arial",10,"bold"),command=lambda:HTML_Solicitantes(selectJug.get()))
    botonMostrar.place(x=40,y=90)
    
def ventana_Generar_Carta():
    """
    Entradas: N/A
    Salidas: N/A
    Funcion: Crea la ventana que le pide al usuario la cantidad de cartas a generar
    """
    def verificar(var):
        """
        Entradas: El input del usuario
        Salidas: N/A
        Funcion: Valida que se haya digitado un numero entero
        """
        if var.isdigit():
            root.destroy()
            generarCartas(int(var))
        else:
            error=Label(root,text="Digite unicamente numeros enteros",bg="#222222",fg="red",width=30,font=("arial",8,"bold"))
            error.place(x=25,y=100)
            
    root=Tk()
    root.geometry("250x200")
    root.title("Generar Cartas")
    root.configure(background='#222222')
    root.resizable(FALSE, FALSE)

    titulo=Label(root,text="Generar Cartas",bg="#222222",fg="white",width=20,font=("arial",19,"bold"))
    titulo.pack(fill=BOTH)

    carta=StringVar()
    
    insertarReps=Label(root,text="Cartas a generar:",bg="#222222",fg="white",width=20,font=("arial",10,"bold"))
    insertarReps.place(x=25,y=55)
    

    cantidadCarta=Entry(root,width=5,textvariable=carta,font=("arial",10,"bold"))
    cantidadCarta.place(x=170,y=55)
    
    botonGenerar=Button(root,text="Generar cartas",width=20,bg="#444444",fg="white",font=("arial",10,"bold"),command=lambda: verificar(cantidadCarta.get()))
    botonGenerar.place(x=40,y=150)

    

def ventanaReportes():
    """
    Entradas: N/A
    Salidas: N/A
    Funcion: Crea la ventana de Reportes
    """
    toor=Tk()
    toor.geometry("400x250")
    toor.title("Generar Cartas")
    toor.configure(background='#222222')
    toor.resizable(FALSE, FALSE)

    solicitanteJuguete=Button(toor,text="Solicitantes por Juguete",width=40,bg="#444444",fg="white",font=("arial",10,"bold"),command=lambda:ventana_solicitantes_juguete(toor))
    solicitanteJuguete.place(x=40,y=40)
    
    juguetesMas=Button(toor,text="Interesados en 2 juguetes o mas",width=40,bg="#444444",fg="white",font=("arial",10,"bold"),command=lambda:HTML_VariosJuguetes())
    juguetesMas.place(x=40,y=80)

    inventario=Button(toor,text="Inventario",width=40,bg="#444444",fg="white",font=("arial",10,"bold"),command=lambda:HTML_Inventario())
    inventario.place(x=40,y=120)
    
    segunSexo=Button(toor,text="Lista solicitudes segun sexo",width=40,bg="#444444",fg="white",font=("arial",10,"bold"),command=lambda:HTML_Sexo())
    segunSexo.place(x=40,y=160)

    nino=Button(toor,text="Carta de un niño",width=40,bg="#444444",fg="white",font=("arial",10,"bold"),command=lambda:ventana_una_carta(toor))
    nino.place(x=40,y=200)

def salir():
    """
    Entradas: N/A
    Salidas: N/A
    Funcion: Llama a la funcion de guardar y cierra el programa
    """
    save()
    window.destroy()

#Ventana Principal 
#=============================================
window=Tk()
window.geometry("250x250")
window.title("Principal")
window.configure(background='#222222')
window.resizable(FALSE, FALSE)

titulo=Label(window,text="Carta a Santa",bg="#222222",fg="white",width=20,font=("arial",19,"bold"))
titulo.pack(fill=BOTH)

cargarInv=Button(window,text="Cargar Inventario",width=20,bg="#444444",fg="white",font=("arial",10,"bold"),command= lambda: cargarInventario())
cargarInv.place(x=40,y=65)

generarCarta=Button(window,text="Generar Carta",width=20,bg="#444444",fg="white",font=("arial",10,"bold"),state=DISABLED,command=lambda:ventana_Generar_Carta())
generarCarta.place(x=40,y=105)

generarReporte=Button(window,text="Reporte",width=20,bg="#444444",fg="white",font=("arial",10,"bold"),state=DISABLED,command= lambda:ventanaReportes())
generarReporte.place(x=40,y=145)

botonSalir=Button(window,text="Salir",width=20,bg="#444444",fg="white",font=("arial",10,"bold"),command=lambda:salir())
botonSalir.place(x=40,y=185)

window.mainloop()
