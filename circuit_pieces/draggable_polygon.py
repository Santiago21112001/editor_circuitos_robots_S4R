from circuit_pieces.draggable_piece import DraggablePiece


class DraggablePolygon(DraggablePiece):

    def __init__(self, canvas, points):
        super().__init__(canvas)
        self.piece = self.canvas.create_polygon(points, fill='black')
        self.bind_events()

    def get_piece_type(self):
        return "turn1"
