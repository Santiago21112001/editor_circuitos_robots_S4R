from abc import ABC, abstractmethod


class DraggablePiece(ABC):

    def __init__(self, app):
        self.piece = None
        self.canvas = app.canvas
        self.app = app
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
        self.app.set_select_piece(self)

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
