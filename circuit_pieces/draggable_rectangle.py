from circuit_pieces.draggable_piece import DraggablePiece


class DraggableRectangle(DraggablePiece):

    def __init__(self, canvas, x1, y1, orient, dist):
        super().__init__(canvas)

        if orient == "x":
            self.piece = self.canvas.create_rectangle(x1, y1, x1+dist, y1+self.width, fill="black")
        else:
            self.piece = self.canvas.create_rectangle(x1, y1, x1+self.width, y1+dist, fill="black")

        self.bind_events()

    def get_piece_type(self):
        return "straight"
