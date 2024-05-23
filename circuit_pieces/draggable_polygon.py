from circuit_pieces.draggable_piece import DraggablePiece


class DraggablePolygon(DraggablePiece):

    def __init__(self, canvas, x, y):
        super().__init__(canvas)
        w = self.width
        points = [
            x, y,
            x + w, y,
            x + w, y - w,
            x + w * 2, y - w,
            x + w * 2, y,
            x + w * 3, y,
            x + w * 3, y + w,
            x + w * 2, y + w,
            x + w * 2, y + w * 2,
            x + w, y + w * 2,
            x + w, y + w,
            x, y + w
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
            "scale": 0.2
        }
        return piece_info
