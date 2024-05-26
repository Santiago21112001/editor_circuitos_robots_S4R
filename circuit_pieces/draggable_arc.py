from circuit_pieces.draggable_piece import DraggablePiece


class DraggableArc(DraggablePiece):

    def __init__(self, app, x1, y1, dist, start=-90, extent=90):
        """
        Creates the straight piece and draws it.

        Parameters:
        canvas (tkinter.Canvas): The canvas where the piece will be drawn.
        x1 (int): The x-coordinate of the first point.
        y1 (int): The y-coordinate of the first point.
        dist (int): The width and height of the invisible square which contains the arc.
        start (int, optional): The starting angle of the arc in degrees. Default is -90.
        extent (int, optional): The extent of the arc in degrees. Default is 90.
        """
        super().__init__(app)
        self.start = start
        self.extent = extent
        self.dist = dist
        self.piece = self.canvas.create_arc(x1, y1, x1+dist, y1+dist, width=self.width, style="arc", start=start,
                                            extent=extent)
        self.bind_events()

    def get_piece_type(self):
        return "turn"

    def get_piece_info(self):
        x1, y1, x2, y2 = self.canvas.coords(self.piece)
        piece_info = {
            "type": self.get_piece_type(),
            "x1": x1,
            "y1": y1,
            "dist": self.dist,
            "start": self.start,
            "extent": self.extent,
            "width": self.width,
            "scale": self.scale
        }
        return piece_info

    def rotate(self):
        new_start = self.start
        if self.start == -90:
            new_start = 0
        elif self.start == 0:
            new_start = 90
        elif self.start == 90:
            new_start = 180
        elif self.start == 180:
            new_start = -90
        self.start = new_start
        self.canvas.itemconfig(self.piece, start=new_start)
