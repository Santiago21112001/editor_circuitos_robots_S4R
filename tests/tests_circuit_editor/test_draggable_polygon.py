import unittest
import tkinter as tk
from circuit_pieces.draggable_four_way import DraggableFourWay


class MockApp:
    def __init__(self):
        self.canvas = tk.Canvas()

    def set_select_piece(self, piece):
        pass


class TestDraggablePolygon(unittest.TestCase):

    def setUp(self):
        self.app = MockApp()
        self.draggable_polygon = DraggableFourWay(self.app, 10, 10)

    def test_initialization(self):
        self.assertEqual(self.draggable_polygon.width, 20)
        self.assertEqual(self.draggable_polygon.scale, 0.2)
        self.assertIsNotNone(self.draggable_polygon.piece)

    def test_get_piece_type(self):
        self.assertEqual(self.draggable_polygon.get_piece_type(), 'polygon')

    def test_get_piece_info(self):
        expected_info = {
            "type": "polygon",
            "x1": 10.0,
            "y1": 10.0,
            "width": 20,
            "scale": 0.2
        }
        self.assertEqual(self.draggable_polygon.get_piece_info(), expected_info)

    def test_set_outline(self):
        new_color = 'red'
        self.draggable_polygon.set_outline(new_color)
        self.assertEqual(self.draggable_polygon.canvas.itemcget(self.draggable_polygon.piece, 'outline'), new_color)
        self.assertEqual(self.draggable_polygon.canvas.itemcget(self.draggable_polygon.piece, 'fill'), new_color)


if __name__ == '__main__':
    unittest.main()
