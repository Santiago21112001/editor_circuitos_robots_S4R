import unittest
import tkinter as tk
from circuit_pieces.arc import Arc


class MockApp:
    def __init__(self):
        self.canvas = tk.Canvas()

    def set_select_piece(self, piece):
        pass


class TestArc(unittest.TestCase):

    def setUp(self):
        self.app = MockApp()
        self.draggable_arc = Arc(self.app, 10, 10, 50)

    def test_initialization(self):
        self.assertEqual(self.draggable_arc.start, -90)
        self.assertEqual(self.draggable_arc.extent, 90)
        self.assertEqual(self.draggable_arc.dist, 50)
        self.assertIsNotNone(self.draggable_arc.piece)

    def test_get_piece_type(self):
        self.assertEqual(self.draggable_arc.get_piece_type(), 'turn')

    def test_get_piece_info(self):
        expected_info = {
            "type": "turn",
            "x1": 10.0,
            "y1": 10.0,
            "dist": 50,
            "start": self.draggable_arc.start,
            "extent": self.draggable_arc.extent,
            "width": 20,
            "scale": 0.2
        }
        self.assertEqual(self.draggable_arc.get_piece_info(), expected_info)

    def test_rotate(self):
        # Rotate to 0 degrees
        self.draggable_arc.rotate()
        self.assertEqual(self.draggable_arc.start, 0)
        self.assertEqual(self.draggable_arc.canvas.itemcget(self.draggable_arc.piece, 'start'), '0.0')

        # Rotate to 90 degrees
        self.draggable_arc.rotate()
        self.assertEqual(self.draggable_arc.start, 90)
        self.assertEqual(self.draggable_arc.canvas.itemcget(self.draggable_arc.piece, 'start'), '90.0')

        # Rotate to 180 degrees
        self.draggable_arc.rotate()
        self.assertEqual(self.draggable_arc.start, 180)
        self.assertEqual(self.draggable_arc.canvas.itemcget(self.draggable_arc.piece, 'start'), '180.0')

        # Rotate back to -90 degrees
        self.draggable_arc.rotate()
        self.assertEqual(self.draggable_arc.start, -90)
        self.assertEqual(self.draggable_arc.canvas.itemcget(self.draggable_arc.piece, 'start'), '270.0')


if __name__ == '__main__':
    unittest.main()
