from tkinter import *
import os.path

class Programa(object):
    """docstring for Programa."""
    def __init__(self):
        self.title = "Master en Python"
        self.icon = "./img/logo.ico"
        self.icon_alt = "./tkinter/img/logo.ico"
        self.size = "770x470"
        self.resizable = False

    def cargar(self):
        
        # Crear ventana raiz
        ventana = Tk()
        self.ventana = ventana

        # Titulo de la ventana
        ventana.title(self.title)

        # Comprobar si existe un archivo
        ruta_icono = os.path.abspath(self.icon)

        # Mostrar texto en la ventana
        texto = Label(ventana, text = ruta_icono)
        texto.pack()

        if not os.path.isfile(ruta_icono):
            ruta_icono = os.path.abspath(self.icon_alt)

        # Icono de la ventana con ruta de path
        ventana.iconbitmap(ruta_icono)

        # Cambio en el tamaño de la ventana
        ventana.geometry(self.size)

        # Icono de la ventana
        # ventana.iconbitmap("img/logo.ico")

        # Bloquear el tamaño de la ventana
        '''
        ventana.resizable(0,0) no permite que se cambie el tamaño de la ventana
        ventana.resizable(0,1) permite que se cambie el tamaño del largo de la ventana
        ventana.resizable(1,0) permite que se cambie el tamaño del ancho de la ventana
        ventana.resizable(1,1) permite que se cambie el tamaño de la ventana
        '''
        if self.resizable:
            ventana.resizable(1,1)
        else:
            ventana.resizable(0,0)

        # Arrancar y mostrar la ventana hasta que se cierre
        # ventana.mainloop()

    def addTexto(self, dato):
        texto = Label(self.ventana, text = dato)
        texto.pack()

    def mostrar(self):
        # Arrancar y mostrar la ventana hasta que se cierre
        self.ventana.mainloop()

# Instanciar el programa
programa = Programa()
programa.cargar()
programa.addTexto("Hola mundo")
programa.addTexto("Desde Python")
programa.mostrar()