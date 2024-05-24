from circuit_pieces.draggable_piece import DraggablePiece


class DraggableRectangle(DraggablePiece):

    def __init__(self, canvas, x1, y1, orient, dist):
        super().__init__(canvas)
        self.orient = orient
        self.dist = dist
        if orient == "x":
            self.piece = self.canvas.create_rectangle(x1, y1, x1+dist, y1+self.width, fill="black")
        else:
            self.piece = self.canvas.create_rectangle(x1, y1, x1+self.width, y1+dist, fill="black")

        self.bind_events()

    def get_piece_type(self):
        return "straight"

    def get_piece_info(self):
        x1, y1, x2, y2 = self.canvas.coords(self.piece)
        piece_info = {
            "type": self.get_piece_type(),
            "x1": x1,
            "y1": y1,
            "orient": self.orient,
            "width": self.width,
            "dist": self.dist,
            "scale": self.scale
        }
        return piece_info
