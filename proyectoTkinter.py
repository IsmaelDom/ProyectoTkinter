from tkinter import *
from tkinter import ttk

# Definir ventana
ventana = Tk()
#ventana.geometry("500x500")
# La ventana se va acoplando al tamaño del contenido
ventana.minsize(500, 500)
ventana.title("Proyecto Tkinter - Python")

ventana.resizable(0,0)

# Pantallas
def home():
    # Montar Pantalla
    home_label.config(fg="white", bg="black", font=("Arial", 30), padx=210, pady=20)
    home_label.grid(row=0, column=0)

    products_box.grid(row=2)
    """
    # Se listan los productos
    for product in products:
        if len(product) == 3:
            product.append("added")
            Label(products_box, text=product[0]).grid()
            Label(products_box, text=product[1]).grid()
            Label(products_box, text=product[2]).grid()
            Label(products_box, text="-----------------------------------").grid()
    """
    # Se va a mostrar en la tabla
    for product in products:
        if len(product) == 3:
            product.append("added")
            products_box.insert('', 0, text=product[0], values=(product[1]))
            

    # Ocultar otras pantallas
    add_label.grid_remove()
    add_frame.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()

    return True

def add():
    # Montar Pantalla
    add_label.config(fg="white", bg="black", font=("Arial", 30), padx=120, pady=20)
    add_label.grid(row=0, column=0, columnspan=10)

    # Campos del formulario
    add_frame.grid(row=1)
    add_name_label.grid(row=1, column=0, padx=5, pady=5, sticky=E)
    add_name_entry.grid(row=1, column=1, padx=5, pady=5, sticky=W)

    add_price_label.grid(row=2, column=0, padx=5, pady=5, sticky=E)
    add_price_entry.grid(row=2, column=1, padx=5, pady=5, sticky=W)

    add_description_label.grid(row=3, column=0, padx=5, pady=5, sticky=NW)
    add_description_entry.grid(row=3, column=1, padx=5, pady=5, sticky=W)
    add_description_entry.config(width=30, height=5, font=("Consolas", 12), padx=15, pady=15)

    add_separator.grid(row=4, column=1)

    boton.grid(row=5, column=1, sticky=E)
    boton.config(padx=15, pady=5, bg="red", fg="white", cursor="hand2")

    # Ocultar otras pantallas
    home_label.grid_remove()
    products_box.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()

    return True

def info():
    # Montar Pantalla
    info_label.config(fg="white", bg="black", font=("Arial", 30), padx=150, pady=20)
    info_label.grid(row=0, column=0)

    data_label.grid(row=2, column=0)

    # Ocultar otras pantallas
    home_label.grid_remove()
    products_box.grid_remove()
    add_frame.grid_remove()
    add_label.grid_remove()

    return True

def addProducto():
    products.append([
        name_data.get(),
        price_data.get(),
        add_description_entry.get("1.0", "end-1c")
    ])

    # Se limpian los campos del formulario
    name_data.set("")
    price_data.set("")
    add_description_entry.delete("1.0", END)

    # Retorna a home
    home()

# Variables importantes
products = []
name_data = StringVar()
price_data = StringVar()

# Definir campos de pantallas
home_label = Label(ventana, text = "Inicio")
add_label = Label(ventana, text = "Añadir Producto")
data_label = Label(ventana, text="Creado por Ismael")
info_label = Label(ventana, text = "Información")

#products_box = Frame(ventana, width=250)
Label(ventana).grid(row=1)

# Se crea una tabla para mostrar los productos
#Label(products_box).grid(row=0)
products_box = ttk.Treeview(height=12, columns=2)
products_box.grid(row=1, column=0, columnspan=2)
products_box.heading("#0", text="Producto", anchor=W)
products_box.heading("#1", text="Precio", anchor=W)

# Campos del formulario
add_frame = Frame(ventana)

add_name_label = Label(add_frame, text="Nombre:")
add_name_entry = Entry(add_frame, textvariable=name_data)

add_price_label = Label(add_frame, text="Precio:")
add_price_entry = Entry(add_frame, textvariable=price_data)

add_description_label = Label(add_frame, text="Descripción:")
add_description_entry = Text(add_frame)

add_separator = Label(add_frame)
boton = Button(add_frame, text="Guardar", command=addProducto)

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