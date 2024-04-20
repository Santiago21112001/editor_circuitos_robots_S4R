class DraggableRectangle:
    def __init__(self, canvas, x1, y1, x2, y2):
        self.canvas = canvas
        self.rect = canvas.create_rectangle(x1, y1, x2, y2, fill="black")
        self.canvas.tag_bind(self.rect, "<ButtonPress-1>", self.__start_drag)
        self.canvas.tag_bind(self.rect, "<ButtonRelease-1>", self.__stop_drag)
        self.canvas.tag_bind(self.rect, "<B1-Motion>", self.__drag)

        self.start_x = 0
        self.start_y = 0

    def __start_drag(self, event):
        self.start_x = event.x
        self.start_y = event.y

    def __stop_drag(self, event):
        self.start_x = 0
        self.start_y = 0

    def __drag(self, event):
        delta_x = event.x - self.start_x
        delta_y = event.y - self.start_y
        self.canvas.move(self.rect, delta_x, delta_y)
        self.start_x = event.x
        self.start_y = event.y

    def get_rect_info(self):
        x1, y1, x2, y2 = self.canvas.coords(self.rect)
        width = x2 - x1
        height = y2 - y1
        rect_info = {
            "x": x1,
            "y": y1,
            "width": width,
            "height": height
        }
        return rect_info
