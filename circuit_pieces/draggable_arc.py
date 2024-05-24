from circuit_pieces.draggable_piece import DraggablePiece


class DraggableArc(DraggablePiece):

    def __init__(self, canvas, x1, y1, dist, start=-90, extent=90):
        super().__init__(canvas)
        self.start = start
        self.extent = extent
        self.dist = dist
        self.piece = self.canvas.create_arc(x1, y1, x1+dist, y1+dist, width=self.width, style="arc", start=start,
                                            extent=extent)
        self.bind_events()

    def get_piece_type(self):
        return "turn1"

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
