from circuit_pieces.draggable_piece import DraggablePiece


class DraggablePolygon(DraggablePiece):

    def __init__(self, circuit_editor, x1, y1):
        """
        Creates the 4-way intersection piece and draws it.

        Parameters:
        canvas (tkinter.Canvas): The canvas where the piece will be drawn.
        x1 (int): The x-coordinate of the first point of the intersection.
        y1 (int): The y-coordinate of the first point of the intersection.
        """
        super().__init__(circuit_editor)
        w = self.width  # Length of each individual line.
        points = [
            x1, y1,
            x1 + w, y1,
            x1 + w, y1 - w,
            x1 + w * 2, y1 - w,
            x1 + w * 2, y1,
            x1 + w * 3, y1,
            x1 + w * 3, y1 + w,
            x1 + w * 2, y1 + w,
            x1 + w * 2, y1 + w * 2,
            x1 + w, y1 + w * 2,
            x1 + w, y1 + w,
            x1, y1 + w
        ]
        self.piece = self.canvas.create_polygon(points, fill='black')
        self.bind_events()

    def get_piece_type(self):
        return "polygon"

    def get_piece_info(self):
        points = self.canvas.coords(self.piece)
        piece_info = {
            "type": self.get_piece_type(),
            "x1": points[0],
            "y1": points[1],
            "width": self.width,
            "scale": self.scale
        }
        return piece_info
