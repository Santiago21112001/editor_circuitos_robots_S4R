import tkinter as tk
from tkinter import messagebox

from circuit_pieces.arc import Arc
from circuit_pieces.draggable_piece import DraggablePiece
from circuit_pieces.four_way import FourWay
from circuit_pieces.rectangle import Rectangle
from circuit_pieces.three_way import ThreeWay


class CircuitPiecesEditor:

    NEW_PIECE_X = 100
    NEW_PIECE_Y = 100
    NEW_PIECE_DIST = 70

    def __init__(self, circuits_editor, circuit_data):
        # We pass circuits_editor.frame.master in order to avoid hiding CircuitEditor when we hide CircuitsEditor.
        container = circuits_editor.frame.master
        self.frame = tk.Frame(master=container)
        self.frame.pack(fill="both", expand=True)
        self.circuits_editor = circuits_editor
        self.selected_piece = None

        self.canvas = tk.Canvas(self.frame, width=circuits_editor.width, height=circuits_editor.height - 210)
        self.canvas.pack()

        self.create_buttons()
        self.draggable_pieces = []

        self.circuit_name = circuit_data["name"]
        self.load_file_pieces(circuit_data["parts"])

    def create_buttons(self):
        button_frame = tk.Frame(self.frame)
        button_frame.pack(side=tk.BOTTOM, fill=tk.X)

        top_buttons = [
            ("Volver sin guardar", self.go_back, "blue"),
            ("Guardar y volver", self.save_and_go_back, "blue"),
        ]

        mid_buttons = [
            ("Añadir recta horizontal", self.add_rectangle, "green"),
            ("Añadir curva", self.add_arc, "green"),
            ("Añadir cruce de 4 vías", self.add_four_way, "green"),
            ("Añadir cruce de 3 vías", self.add_three_way, "green")
        ]

        bottom_buttons = [
            ("Rotar", self.rotate_selected_piece, "green"),
            ("Eliminar pieza elegida", self.delete_selected_piece, "green"),
            ("Eliminar todas las piezas", self.delete_all_pieces, "red")
        ]

        for i, (text, command, color) in enumerate(top_buttons):
            button = tk.Button(button_frame, text=text, command=command, bg=color, fg="white", padx=10, pady=5)
            button.grid(row=0, column=i, padx=5, pady=10)

        for i, (text, command, color) in enumerate(mid_buttons):
            button = tk.Button(button_frame, text=text, command=command, bg=color, fg="white", padx=10, pady=5)
            button.grid(row=1, column=i, padx=5, pady=10)

        for i, (text, command, color) in enumerate(bottom_buttons):
            button = tk.Button(button_frame, text=text, command=command, bg=color, fg="white", padx=10, pady=5)
            button.grid(row=2, column=i, padx=5, pady=10)

    def add_rectangle(self):
        new_piece: DraggablePiece = Rectangle(self, self.NEW_PIECE_X, self.NEW_PIECE_Y, "x",
                                              self.NEW_PIECE_DIST)
        self.draggable_pieces.append(new_piece)
        self.set_selected_piece(new_piece)

    def add_arc(self):
        new_piece: DraggablePiece = Arc(self, self.NEW_PIECE_X, self.NEW_PIECE_Y, self.NEW_PIECE_DIST)
        self.draggable_pieces.append(new_piece)
        self.set_selected_piece(new_piece)

    def add_four_way(self):
        new_piece: DraggablePiece = FourWay(self, self.NEW_PIECE_X, self.NEW_PIECE_Y)
        self.draggable_pieces.append(new_piece)
        self.set_selected_piece(new_piece)

    def add_three_way(self):
        new_piece: DraggablePiece = ThreeWay(self, self.NEW_PIECE_X, self.NEW_PIECE_Y)
        self.draggable_pieces.append(new_piece)
        self.set_selected_piece(new_piece)

    def delete_all_pieces(self):
        self.draggable_pieces.clear()
        self.selected_piece = None
        self.canvas.delete("all")

    def rotate_selected_piece(self):
        if self.selected_piece is None:
            messagebox.showwarning("Advertencia", "Selecciona una pieza")
        else:
            self.selected_piece.rotate()

    def set_selected_piece(self, piece: DraggablePiece):
        if self.selected_piece is not None:
            self.selected_piece.set_outline("black")
        self.selected_piece = piece
        piece.set_outline("red")

    def go_back(self):
        title = "Volver sin guardar"
        message = "Se perderán los cambios si vuelve atrás. ¿Desea continuar?"
        if messagebox.askokcancel(title, message):
            self.circuits_editor.open_this()

    def save_and_go_back(self):
        if not self.draggable_pieces:
            messagebox.showerror("Circuito inválido", "El circuito debe tener al menos una pieza")
            return
        parts_json = [piece.get_piece_info() for piece in self.draggable_pieces]
        self.frame.destroy()
        circuit_data = {"name": self.circuit_name, "parts": parts_json}
        self.circuits_editor.open_this(circuit_data)

    def delete_selected_piece(self):
        if self.selected_piece:
            self.draggable_pieces.remove(self.selected_piece)
            self.canvas.delete(self.selected_piece.get_id())
            self.selected_piece = None

    def load_file_pieces(self, file_pieces):
        """Draws the circuit parts of the JSON file."""
        self.delete_all_pieces()
        for part in file_pieces:
            part_type = part['type']
            x1 = part['x1']
            y1 = part['y1']
            piece = None
            if part_type == 'turn':
                piece = Arc(self, x1, y1, part['dist'], part['start'], part['extent'])
            elif part_type == 'four-way':
                piece = FourWay(self, x1, y1)
            elif part_type == 'straight':
                piece = Rectangle(self, x1, y1, part['orient'], part['dist'])
            elif part_type == 'three-way':
                piece = ThreeWay(self, x1, y1, part['orient'])
            if piece is not None:
                self.draggable_pieces.append(piece)

    def open_file(self):
        messagebox.showerror("Error", "Para abrir un archivo tienes que volver a la ventana anterior.")

    def save_file(self):
        messagebox.showerror("Error", "Para guardar un archivo tienes que volver a la ventana anterior.")
