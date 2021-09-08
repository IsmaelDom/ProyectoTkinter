from tkinter import *

# Definir ventana
ventana = Tk()
ventana.geometry("500x500")
ventana.title("Proyecto Tkinter - Python")

ventana.resizable(0,0)

# Pantallas
def home():
    # Montar Pantalla
    home_label.config(fg="white", bg="black", font=("Arial", 30), padx=210, pady=20)
    home_label.grid(row=0, column=0)

    # Ocultar otras pantallas
    add_label.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()

    return True

def add():
    # Montar Pantalla
    add_label.config(fg="white", bg="black", font=("Arial", 30), padx=120, pady=20)
    add_label.grid(row=0, column=0)

    # Ocultar otras pantallas
    home_label.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()

    return True

def info():
    # Montar Pantalla
    info_label.config(fg="white", bg="black", font=("Arial", 30), padx=150, pady=20)
    info_label.grid(row=0, column=0)

    data_label.grid(row=1, column=0)

    # Ocultar otras pantallas
    home_label.grid_remove()
    add_label.grid_remove()

    return True

# Variables importantes
name_data = StringVar()
price_data = StringVar()

# Definir campos de pantallas
home_label = Label(ventana, text = "Inicio")
add_label = Label(ventana, text = "Añadir Producto")
data_label = Label(ventana, text="Creado por Ismael")
info_label = Label(ventana, text = "Información")

# Campos del formulario
add_name_label = Label(ventana, text="Nombre del Producto")
add_name_entry = Entry(ventana, textvariable=name_data)

add_price_label = Label(ventana, text="Precio del Producto")
add_price_entry = Entry(ventana, textvariable=price_data)

add_description_label = Label(ventana, text="Descripción")
add_description_entry = Text(ventana)

# Carga Menu
home()

# Menu superior
menu_superior = Menu(ventana)
menu_superior.add_command(label="Inicio", command=home)
menu_superior.add_command(label="Añadir", command=add)
menu_superior.add_command(label="Información", command=info)
menu_superior.add_command(label="Salir", command=ventana.quit)

# Cargar Menu
ventana.config(menu=menu_superior)

# Cargar ventana
ventana.mainloop()