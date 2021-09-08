from tkinter import *
from tkinter import messagebox as MessageBox

# Crear ventana raiz
ventana = Tk()
ventana.geometry("700x600")

# Titulo de la ventana
ventana.title("Formularios en TKinter")
ventana.config(bd=50)

def getDato():
    resultado.set(dato.get())

    if len(resultado.get()) >= 1:
        texto_ingresado.config(bg="black", fg="red")
        MessageBox.showwarning("Alerta", "Hola desde Python")
    else:
        MessageBox.showerror("Atención", "Ingrese un mensaje")

def salir(nombre):
    resultado = MessageBox.askquestion("Salir", "En verdad, ¿desea salir?")
    if resultado == "yes":
        MessageBox.showinfo("¡Adios!", f"Saliendo... Adios {nombre}")
        ventana.destroy()

dato = StringVar()
resultado = StringVar()

Label(ventana, text="Ingrese un texto:").pack(anchor=NW)
Entry(ventana, textvariable=dato).pack(anchor=NW)

Label(ventana, text="Dato Ingresado:").pack(anchor=NW)
texto_ingresado = Label(ventana, textvariable=resultado)
texto_ingresado.pack(anchor=NW)

Button(ventana, text="Mostrar Info.", command=getDato).pack(anchor=NW)
# Label separador
Label(ventana).pack()

Button(ventana, text="Salir", command=lambda: salir("User")).pack(anchor=NW)

ventana.mainloop()