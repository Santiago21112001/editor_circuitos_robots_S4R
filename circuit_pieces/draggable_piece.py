from abc import ABC, abstractmethod


class DraggablePiece(ABC):

    def __init__(self, canvas):
        self.piece = None
        self.canvas = canvas
        self.start_x = 0
        self.start_y = 0

    def bind_events(self):
        self.canvas.tag_bind(self.piece, "<ButtonPress-1>", self.__start_drag)
        self.canvas.tag_bind(self.piece, "<ButtonRelease-1>", self.__stop_drag)
        self.canvas.tag_bind(self.piece, "<B1-Motion>", self.__drag)

    def __start_drag(self, event):
        self.start_x = event.x
        self.start_y = event.y

    def __stop_drag(self, event):
        self.start_x = 0
        self.start_y = 0
        x1, y1, x2, y2 = self.canvas.coords(self.piece)
        print(str(self.get_piece_type()) + " - x1:"+str(x1)+", y1:"+str(y1)+", x2:"+str(x2)+", y2:" + str(y2))

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
            "y2": y2
        }
        return piece_info

    @abstractmethod
    def get_piece_type(self):
        pass
