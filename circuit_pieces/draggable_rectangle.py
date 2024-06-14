from circuit_pieces.draggable_piece import DraggablePiece


class DraggableRectangle(DraggablePiece):

    def __init__(self, circuit_editor, x1, y1, orient, dist):
        """
        Creates the straight piece and draws it.

        Parameters:
        canvas (tkinter.Canvas): The canvas where the piece will be drawn.
        x1 (int): The x-coordinate of the first point.
        y1 (int): The y-coordinate of the first point.
        orient (string): 'x' is horizontal, anything else is vertical.
        dist (int): the length of the horizontal line (orient 'x') or the vertical line (orient 'y').
        """
        super().__init__(circuit_editor)
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

    def rotate(self):
        x1, y1, x2, y2 = self.canvas.coords(self.piece)
        if self.orient == "x":
            self.orient = "y"
            x2 = x1 + self.width
            y2 = y1 + self.dist
        else:
            self.orient = "x"
            x2 = x1 + self.dist
            y2 = y1 + self.width
        self.canvas.coords(self.piece, x1, y1, x2, y2)
