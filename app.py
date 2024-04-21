import tkinter as tk
from draggable_arc import DraggableArc
from draggable_rectangle import DraggableRectangle
from draggable_piece import DraggablePiece
from file_manager import FileManager


class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Editor de circuitos y robots")
        self.root.resizable(False, False)

        self.canvas = tk.Canvas(self.root, width=400, height=400)
        self.canvas.pack()
        self.menu_bar = self.create_menu()
        self.create_add_buttons()
        self.draggable_pieces = []

        self.file_manager = FileManager()

        self.root.mainloop()

    def create_menu(self):
        menu_bar = tk.Menu(self.root)
        self.root.config(menu=menu_bar)

        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Archivo", menu=file_menu)

        file_menu.add_command(label="Abrir", command=self.open_file)
        file_menu.add_command(label="Guardar", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Salir", command=self.root.destroy)

        return menu_bar

    def create_add_buttons(self):
        add_rectangle_button = tk.Button(self.root, text="Añadir recta", command=self.add_rectangle, bg="green",
                                         fg="white", padx=10, pady=5)
        add_rectangle_button.pack(side=tk.RIGHT, padx=10, pady=10)

        add_arc_button = tk.Button(self.root, text="Añadir curva", command=self.add_arc, bg="green",
                                   fg="white", padx=10, pady=5)
        add_arc_button.pack(side=tk.RIGHT, padx=10, pady=10)

    def add_rectangle(self):
        new_piece: DraggablePiece = DraggableRectangle(self.canvas, 100, 200, 200, 150)
        self.draggable_pieces.append(new_piece)

    def add_arc(self):
        new_piece: DraggablePiece = DraggableArc(self.canvas, 100, 200, 200, 300)
        self.draggable_pieces.append(new_piece)

    def open_file(self):
        self.file_manager.open_file()

    def save_file(self):
        parts_json = [rectangle.get_piece_info() for rectangle in self.draggable_pieces]
        content = {"circuits": [{"name": "circuit", "parts": parts_json}]}
        self.file_manager.save_file(content)
