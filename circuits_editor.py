import tkinter as tk

from tkinter import messagebox

from circuit_pieces.draggable_arc import DraggableArc
from circuit_pieces.draggable_rectangle import DraggableRectangle
from circuit_pieces.draggable_piece import DraggablePiece
from circuit_pieces.draggable_polygon import DraggablePolygon
from editor import Editor


class CircuitsEditor(Editor):
    def __init__(self, container, width, height):
        super().__init__(container)
        self.file_content = None
        self.selected_piece = None

        self.canvas = tk.Canvas(self.frame, width=width, height=height - 100)
        self.canvas.pack()

        self.create_buttons()
        self.draggable_pieces = []
        self.file_content = {"circuits": [
            {
                "name": "circuit",
                "parts": []
            }]}

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

    def create_buttons(self):
        add_rectangle_button = tk.Button(self.frame, text="Añadir recta horizontal", command=self.add_rectangle,
                                         bg="green", fg="white", padx=10, pady=5)
        add_rectangle_button.pack(side=tk.RIGHT, padx=10, pady=10)

        add_rectangle_y_button = tk.Button(self.frame, text="Añadir recta vertical", command=self.add_rectangle_y,
                                           bg="green", fg="white", padx=10, pady=5)
        add_rectangle_y_button.pack(side=tk.RIGHT, padx=10, pady=10)

        add_arc_button = tk.Button(self.frame, text="Añadir curva", command=self.add_arc, bg="green",
                                   fg="white", padx=10, pady=5)
        add_arc_button.pack(side=tk.RIGHT, padx=10, pady=10)

        add_polygon_button = tk.Button(self.frame, text="Añadir cruce", command=self.add_polygon, bg="green",
                                       fg="white", padx=10, pady=5)
        add_polygon_button.pack(side=tk.RIGHT, padx=10, pady=10)

        clear_canvas_button = tk.Button(self.frame, text="Limpiar lienzo", command=self.clear_canvas, bg="green",
                                        fg="white", padx=10, pady=5)
        clear_canvas_button.pack(side=tk.RIGHT, padx=10, pady=10)

        rotate_button = tk.Button(self.frame, text="Rotar", command=self.rotate, bg="green",
                                  fg="white", padx=10, pady=5)
        rotate_button.pack(side=tk.RIGHT, padx=10, pady=10)

    def append_file_pieces(self, file_content):
        """Draws the circuit parts of the JSON file."""
        parts = file_content["circuits"][0]["parts"]
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
        file_content = self.file_manager.open_file()
        message = check_format(file_content)
        if message != "":
            messagebox.showerror("Archivo inválido", message)
            return
        self.file_content = file_content
        self.append_file_pieces(file_content)

    def save_file(self):
        if not self.draggable_pieces:
            messagebox.showerror("Circuito inválido", "El circuito debe tener al menos una pieza")
            return
        parts_json = [piece.get_piece_info() for piece in self.draggable_pieces]
        # Partes del primer circuito
        self.file_content["circuits"][0]["parts"] = parts_json
        file_path = "circuits.json"
        self.file_manager.save_file(self.file_content, file_path)
        messagebox.showinfo("Archivo guardado", "Se ha guardado el archivo 'circuits.json' en el directorio raíz de "
                                                "la aplicación")


def check_format(data):
    # Comprobar que data es un diccionario
    if not isinstance(data, dict):
        return "El contenido debe ser un diccionario."

    # Comprobar que tiene el campo 'circuits' y que es una lista
    if 'circuits' not in data:
        return "Falta el campo 'circuits'."
    if not isinstance(data['circuits'], list):
        return "El campo 'circuits' debe ser una lista."

    # Comprobar cada circuito
    for circuit in data['circuits']:
        if not isinstance(circuit, dict):
            return "Cada elemento de 'circuits' debe ser un diccionario."
        if 'name' not in circuit:
            return "Falta el campo 'name' en un circuito."
        if 'parts' not in circuit:
            return "Falta el campo 'parts' en un circuito."
        if not isinstance(circuit['parts'], list):
            return "El campo 'parts' debe ser una lista en un circuito."

        # Comprobar cada parte del circuito
        for part in circuit['parts']:
            if not isinstance(part, dict):
                return "Cada elemento de 'parts' debe ser un diccionario."
            if 'type' not in part:
                return "Falta el campo 'type' en una parte del circuito."
            if part['type'] not in ['straight', 'turn', 'polygon']:
                return f"Tipo de parte inválido: {part['type']}"

            # Inicializar required_fields
            required_fields = []
            # Comprobar campos específicos para cada tipo
            if part['type'] == 'straight':
                required_fields = ['x1', 'y1', 'orient', 'width', 'dist', 'scale']
            elif part['type'] == 'turn':
                required_fields = ['x1', 'y1', 'dist', 'start', 'extent', 'width', 'scale']
            elif part['type'] == 'polygon':
                required_fields = ['x1', 'y1', 'width', 'scale']

            for field in required_fields:
                if field not in part:
                    return f"Falta el campo '{field}' en una parte del tipo '{part['type']}'"

    return ""
