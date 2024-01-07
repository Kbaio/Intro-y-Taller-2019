from tkinter import *

def doDisable():
    b2.configure(state=DISABLED)

root = Tk()
b2 = Button(root, text="Disable button",command="hola")
b2.pack()
root.mainloop()
