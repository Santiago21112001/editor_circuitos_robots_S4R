import unittest
import tkinter as tk
from circuit_model.arc import Arc


class MockApp:
    def __init__(self):
        self.canvas = tk.Canvas()

    def set_select_piece(self, piece):
        pass


class TestArc(unittest.TestCase):

    def setUp(self):
        self.app = MockApp()
        self.draggable_arc = Arc(self.app, 10, 10, 50)

    def test_rotate(self):
        self.draggable_arc.rotate()
        self.assertEqual(self.draggable_arc.start, 0)
        self.assertEqual(self.draggable_arc.canvas.itemcget(self.draggable_arc.piece, 'start'), '0.0')


if __name__ == '__main__':
    unittest.main()
