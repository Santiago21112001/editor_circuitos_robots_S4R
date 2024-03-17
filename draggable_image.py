import tkinter as tk
from tkinter import Canvas


class DraggableImage:
    def __init__(self, widget, filename):
        self.widget = widget
        self.canvas = Canvas(self.widget)
        self.canvas.pack()
        self.img = tk.PhotoImage(file=filename)
        self.crear_draggable()

    def crear_draggable(self):
        self.canvas.create_image(20, 20, anchor='nw', image=self.img)
        make_draggable(self.canvas)


def make_draggable(widget):
    widget.bind("<Button-1>", on_drag_start)
    widget.bind("<B1-Motion>", on_drag_motion)


def on_drag_start(event):
    widget = event.widget
    widget._drag_start_x = event.x
    widget._drag_start_y = event.y


def on_drag_motion(event):
    widget = event.widget
    x = widget.winfo_x() - widget._drag_start_x + event.x
    y = widget.winfo_y() - widget._drag_start_y + event.y
    widget.place(x=x, y=y)
