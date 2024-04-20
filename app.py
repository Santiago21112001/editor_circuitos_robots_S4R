import tkinter as tk
from tkinter import filedialog
import json
from draggable_rectangle import DraggableRectangle


class App:
    def __init__(self):
        self.ventana = self.__crear_ventana()

        canvas = tk.Canvas(self.ventana, width=400, height=400)
        canvas.pack()

        self.barra_menu = tk.Menu(self.ventana)
        self.ventana.config(menu=self.barra_menu)

        self.__crear_menu_archivo()
        self.parts = [DraggableRectangle(canvas, 50, 50, 150, 150),
                      DraggableRectangle(canvas, 200, 200, 300, 300)]

        self.ventana.mainloop()

    def __crear_ventana(self):
        ventana = tk.Tk()
        ventana.title("Editor de circuitos y robots")
        ventana.resizable(False, False)
        return ventana

    def __crear_menu_archivo(self):
        menu_archivo = tk.Menu(self.barra_menu, tearoff=0)
        self.barra_menu.add_cascade(label="Archivo", menu=menu_archivo)

        menu_archivo.add_command(label="Abrir", command=self.__abrir_archivo)
        menu_archivo.add_command(label="Guardar", command=self.__guardar_archivo)
        menu_archivo.add_command(label="Añadir pieza", command=self.__anadir_pieza)
        menu_archivo.add_separator()
        menu_archivo.add_command(label="Salir", command=self.ventana.destroy)

    def __anadir_pieza(self):
        self.parts.append(DraggableRectangle(self.ventana))

    def __abrir_archivo(self):
        ruta_archivo = filedialog.askopenfilename(filetypes=[("Archivos JSON", "*.json")])
        if ruta_archivo:
            with open(ruta_archivo, 'r') as archivo:
                contenido = json.load(archivo)
                print("Contenido del archivo JSON:")
                print(contenido)

    def __guardar_archivo(self):
        partsJSON = []
        for i in range(len(self.parts)):
            partsJSON.append(self.parts[i].get_rect_info())
            if i != len(self.parts) - 1:
                partsJSON.append(",")
        contenido = {
            "circuits": [
                {
                    "name": "circuit",
                    "parts": partsJSON
                }
            ]
        }
        self.__crear_archivo_json(contenido, "circuits.json")

    def __crear_archivo_json(self, contenido, nombre_archivo):
        with open(nombre_archivo, 'w') as archivo:
            json.dump(contenido, archivo, indent=4)
        print(f"Se ha creado el archivo JSON '{nombre_archivo}'.")
