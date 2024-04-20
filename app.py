import tkinter as tk
from tkinter import filedialog
import json
from draggable_rectangle import DraggableRectangle
from file_manager import FileManager

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Editor de circuitos y robots")
        self.root.resizable(False, False)

        self.canvas = tk.Canvas(self.root, width=400, height=400)
        self.canvas.pack()

        self.menu_bar = self.create_menu()
        self.draggable_rectangles = []

        self.file_manager = FileManager()

        self.root.mainloop()

    def create_menu(self):
        menu_bar = tk.Menu(self.root)
        self.root.config(menu=menu_bar)

        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Archivo", menu=file_menu)

        file_menu.add_command(label="Abrir", command=self.open_file)
        file_menu.add_command(label="Guardar", command=self.save_file)
        file_menu.add_command(label="Añadir pieza", command=self.add_piece)
        file_menu.add_separator()
        file_menu.add_command(label="Salir", command=self.root.destroy)

        return menu_bar

    def add_piece(self):
        new_rectangle = DraggableRectangle(self.canvas, 100, 100, 100, 100)
        self.draggable_rectangles.append(new_rectangle)

    def open_file(self):
        self.file_manager.open_file()

    def save_file(self):
        parts_json = [rectangle.get_rect_info() for rectangle in self.draggable_rectangles]
        content = {"circuits": [{"name": "circuit", "parts": parts_json}]}
        self.file_manager.save_file(content)
