from tkinter import *
from PIL import Image,ImageTk
import tkinter.messagebox

#Cargar y separar lista 
#=============================================
def read():
    f=open("BDPostalCR.txt","r")
    content=f.read()
    return quebrarCodigo(content)

def quebrarCodigo(content):
    mat=[]
    lista=content.split("\n")
    for i in lista:
        mat.append(i.split(";"))    
    return mat

def getProvincias(lista):
    prov=[]
    for fila in lista:
        if fila[0] not in prov:
            prov.append(fila[0])
    return prov

def getCantones(prov):
    lista=read()
    lista.pop()
    cant=[]
    for fila in lista:
        if fila[0]==prov:
            if fila[1] not in cant:
                cant.append(fila[1])
    return cant

def getDistrito(cant):
    lista=read()
    lista.pop()
    dist=[]
    for fila in lista:
        if fila[1]==cant:
            if fila[2] not in dist:
                dist.append(fila[2])
    return dist

def combobox():

    def setCanton(event):
        listaCant=getCantones(selectProv.get())
        selectCant.config(values=listaCant)

    def setDistrito(event):
        listaDist=getDistrito(selectCant.get())
        selectDist.config(values=listaDist)

    listaprov=getProvincias(read())
    listax=[]

    selectProv=ttk.Combobox(root,values=listaprov)
    selectProv.place(x=250,y=115)
    selectProv.current(0)
    selectProv.bind('<<ComboboxSelected>>',setCanton)

    selectCant=ttk.Combobox(root,values=listax)
    selectCant.place(x=250,y=150)
    selectCant.bind('<<ComboboxSelected>>',setDistrito)

    selectDist=ttk.Combobox(root,values=listax)
    selectDist.place(x=250,y=190)

#Second window(progress)
#=============================================
def secondwindow():
    root=Tk()
    root.geometry("500x400")
    root.title("Beta 1.1")
    root.configure(background='#222222')

    header=Label(root,text="Codigo",relief="solid",bg="#333333",fg="White",width=20,font=("arial",19,"bold"))
    header.pack(fill=BOTH,)

    prov=Label(root,text="Provincia",bg="#333333",fg="White",width=15,font=("arial",15,"bold"))
    prov.place(x=50,y=110)

    cant=Label(root,text="Canton",bg="#333333",fg="White",width=15,font=("arial",15,"bold"))
    cant.place(x=50,y=150)

    dist=Label(root,text="Distrito",bg="#333333",fg="White",width=15,font=("arial",15,"bold"))
    dist.place(x=50,y=190)

    dist=Label(root,text="Su codigo postal es: ",bg="#333333",fg="White",width=18,font=("arial",15,"bold"))
    dist.place(x=50,y=230)
    
    combobox()

    #codigoZip=Label(root,text="hola",bg="#333333",fg="White",width=18,font=("arial",15,"bold"))
    #codigoZip.place(x=280,y=230)

#Habilitar botones 1st window (Done)
#=============================================
    
def botonesHabilitados():

    lista=read()

    generarSobre=Button(window,text="Generar Sobre",width=15,bg="#444444",fg="white",font=("arial",10,"bold"),command=secondwindow)
    generarSobre.place(x=35,y=105)
    generarSobre.config(state="normal")

    crearReporte=Button(window,text="Generar Reporte",width=15,bg="#444444",fg="white",font=("arial",10,"bold"),command=print("Hola"))#command
    crearReporte.place(x=35,y=145)
    crearReporte.config(state="normal")
    

#Ventana Principal (Progreso)
#=============================================
window=Tk()
window.geometry("200x200")
window.title("Beta")
window.configure(background='#222222')

titulo=Label(window,text="Administración",bg="#222222",fg="white",width=20,font=("arial",19,"bold"))
titulo.pack(fill=BOTH,)

cargarBD=Button(window,text="Cargar BD",width=15,bg="#444444",fg="white",font=("arial",10,"bold"),command=botonesHabilitados)
cargarBD.place(x=35,y=65)

window.mainloop()
