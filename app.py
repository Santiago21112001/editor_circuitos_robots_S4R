import tkinter as tk
from tkinter import filedialog
import json


class App:
    def __init__(self):
        self.barra_menu = None
        self.ventana = tk.Tk()
        self.ventana.title("Editor de circuitos y robots")
        self.crear_interfaz()
        self.ventana.mainloop()

    def crear_interfaz(self):
        self.barra_menu = tk.Menu(self.ventana)
        self.ventana.config(menu=self.barra_menu)

        self.crear_menu_archivo()

    def crear_menu_archivo(self):
        menu_archivo = tk.Menu(self.barra_menu, tearoff=0)
        self.barra_menu.add_cascade(label="Archivo", menu=menu_archivo)

        menu_archivo.add_command(label="Abrir", command=self.abrir_archivo)
        menu_archivo.add_command(label="Guardar", command=self.guardar_archivo)
        menu_archivo.add_separator()
        menu_archivo.add_command(label="Salir", command=self.ventana.destroy)

    def abrir_archivo(self):
        ruta_archivo = filedialog.askopenfilename(filetypes=[("Archivos JSON", "*.json")])
        if ruta_archivo:
            with open(ruta_archivo, 'r') as archivo:
                contenido = json.load(archivo)
                print("Contenido del archivo JSON:")
                print(contenido)

    def guardar_archivo(self):
        print("Función Guardar")
