from tkinter import *

# Definir ventana
ventana = Tk()
ventana.geometry("500x500")
ventana.title("Proyecto Tkinter - Python")

ventana.resizable(0,0)

# Pantallas
def home():
    home_label = Label(ventana, text = "Inicio")
    home_label.config(fg="white", bg="black", font=("Arial", 30), padx=20, pady=20)
    home_label.grid(row=0, column=0)

    return True

def add():
    return True

def info():
    return True

# Carga Menu
home()

# Menu superior
menu_superior = Menu(ventana)
menu_superior.add_command(label="Inicio")
menu_superior.add_command(label="Añadir")
menu_superior.add_command(label="Información")
menu_superior.add_command(label="Salir", command=ventana.quit)

# Cargar Menu
ventana.config(menu=menu_superior)

# Cargar ventana
ventana.mainloop()