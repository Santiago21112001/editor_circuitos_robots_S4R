import unittest
from files_manager.files_manager import FilesManager


class TestFilesManager(unittest.TestCase):

    def setUp(self):
        self.manager = FilesManager()

    def test_check_robots_data_format_valid(self):
        valid_data = {
            'robots': [
                {
                    'name': 'robot1',
                    'elements': [
                        {'name': 'element1', 'pin': '1'},
                        {'name': 'element2', 'pin': '2'}
                    ]
                },
                {
                    'name': 'robot2',
                    'elements': [
                        {'name': 'element1', 'pin': '3'}
                    ]
                }
            ]
        }
        self.assertIsNone(self.manager.check_robots_data_format(valid_data))

    def test_check_robots_data_format_invalid(self):
        invalid_data = {
            'circuits': [
                {
                    'name': 'robot1',
                    'elements': [
                        {'name': 'element1', 'pin': '1'},
                        {'name': 'element2', 'pin': '2'}
                    ]
                }
            ]
        }
        with self.assertRaises(ValueError):
            self.manager.check_robots_data_format(invalid_data)

    def test_check_circuits_data_format_valid(self):
        valid_data = {
            'circuits': [
                {
                    'name': 'circuit1',
                    'parts': [
                        {'type': 'straight', 'x1': 0, 'y1': 0, 'orient': 'horizontal', 'width': 10, 'dist': 20,
                         'scale': 1.0}
                    ]
                },
                {
                    'name': 'circuit2',
                    'parts': [
                        {'type': 'turn', 'x1': 10, 'y1': 10, 'dist': 30, 'start': 45, 'extent': 90, 'width': 8,
                         'scale': 1.0}
                    ]
                }
            ]
        }
        self.assertIsNone(self.manager.check_circuits_data_format(valid_data))

    def test_check_circuits_data_format_invalid(self):
        invalid_data = {
            'robots': [
                {
                    'name': 'circuit1',
                    'parts': [
                        {'type': 'straight', 'x1': 0, 'y1': 0, 'orient': 'horizontal', 'width': 10, 'dist': 20,
                         'scale': 1.0}
                    ]
                }
            ]
        }
        with self.assertRaises(ValueError):
            self.manager.check_circuits_data_format(invalid_data)


if __name__ == '__main__':
    unittest.main()
