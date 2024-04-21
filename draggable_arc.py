from draggable_piece import DraggablePiece


class DraggableArc(DraggablePiece):

    def create_canvas_part(self, canvas, x1, y1, x2, y2):
        canvas_part = canvas.create_arc(x1, y1, x2, y2, style="arc", start=0, extent=90, outline="black", width=10)
        return canvas_part
