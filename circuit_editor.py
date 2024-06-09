import tkinter as tk

from tkinter import messagebox

from circuit_pieces.draggable_arc import DraggableArc
from circuit_pieces.draggable_rectangle import DraggableRectangle
from circuit_pieces.draggable_piece import DraggablePiece
from circuit_pieces.draggable_polygon import DraggablePolygon
from editor import Editor


class CircuitEditor(Editor):
    def __init__(self, circuits_editor, circuit_data):
        # We pass circuits_editor.frame.master in order to avoid hiding CircuitEditor when we hide CircuitsEditor.
        super().__init__(circuits_editor.frame.master)
        self.circuits_editor = circuits_editor
        self.selected_piece = None

        self.canvas = tk.Canvas(self.frame, width=circuits_editor.width, height=circuits_editor.height - 110)
        self.canvas.pack()

        self.create_buttons(self.frame)
        self.draggable_pieces = []

        self.circuit_name = circuit_data["name"]
        self.append_file_pieces(circuit_data["parts"])

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

    def clear_canvas(self):
        self.draggable_pieces.clear()
        self.selected_piece = None
        self.canvas.delete("all")

    def rotate(self):
        if self.selected_piece is None:
            messagebox.showwarning("Advertencia", "Selecciona una pieza")
        else:
            self.selected_piece.rotate()

    def set_select_piece(self, piece: DraggablePiece):
        if self.selected_piece is not None:
            self.selected_piece.set_outline("black")
        self.selected_piece = piece
        piece.set_outline("red")

    def create_buttons(self, frame):
        button_frame = tk.Frame(frame)
        button_frame.pack(side=tk.BOTTOM, fill=tk.X)

        top_buttons = [
            ("Volver sin guardar", self.go_back, "blue"),
            ("Guardar y volver", self.save_and_go_back, "blue"),
        ]

        bottom_buttons = [
            ("Añadir recta horizontal", self.add_rectangle, "green"),
            ("Añadir recta vertical", self.add_rectangle_y, "green"),
            ("Añadir curva", self.add_arc, "green"),
            ("Añadir cruce", self.add_polygon, "green"),
            ("Rotar", self.rotate, "green"),
            ("Eliminar pieza elegida", self.delete_selected_piece, "green"),
            ("Limpiar lienzo", self.clear_canvas, "red")
        ]

        for i, (text, command, color) in enumerate(top_buttons):
            button = tk.Button(button_frame, text=text, command=command, bg=color, fg="white", padx=10, pady=5)
            button.grid(row=0, column=i, padx=5, pady=10)

        for i, (text, command, color) in enumerate(bottom_buttons):
            button = tk.Button(button_frame, text=text, command=command, bg=color, fg="white", padx=10, pady=5)
            button.grid(row=1, column=i, padx=5, pady=10)

    def go_back(self):
        title = "Volver sin guardar"
        message = "Se perderán los cambios si vuelve atrás. ¿Desea continuar?"
        if messagebox.askokcancel(title, message):
            self.frame.destroy()
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

    def append_file_pieces(self, parts):
        """Draws the circuit parts of the JSON file."""
        self.clear_canvas()
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

    def open_file(self):
        messagebox.showerror("Error", "Para abrir un archivo tienes que volver a la ventana anterior.")

    def save_file(self):
        messagebox.showerror("Error", "Para guardar un archivo tienes que volver a la ventana anterior.")
