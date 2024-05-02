from circuit_pieces.draggable_piece import DraggablePiece


class DraggablePolygon(DraggablePiece):

    def __init__(self, canvas, points):
        super().__init__(canvas)
        self.piece = self.canvas.create_polygon(points, fill='black')
        self.bind_events()

    def get_piece_type(self):
        return "polygon"

    def get_piece_info(self):
        points = self.canvas.coords(self.piece)
        piece_info = {
            "type": self.get_piece_type(),
            "points": points
        }
        return piece_info
