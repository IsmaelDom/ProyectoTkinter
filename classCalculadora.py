from tkinter import *
from tkinter import messagebox

class Calculadora:
    """docstring for Calculadora."""

    def __init__(self, alertas):
        self.numero1 = StringVar()
        self.numero2 = StringVar()
        self.resultado = StringVar()
        self.alertas = alertas
        
    def convertToFloat(self, numero):
        try:
            result = float(numero)
        except Exception as e:
            result = 0
            messagebox.showerror("Error", "Ingrese datos validos")
        
        return result

    def sumar(self):
        try:
            self.resultado.set(float(self.numero1.get()) + float(self.numero2.get()))
            self.mostrarResultado()
        except Exception as e:
            messagebox.showerror("Error", "Ingrese datos validos")

    def restar(self):
        self.resultado.set(self.convertToFloat(self.numero1.get()) - self.convertToFloat(self.numero2.get()))
        self.mostrarResultado()

    def multiplicar(self):
        self.resultado.set(self.convertToFloat(self.numero1.get()) * self.convertToFloat(self.numero2.get()))
        self.mostrarResultado()

    def dividir(self):
        self.resultado.set(self.convertToFloat(self.numero1.get()) / self.convertToFloat(self.numero2.get()))
        self.mostrarResultado()
        
    def mostrarResultado(self):
        self.alertas.showinfo("Resultado", f"El resultado es {self.resultado.get()}")
        self.numero1.set("")
        self.numero2.set("")

# Crear ventana raiz
ventana = Tk()
ventana.title("Ejercicio con TKinter")
ventana.geometry("400x400")
ventana.config(bd=25)

calculadora = Calculadora(messagebox)

marco = Frame(ventana, width=300, height=200)
marco.config(padx=15, pady=15, bd=5, relief=SOLID)
marco.pack(side=TOP, anchor=CENTER)
marco.pack_propagate(False)

Label(marco, text="Primer Numero: ").pack()
Entry(marco, textvariable=calculadora.numero1, justify="center").pack()

Label(marco, text="Segundo Numero: ").pack()
Entry(marco, textvariable=calculadora.numero2, justify="center").pack()

Label(marco, text="").pack()

Button(marco, text="Sumar", command=calculadora.sumar).pack(side="left", fill=X, expand=YES)
Button(marco, text="Restar", command=calculadora.restar).pack(side="left", fill=X, expand=YES)
Button(marco, text="Multiplicar", command=calculadora.multiplicar).pack(side="left", fill=X, expand=YES)
Button(marco, text="Dividir", command=calculadora.dividir).pack(side="left", fill=X, expand=YES)

ventana.mainloop()