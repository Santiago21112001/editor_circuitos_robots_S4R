import unittest

from robots_editor import check_format


class TestCheckFormat(unittest.TestCase):

    def test_valid_data(self):
        data = {
            "robots": [
                {
                    "name": "mobile2",
                    "elements": [
                        {"name": "servo left", "pin": "8"},
                        {"name": "servo right", "pin": "9"},
                        {"name": "light 2", "pin": "2"},
                        {"name": "light 3", "pin": "3"},
                        {"name": "trig", "pin": "4"},
                        {"name": "echo", "pin": "5"}
                    ]
                }
            ]
        }
        result = check_format(data)
        self.assertEqual(result, "")

    def test_missing_robots(self):
        data = {
            "name": "example"
        }
        result = check_format(data)
        self.assertEqual(result, "Falta el campo 'robots'.")

    def test_robots_not_list(self):
        data = {
            "robots": {}
        }
        result = check_format(data)
        self.assertEqual(result, "El campo 'robots' debe ser una lista.")

    def test_robot_not_dict(self):
        data = {
            "robots": [
                "not_a_dict"
            ]
        }
        result = check_format(data)
        self.assertEqual(result, "Cada elemento de 'robots' debe ser un diccionario.")

    def test_missing_robot_name(self):
        data = {
            "robots": [
                {
                    "elements": [
                        {"name": "servo left", "pin": "8"}
                    ]
                }
            ]
        }
        result = check_format(data)
        self.assertEqual(result, "Falta el campo 'name' en un robot.")

    def test_missing_elements(self):
        data = {
            "robots": [
                {
                    "name": "mobile2"
                }
            ]
        }
        result = check_format(data)
        self.assertEqual(result, "Falta el campo 'elements' en un robot.")

    def test_elements_not_list(self):
        data = {
            "robots": [
                {
                    "name": "mobile2",
                    "elements": {}
                }
            ]
        }
        result = check_format(data)
        self.assertEqual(result, "El campo 'elements' debe ser una lista en un robot.")

    def test_element_not_dict(self):
        data = {
            "robots": [
                {
                    "name": "mobile2",
                    "elements": [
                        "not_a_dict"
                    ]
                }
            ]
        }
        result = check_format(data)
        self.assertEqual(result, "Cada elemento de 'elements' debe ser un diccionario.")

    def test_missing_element_name(self):
        data = {
            "robots": [
                {
                    "name": "mobile2",
                    "elements": [
                        {"pin": "8"}
                    ]
                }
            ]
        }
        result = check_format(data)
        self.assertEqual(result, "Falta el campo 'name' en un elemento.")

    def test_missing_element_pin(self):
        data = {
            "robots": [
                {
                    "name": "mobile2",
                    "elements": [
                        {"name": "servo left"}
                    ]
                }
            ]
        }
        result = check_format(data)
        self.assertEqual(result, "Falta el campo 'pin' en un elemento.")


if __name__ == '__main__':
    unittest.main()
