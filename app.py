import tkinter as tk
from circuit_pieces.draggable_arc import DraggableArc
from circuit_pieces.draggable_rectangle import DraggableRectangle
from circuit_pieces.draggable_piece import DraggablePiece
from circuit_pieces.draggable_polygon import DraggablePolygon
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
        add_rectangle_button = tk.Button(self.root, text="Añadir recta horizontal", command=self.add_rectangle,
                                         bg="green", fg="white", padx=10, pady=5)
        add_rectangle_button.pack(side=tk.RIGHT, padx=10, pady=10)

        add_rectangle_y_button = tk.Button(self.root, text="Añadir recta vertical", command=self.add_rectangle_y,
                                           bg="green", fg="white", padx=10, pady=5)
        add_rectangle_y_button.pack(side=tk.RIGHT, padx=10, pady=10)

        add_arc_button = tk.Button(self.root, text="Añadir curva", command=self.add_arc, bg="green",
                                   fg="white", padx=10, pady=5)
        add_arc_button.pack(side=tk.RIGHT, padx=10, pady=10)

        add_polygon_button = tk.Button(self.root, text="Añadir cruce", command=self.add_polygon, bg="green",
                                       fg="white", padx=10, pady=5)
        add_polygon_button.pack(side=tk.RIGHT, padx=10, pady=10)

    def add_rectangle(self):
        new_piece: DraggablePiece = DraggableRectangle(self.canvas, 100, 200, 200, 250)
        self.draggable_pieces.append(new_piece)

    def add_rectangle_y(self):
        new_piece: DraggablePiece = DraggableRectangle(self.canvas, 100, 200, 150, 300)
        self.draggable_pieces.append(new_piece)

    def add_arc(self):
        new_piece: DraggablePiece = DraggableArc(self.canvas, 100, 200, 200, 300)
        self.draggable_pieces.append(new_piece)

    def add_polygon(self):
        w = 50
        x=200
        y=200
        points = [
            x, y,
            x+w, y,
            x+w, y-w,
            x+w*2, y-w,
            x+w*2, y,
            x+w*3, y,
            x+w*3, y+w,
            x+w*2, y+w,
            x+w*2, y+w*2,
            x+w, y+w*2,
            x+w, y+w,
            x, y+w
        ]
        new_piece: DraggablePiece = DraggablePolygon(self.canvas, points)
        self.draggable_pieces.append(new_piece)

    def open_file(self):
        self.file_manager.open_file()

    def save_file(self):
        parts_json = [rectangle.get_piece_info() for rectangle in self.draggable_pieces]
        content = {"circuits": [{"name": "circuit", "parts": parts_json}]}
        self.file_manager.save_file(content)
