from draggable_piece import DraggablePiece


class DraggableRectangle(DraggablePiece):

    def create_canvas_part(self, canvas, x1, y1, x2, y2):
        canvas_part = canvas.create_rectangle(x1, y1, x2, y2, fill="black")
        return canvas_part

    def get_piece_type(self):
        return "straight_x"
