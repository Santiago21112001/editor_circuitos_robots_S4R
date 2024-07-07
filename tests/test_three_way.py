import unittest
from unittest.mock import Mock, patch
from circuit_model.three_way import ThreeWay, ThreeWayOrient


class TestThreeWayRotate(unittest.TestCase):

    def setUp(self):
        self.canvas_mock = Mock()
        self.editor_mock = Mock()
        self.three_way = ThreeWay(self.editor_mock, 100, 100)

    def test_rotate_from_down_to_left(self):
        # Solved "TypeError: 'Mock' object is not subscriptable" by mocking the method ThreeWay.__get_first_point()
        with patch.object(self.three_way, '_ThreeWay__get_first_point', return_value=(100, 100)):
            self.three_way.rotate()
            self.assertEqual(self.three_way.orient.get_orient(), ThreeWayOrient.LEFT)


if __name__ == '__main__':
    unittest.main()
