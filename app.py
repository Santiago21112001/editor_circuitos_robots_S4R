import tkinter as tk
from tkinter import messagebox

from circuit_pieces.draggable_arc import DraggableArc
from circuit_pieces.draggable_rectangle import DraggableRectangle
from circuit_pieces.draggable_piece import DraggablePiece
from circuit_pieces.draggable_polygon import DraggablePolygon
from file_manager import FileManager


class App:
    def __init__(self):
        """
        Constructor for App.
        Opens the main window and reads the JSON file that is in the same directory.
        """
        self.selected_piece = None
        self.root = tk.Tk()
        self.root.title("Editor de circuitos y robots")
        self.root.resizable(False, False)

        self.canvas = tk.Canvas(self.root, width=1280, height=720)
        self.canvas.pack()
        self.menu_bar = self.create_menu()
        self.create_buttons()
        self.draggable_pieces = []

        self.file_manager = FileManager()
        self.file_content = self.file_manager.open_data_file()

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

    def create_buttons(self):
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

        clear_canvas_button = tk.Button(self.root, text="Limpiar lienzo", command=self.clear_canvas, bg="green",
                                        fg="white", padx=10, pady=5)
        clear_canvas_button.pack(side=tk.RIGHT, padx=10, pady=10)

        rotate_button = tk.Button(self.root, text="Rotar", command=self.rotate, bg="green",
                                  fg="white", padx=10, pady=5)
        rotate_button.pack(side=tk.RIGHT, padx=10, pady=10)

    def add_rectangle(self):
        dist = 70
        x1 = 100
        y1 = 100
        new_piece: DraggablePiece = DraggableRectangle(self, x1, y1, "x", dist)
        self.draggable_pieces.append(new_piece)

    def add_rectangle_y(self):
        dist = 70
        x1 = 100
        y1 = 100
        new_piece: DraggablePiece = DraggableRectangle(self, x1, y1, "y", dist)
        self.draggable_pieces.append(new_piece)

    def add_arc(self):
        dist = 70
        x1 = 100
        y1 = 100
        new_piece: DraggablePiece = DraggableArc(self, x1, y1, dist)
        self.draggable_pieces.append(new_piece)

    def add_polygon(self):
        x = 100
        y = 100
        new_piece: DraggablePiece = DraggablePolygon(self, x, y)
        self.draggable_pieces.append(new_piece)

    def open_file(self):
        file_content = self.file_manager.open_file()
        if file_content is None:
            return
        self.file_content = file_content
        self.append_file_pieces(file_content)

    def append_file_pieces(self, file_content):
        """Draws the circuit parts of the JSON file."""
        parts = file_content["circuits"][0]["parts"]
        self.draggable_pieces = []
        for part in parts:
            part_type = part['type']
            x1 = part['x1']
            y1 = part['y1']
            piece = None
            if part_type == 'turn':
                piece = DraggableArc(self, x1, y1, part['dist'], part['start'], part['extent'])
            elif part_type == 'polygon':
                piece = DraggablePolygon(self, x1, y1)
            elif part_type == 'straight':
                piece = DraggableRectangle(self, x1, y1, part['orient'], part['dist'])
            if piece is not None:
                self.draggable_pieces.append(piece)

    def save_file(self):
        parts_json = [piece.get_piece_info() for piece in self.draggable_pieces]
        # Partes del primer circuito
        self.file_content["circuits"][0]["parts"] = parts_json
        self.file_manager.save_file(self.file_content)

    def clear_canvas(self):
        self.draggable_pieces.clear()
        self.selected_piece = None
        self.canvas.delete("all")

    def set_select_piece(self, piece: DraggablePiece):
        self.selected_piece = piece
        print("Pieza seleccionada: " + str(piece.get_piece_info()))

    def rotate(self):
        if self.selected_piece is None:
            messagebox.showwarning("Advertencia", "Selecciona una pieza")
        else:
            self.selected_piece.rotate()
