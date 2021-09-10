from tkinter import *

# Crear ventana raiz
ventana = Tk()
ventana.geometry("500x500")

# Titulo de la ventana
ventana.title("Practica texto")

texto = Label(ventana, text = "Bienvenido a mi aplicación")

# Se cambia el color del fondo y letra, tambien se agrega un padding, fuente y tamaño
texto.config(fg = "red", bg = "black", padx = 50, pady = 30, font = ("Consolas", 20))
texto.pack()

texto = Label(ventana, text = "By dev Ismael")
texto.config(#width = 400,
            height = 3,
            bg = "orange",
            font = ("Arial", 20),
            cursor = "spider")
texto.pack(anchor = SE)

def pruebas(nombre, apellido, pais):
    return f"Hola {nombre} {apellido} eres de {pais}"

texto = Label(ventana, text = pruebas(apellido="Dom", pais="Mexico", nombre="Ismael"))
texto.config(#width = 400,
            height = 4,
            bg = "green",
            font = ("Algerian", 15),
            cursor = "spider")
texto.pack(anchor = NW)

ventana.mainloop()