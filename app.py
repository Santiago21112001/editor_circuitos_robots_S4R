import tkinter as tk
from tkinter import filedialog
import json
from draggable_rectangle import DraggableRectangle

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Editor de circuitos y robots")
        self.root.resizable(False, False)

        self.canvas = tk.Canvas(self.root, width=400, height=400)
        self.canvas.pack()

        self.create_menu()
        self.create_draggable_rectangles()

        self.root.mainloop()

    def create_menu(self):
        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)

        file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Archivo", menu=file_menu)

        file_menu.add_command(label="Abrir", command=self.open_file)
        file_menu.add_command(label="Guardar", command=self.save_file)
        file_menu.add_command(label="Añadir pieza", command=self.add_piece)
        file_menu.add_separator()
        file_menu.add_command(label="Salir", command=self.root.destroy)

    def create_draggable_rectangles(self):
        self.draggable_rectangles = [
            DraggableRectangle(self.canvas, 50, 50, 150, 150),
            DraggableRectangle(self.canvas, 200, 200, 300, 300)
        ]

    def add_piece(self):
        new_rectangle = DraggableRectangle(self.canvas)
        self.draggable_rectangles.append(new_rectangle)

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Archivos JSON", "*.json")])
        if file_path:
            with open(file_path, 'r') as file:
                content = json.load(file)
                print("Contenido del archivo JSON:")
                print(content)

    def save_file(self):
        parts_json = [rectangle.get_rect_info() for rectangle in self.draggable_rectangles]
        content = {"circuits": [{"name": "circuit", "parts": parts_json}]}
        with open("circuits.json", 'w') as file:
            json.dump(content, file, indent=4)
        print("Se ha creado el archivo JSON 'circuits.json'.")
