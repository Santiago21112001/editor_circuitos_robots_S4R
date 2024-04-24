from circuit_pieces.draggable_piece import DraggablePiece


class DraggableArc(DraggablePiece):

    def __init__(self, canvas, x1, y1, x2, y2):
        super().__init__(canvas)
        self.start=-90
        self.extent=90
        self.width=50
        self.piece = self.canvas.create_arc(x1, y1, x2, y2, style="arc", start=-90, extent=90, outline="black",
                                            width=50)
        self.bind_events()

    def get_piece_type(self):
        return "turn1"

    def get_piece_info(self):
        x1, y1, x2, y2 = self.canvas.coords(self.piece)
        piece_info = {
            "type": self.get_piece_type(),
            "x1": x1,
            "y1": y1,
            "x2": x2,
            "y2": y2,
            "start": self.start,
            "extent": self.extent,
            "width": self.width
        }
        return piece_info
