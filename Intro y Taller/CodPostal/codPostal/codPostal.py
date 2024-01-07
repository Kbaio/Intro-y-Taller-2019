#Creado por David Salazar
#Fecha de Creacion: 12/09/2019 6:24pm
#Ultima modificacion: 3/10/2019 10:22pm
#ver:3.7.3

#Importaciones
from tkinter import *
import tkinter.messagebox
from tkinter import ttk
import tkinter as tk
from reportlab.pdfgen import canvas
from reportlab.lib.colors import white,red,green,blue,gray,black
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from os import startfile
import os
import webbrowser


#Variables Globales
listacortada=[]
direcc=""
listaPDF=[]

def espar(num):
      """
      Funcion es par devuelve True si la entrada es par o no
      """
      if num%2==0:
            return True
      else:
            return False

def setHTML(informacion):
      """
      Funcion: recibe la variable de la funcion generarHTML y la coloca en el formato correspondiente para ser leido en HTML retorna el codigo HTML completo
      """
      strTable = """
      <!DOCTYPE html>
      <html>
      <head>
            <meta charset="UTF-8">
            <meta name="description" content="Lista de codigos Zip">
            <title>Codigos Zip</title>
      <head>
      <body style="width:100%; display:flex; justify-content: center;">
            <table style="border: 1px solid black;">
                  <caption><h2>Codigos Zip</h2></caption>
                  <thead>
                  <tr>
                        <th style="border: 1px solid black;">Provincia</th>
                        <th style="border: 1px solid black;">Canton</th>
                        <th style="border: 1px solid black;">Distrito</th>
                        <th style="border: 1px solid black;">Zip</th>
                  </tr>
                  </thead>
                  <tbody>
                  """+ informacion +"""
                  </tbody>
            </table>
      </body>
      </html>
      """  
      return strTable

def generarHtml():
      """
      Funcion: Quiebra toda la lista de codigos zip y lo almacena en una variable mete en la funcion setHTML luego lo guarda
      """
      informacion = ""
      contador=0
      for i in listacortada:
            if espar(contador):
                  numeros=i[3]
                  verde = numeros[0]
                  celeste = numeros[1]+numeros[2]
                  rojo = numeros[3] + numeros[4]
                  texto = """<tr style=background-color:#F5CBA7><td style="border: 1px solid black;">"""+i[0]+"""</td>
                  <td style="border: 1px solid black;">""" + i[1] + """</td>
                  <td style="border: 1px solid black;">""" + i[2] + """</td>
                  <td style="border: 1px solid black;">"""+"""<len style=color:#45B39D>"""+verde+"""</len>"""+"""<len style=color:#3498DB>"""+celeste+"""</len>"""+"""<len style=color:#FF0000>"""+rojo+"""</len>"""+ """</td></tr>"""
                  informacion = informacion + texto
                  contador+=1
            else:
                  numeros=i[3]
                  verde = numeros[0]
                  celeste = numeros[1]+numeros[2]
                  rojo = numeros[3] + numeros[4]
                  texto = """<tr style=background-color:#F7DC6F><td style="border: 1px solid black;">"""+i[0]+"""</td>
                  <td style="border: 1px solid black;">""" + i[1] + """</td>
                  <td style="border: 1px solid black;">""" + i[2] + """</td>
                  <td style="border: 1px solid black;">"""+"""<len style=color:#45B39D>"""+verde+"""</len>"""+"""<len style=color:#3498DB>"""+celeste+"""</len>"""+"""<len style=color:#FF0000>"""+rojo+"""</len>"""+ """</td></tr>"""
                  informacion = informacion + texto
                  contador+=1
      html = setHTML(informacion)
      f = open('codigoPostal.html','w')
      f.write(html)
      filename = 'file:///'+os.getcwd()+'/'+'codigoPostal.html'
      webbrowser.open(filename)
    

#Cargar y separar lista (progreso)
#=============================================
def read():
    """
    Funcion: lee el archivo de textos y lo guarda en una variable para mandarlo a la funcon quebrarCodigo
    """
    f=open("BDPostalCR.txt","r")
    content=f.read()
    return quebrarCodigo(content)

def quebrarCodigo(content):
    """
    Funcion: Recibe los contenidos del archivo de texto y los separa en listas. 
    """
    mat=[]
    lista=content.split("\n")
    for i in lista:
        mat.append(i.split(";"))    
    return mat

def getProvincias():
    """
    Funcion: Saca las provincias de la lista global con los codigos zip
    """ 
    listacortada
    prov=[]
    for fila in listacortada:
        if fila[0] not in prov:
            prov.append(fila[0])
    return prov

def getCantones(prov):
    """
    Funcion: Saca los cantones de la lista global con los codigos zip en base a la provincia que se eligio en la combobox
    """ 
    listacortada
    cant=[]
    for fila in listacortada:
        if fila[0]==prov:
            if fila[1] not in cant:
                cant.append(fila[1])
    return cant

def getDistrito(cant):
    """
    Funcion: Saca los distritos de la lista global con los codigos zip en base al canton que se eligio en la combobox
    """ 
    listacortada
    dist=[]
    for fila in listacortada:
        if fila[1]==cant:
            if fila[2] not in dist:
                dist.append(fila[2])
    return dist

def getZip(prov,cant,dist):
    """
    Funcion: En base a las opciones marcadas en los combobox se saca el codigo zip en la lista de codigos zip global
    """ 
    listacortada
    czip=""
    for fila in listacortada:
        if fila[0]==prov:
            if fila[1]==cant:
                if fila[2]==dist:
                    czip=fila[3]
    return czip

def getDirgen():
    """
    Funcion: Se saca la provincia,canton y distrito en base al zip de la lista global: direcc 
    """ 
    listacortada
    direcc
    for fila in listacortada:
        if fila[3]==direcc:
            exactitud=fila[0]+","+fila[1]+","+fila[2]
    return str(exactitud)
    

#CrearPDF
#=============================================
def crearPDF():
      """
      Funcion: Crea el PDF con la lista global:listaPDF en base a las opciones
      """
      if listaPDF[0]=="":
            nombre_archivo=("nombre.pdf")
            pdf=canvas.Canvas(nombre_archivo)
      else:
            nombre_archivo=(listaPDF[0]+".pdf")
            pdf=canvas.Canvas(nombre_archivo)

      pdfmetrics.registerFont(TTFont('GOTHIC', 'GOTHIC.ttf'))
      pdfmetrics.registerFont(TTFont('GOTHICB', 'GOTHICB.ttf'))
      
      cx=250
      cy=550
      ancho=300
      alto=150

      pdf.setFont('Times-Italic', 32)
      pdf.setFillColor(blue)
      pdf.drawString(60,800,"Costa Rica")

      pdf.setFont('Times-Italic', 20)
      pdf.setFillColor(black)
      pdf.drawString(60,650,direcc)

      pdf.setFillColor(red)
      pdf.rect(cx,cy,ancho,alto)

      pdf.line(10,780,x2=700,y2=780)

      if listaPDF[0]=="":
        pdf.setFont('GOTHICB', 12)
        pdf.setFillColor(black)
        pdf.drawString(cx+40,cy+100,"Nombre")
      else:
        pdf.setFont('GOTHICB', 12)
        pdf.setFillColor(black)
        pdf.drawString(cx+40,cy+100,listaPDF[0])

      if listaPDF[1]=="":
        pdf.setFont('GOTHIC', 12)
        pdf.setFillColor(black)
        pdf.drawString(cx+40,cy+85,"Direccion Exacta")
      else:
        pdf.setFont('GOTHIC', 12)
        pdf.setFillColor(black)
        pdf.drawString(cx+40,cy+85,listaPDF[1])

      pdf.setFillColor(black)
      pdf.drawString(cx+40,cy+70,listaPDF[2])

      pdf.setFillColor(black)
      pdf.drawString(cx+40,cy+55,direcc)

      pdf.drawImage("logo.png",cx+275,cy+125,20,20)

      pdf.showPage()
      pdf.save()
      startfile(nombre_archivo)
    
#Ventana 3
#=============================================
def thirdwindow():
      """
      funcion= Creacion de la tercera ventana
      """
      def closetirdwindow():
          """
          funcion= Llama a la funcion de crear PDF y cierra la tercera ventana
          """
          crearPDF()
          app.destroy()

      def getinputs():
        """
        funcion= Se sacan todos los inputs de las entrys para meterlos en una lista global: listaPDF que se utiliza en la creacion del PDF 
        """
        nombre=entNombre.get()
        direccion=entDireccion.get()
        listaPDF.append(nombre)
        listaPDF.append(direccion)
        listaPDF.append(strDirgen)
        closetirdwindow()

      global direcc
      app=Tk()
      app.geometry("600x400")
      app.title("Formato de la Direccion")
      app.configure(background='#222222')

      title=Label(app,text="Formato de la Dirección",bg="#333333",fg="White",width=20,font=("arial",19,"bold"))
      title.pack(fill=BOTH,)

      nombre=Label(app,text="Nombre",bg="#333333",fg="White",width=18,font=("arial",15,"bold"))
      nombre.place(x=30,y=110)

      direccion=Label(app,text="Dirección Especifica",bg="#333333",fg="White",width=18,font=("arial",15,"bold"))
      direccion.place(x=30,y=150)

      direccionGeneral=Label(app,text="Dirección General",bg="#333333",fg="White",width=18,font=("arial",15,"bold"))
      direccionGeneral.place(x=30,y=190)

      codigo=Label(app,text="Código",bg="#333333",fg="White",width=18,font=("arial",15,"bold"))
      codigo.place(x=30,y=230)

      CR=Label(app,text="Costa Rica",bg="#333333",fg="White",width=18,font=("arial",15,"bold"))
      CR.place(x=30,y=270)

      strDirgen=getDirgen()
      
      entNombre=Entry(app,width=40,font=("arial",10,"bold"))
      entNombre.place(x=260,y=115)

      entDireccion=Entry(app,width=40,font=("arial",10,"bold"))
      entDireccion.place(x=260,y=155)

      entDirgeneral=Label(app,text=strDirgen,bg="#333333",fg="White",width=40,font=("arial",10,"bold"))
      entDirgeneral.place(x=260,y=190)

      entCodigo=Label(app,text=direcc,bg="#333333",fg="White",width=18,font=("arial",15,"bold"))
      entCodigo.place(x=260,y=230)

      genPDF=Button(app,text="Generar PDF",width=15,bg="brown",fg="white",font=("arial",10,"bold"),command=getinputs)
      genPDF.place(x=240,y=320)
    
#Combobox, entry box y botones ventana 2 (Done)
#=============================================
def combobox(root):
    """
    Funcion: Crea las comboboxes de la segunda ventana y se bindean a las respectivas funciones.
    """
    def setCanton(event):
        """
        Funcion: Cuado se elige la provincia en el primer combobox se bindea a esta funcion para sacar la lista de cantones.
        """
        listaCant=getCantones(selectProv.get())
        selectCant.set('')
        selectDist.set('')
        codigoZip.config(text="")
        selectCant.config(values=listaCant)

    def setDistrito(event):
        """
        Funcion: Cuado se elige el canton en la segunda combobox se bindea a esta funcion para sacar la lista de distritos.
        """
        listaDist=getDistrito(selectCant.get())
        selectDist.set('')
        codigoZip.config(text="")
        selectDist.config(values=listaDist)
        
    def setZip(event):
        """
        Funcion: Cuado se elige el distrito se muestra automaticamente el zip y a la vez lo guarda en una variable global
        """
        global direcc
        sip=getZip(selectProv.get(),selectCant.get(),selectDist.get())
        direcc=sip
        codigoZip.config(text=sip)
        siguiente.config(state="normal")
    def closewindow():
        """
        Funcion: Una vez el boton "Siguiente" es clickeado llama esta funcion para cerrar la segunda ventana y abrir la tercera
        """
        thirdwindow()
        root.destroy()
        
    listaprov=getProvincias()
    listax=[]

    selectProv=ttk.Combobox(root,values=listaprov)
    selectProv.place(x=230,y=115)
    selectProv.set("")
    selectProv.bind("<<ComboboxSelected>>",setCanton)

    selectCant=ttk.Combobox(root,values=listax)
    selectCant.place(x=230,y=155)
    selectCant.bind("<<ComboboxSelected>>",setDistrito)

    selectDist=ttk.Combobox(root,values=listax)
    selectDist.place(x=230,y=195)
    selectDist.bind("<<ComboboxSelected>>",setZip)

    codigoZip=Label(root,bg="#333333",fg="White",width=15,font=("arial",10,"bold"))
    codigoZip.place(x=230,y=235)

    siguiente=Button(root,text="Siguiente",width=15,bg="brown",fg="white",font=("arial",10,"bold"),command=closewindow)
    siguiente.config(state="disabled")
    siguiente.place(x=140,y=300)

#Second window(Done)
#=============================================
def secondwindow():
    """
    Funcion: Crea la segunda ventana con labels, botones y combobox una vez el boton de generar sobre es clickeado, llama a la funcion combobox.
    """
        
    root=Tk()
    root.geometry("400x400")
    root.title("Crear Codigo")
    root.configure(background='#222222')

    header=Label(root,text="Dirección",bg="#333333",fg="White",width=20,font=("arial",19,"bold"))
    header.pack(fill=BOTH,)

    prov=Label(root,text="Provincia",bg="#333333",fg="White",width=15,font=("arial",15,"bold"))
    prov.place(x=30,y=110)

    cant=Label(root,text="Canton",bg="#333333",fg="White",width=15,font=("arial",15,"bold"))
    cant.place(x=30,y=150)

    dist=Label(root,text="Distrito",bg="#333333",fg="White",width=15,font=("arial",15,"bold"))
    dist.place(x=30,y=190)

    dist=Label(root,text="Código Zip",bg="#333333",fg="White",width=15,font=("arial",15,"bold"))
    dist.place(x=30,y=230)

    combobox(root)

    
    
def botonesHabilitados():
    """
    Funcion:Habilita los botones de Sobre y Reporte tambien carga la lista en una variable global
    """
    global listacortada
    f=open("BDPostalCR.txt","r")
    content=f.read()
    listacortada=quebrarCodigo(content)
    listacortada.pop()
    
    generarSobre=Button(window,text="Generar Sobre",width=15,bg="#444444",fg="white",font=("arial",10,"bold"),command=secondwindow)
    generarSobre.place(x=35,y=105)
    generarSobre.config(state="normal")

    crearReporte=Button(window,text="Generar Reporte",width=15,bg="#444444",fg="white",font=("arial",10,"bold"),command=generarHtml)
    crearReporte.place(x=35,y=145)
    crearReporte.config(state="normal")

#Ventana Principal (Done)
#=============================================
"""
Creacion de la ventana principal con los botones de Generar Sobre y Generar Reporte deshabilitados
"""
window=Tk()
window.geometry("200x200")
window.title("Ventana Principal")
window.configure(background='#222222')

lista=[]
titulo=Label(window,text="Administración",bg="#222222",fg="white",width=20,font=("arial",19,"bold"))
titulo.pack(fill=BOTH,)

cargarBD=Button(window,text="Cargar BD",width=15,bg="#444444",fg="white",font=("arial",10,"bold"),command=botonesHabilitados)
cargarBD.place(x=35,y=65)

generarSobre=Button(window,text="Generar Sobre",width=15,bg="#444444",fg="white",font=("arial",10,"bold"))
generarSobre.place(x=35,y=105)
generarSobre.config(state="disabled")

crearReporte=Button(window,text="Generar Reporte",width=15,bg="#444444",fg="white",font=("arial",10,"bold"))
crearReporte.place(x=35,y=145)
crearReporte.config(state="disabled")

window.mainloop()
