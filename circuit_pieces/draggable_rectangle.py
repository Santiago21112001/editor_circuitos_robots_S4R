from circuit_pieces.draggable_piece import DraggablePiece


class DraggableRectangle(DraggablePiece):

    def __init__(self, canvas, x1, y1, x2, y2):
        super().__init__(canvas)
        self.piece = self.canvas.create_rectangle(x1, y1, x2, y2, fill="black")
        self.bind_events()

    def get_piece_type(self):
        return "straight"
