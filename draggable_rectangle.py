from tkinter import Canvas


class DraggableRectangle:
    def __init__(self, widget):
        self.widget = widget
        self.canvas = Canvas(self.widget)
        self.canvas.pack()
        self.__crear_draggable()

    def toJSON(self):
        return {
            "type": "straight",
            "orient": "x",
            "x": self.x,
            "y": self.y,
            "dist": self.width,
            "anchor next": "mid",
            "save anchors": ""
        }

    def __crear_draggable(self):
        self.x = 20
        self.y = 20
        self.width = 100
        height = 30
        color = "black"
        self.canvas.create_rectangle(
            self.x, self.y, self.x + self.width, self.y + height, fill=color)
        self.__make_draggable(self.canvas)

    def __make_draggable(self, widget):
        widget.bind("<Button-1>", self.__set_drag_start_position)
        widget.bind("<B1-Motion>", self.__update_position)

    def __set_drag_start_position(self, event):
        widget = event.widget
        widget._drag_start_x = event.x
        widget._drag_start_y = event.y

    def __update_position(self, event):
        widget = event.widget
        self.x = widget.winfo_x() - widget._drag_start_x + event.x
        self.y = widget.winfo_y() - widget._drag_start_y + event.y
        widget.place(x=self.x, y=self.y)
