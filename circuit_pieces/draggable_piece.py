from abc import ABC, abstractmethod


class DraggablePiece(ABC):

    def __init__(self, circuit_editor):
        self.piece = None
        self.canvas = circuit_editor.canvas
        self.circuit_editor = circuit_editor
        self.width = 20
        self.start_x = 0
        self.start_y = 0
        self.scale = 0.2

    def bind_events(self):
        self.canvas.tag_bind(self.piece, "<ButtonPress-1>", self.__start_drag)
        self.canvas.tag_bind(self.piece, "<ButtonRelease-1>", self.__stop_drag)
        self.canvas.tag_bind(self.piece, "<B1-Motion>", self.__drag)

    def __start_drag(self, event):
        self.start_x = event.x
        self.start_y = event.y
        self.circuit_editor.set_selected_piece(self)

    def __stop_drag(self, event):
        self.start_x = 0
        self.start_y = 0

    def __drag(self, event):
        delta_x = event.x - self.start_x
        delta_y = event.y - self.start_y
        self.canvas.move(self.piece, delta_x, delta_y)
        self.start_x = event.x
        self.start_y = event.y

    def get_piece_info(self):
        x1, y1, x2, y2 = self.canvas.coords(self.piece)
        piece_info = {
            "type": self.get_piece_type(),
            "x1": x1,
            "y1": y1,
            "x2": x2,
            "y2": y2,
            "scale": self.scale
        }
        return piece_info

    @abstractmethod
    def get_piece_type(self):
        pass

    def rotate(self):
        pass

    def set_outline(self, new_color):
        self.canvas.itemconfig(self.piece, outline=new_color, fill=new_color)

    def get_id(self):
        return self.piece
