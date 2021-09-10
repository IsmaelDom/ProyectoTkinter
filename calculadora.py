from tkinter import *
from tkinter import messagebox

# Crear ventana raiz
ventana = Tk()
ventana.title("Ejercicio con TKinter")
ventana.geometry("400x400")
ventana.config(bd=25)

def convertToFloat(numero):
    try:
        result = float(numero)
    except Exception as e:
        result = 0
        messagebox.showerror("Error", "Ingrese datos validos")
    
    return result

def sumar():
    try:
        resultado.set(float(numero1.get()) + float(numero2.get()))
        mostrarResultado()
    except Exception as e:
        messagebox.showerror("Error", "Ingrese datos validos")

def restar():
    resultado.set(convertToFloat(numero1.get()) - convertToFloat(numero2.get()))
    mostrarResultado()

def multiplicar():
    resultado.set(convertToFloat(numero1.get()) * convertToFloat(numero2.get()))
    mostrarResultado()

def dividir():
    resultado.set(convertToFloat(numero1.get()) / convertToFloat(numero2.get()))
    mostrarResultado()
    
def mostrarResultado():
    messagebox.showinfo("Resultado", f"El resultado es {resultado.get()}")
    numero1.set("")
    numero2.set("")

numero1 = StringVar()
numero2 = StringVar()
resultado = StringVar()

marco = Frame(ventana, width=300, height=200)
marco.config(padx=15, pady=15, bd=5, relief=SOLID)
marco.pack(side=TOP, anchor=CENTER)
marco.pack_propagate(False)

Label(marco, text="Primer Numero: ").pack()
Entry(marco, textvariable=numero1, justify="center").pack()

Label(marco, text="Segundo Numero: ").pack()
Entry(marco, textvariable=numero2, justify="center").pack()

Label(marco, text="").pack()

Button(marco, text="Sumar", command=sumar).pack(side="left", fill=X, expand=YES)
Button(marco, text="Restar", command=restar).pack(side="left", fill=X, expand=YES)
Button(marco, text="Multiplicar", command=multiplicar).pack(side="left", fill=X, expand=YES)
Button(marco, text="Dividir", command=dividir).pack(side="left", fill=X, expand=YES)

ventana.mainloop()