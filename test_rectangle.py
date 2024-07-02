import unittest
import tkinter as tk
from circuit_pieces.rectangle import Rectangle


class MockApp:
    def __init__(self):
        self.canvas = tk.Canvas()

    def set_select_piece(self, piece):
        pass


class TestRectangle(unittest.TestCase):

    def setUp(self):
        self.app = MockApp()
        self.draggable_rectangle = Rectangle(self.app, 10, 10, 'x', 50)

    def test_rotate(self):
        self.draggable_rectangle.rotate()
        self.assertEqual(self.draggable_rectangle.orient, 'y')
        x1, y1, x2, y2 = self.draggable_rectangle.canvas.coords(self.draggable_rectangle.piece)
        self.assertEqual((x1, y1, x2, y2), (10, 10, 30, 60))


if __name__ == '__main__':
    unittest.main()
