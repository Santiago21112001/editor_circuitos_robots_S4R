import unittest
import tkinter as tk
from circuit_pieces.draggable_rectangle import DraggableRectangle


class MockApp:
    def __init__(self):
        self.canvas = tk.Canvas()

    def set_select_piece(self, piece):
        pass


class TestDraggableRectangle(unittest.TestCase):

    def setUp(self):
        self.app = MockApp()
        self.draggable_rectangle = DraggableRectangle(self.app, 10, 10, 'x', 50)

    def test_initialization(self):
        self.assertEqual(self.draggable_rectangle.orient, 'x')
        self.assertEqual(self.draggable_rectangle.dist, 50)
        self.assertIsNotNone(self.draggable_rectangle.piece)

    def test_get_piece_type(self):
        self.assertEqual(self.draggable_rectangle.get_piece_type(), 'straight')

    def test_get_piece_info(self):
        expected_info = {
            "type": "straight",
            "x1": 10.0,
            "y1": 10.0,
            "orient": 'x',
            "width": 20,
            "dist": 50,
            "scale": 0.2
        }
        self.assertEqual(self.draggable_rectangle.get_piece_info(), expected_info)

    def test_rotate(self):
        # Rotate to vertical
        self.draggable_rectangle.rotate()
        self.assertEqual(self.draggable_rectangle.orient, 'y')
        x1, y1, x2, y2 = self.draggable_rectangle.canvas.coords(self.draggable_rectangle.piece)
        self.assertEqual((x1, y1, x2, y2), (10, 10, 30, 60))

        # Rotate back to horizontal
        self.draggable_rectangle.rotate()
        self.assertEqual(self.draggable_rectangle.orient, 'x')
        x1, y1, x2, y2 = self.draggable_rectangle.canvas.coords(self.draggable_rectangle.piece)
        self.assertEqual((x1, y1, x2, y2), (10, 10, 60, 30))


if __name__ == '__main__':
    unittest.main()
