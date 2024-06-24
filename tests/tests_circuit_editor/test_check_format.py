import unittest

from circuit_parts_editor import check_format


class TestCheckFormat(unittest.TestCase):

    def test_valid_data(self):
        data = {
            "circuits": [
                {
                    "name": "circuit",
                    "parts": [
                        {
                            "type": "straight",
                            "x1": 100.0,
                            "y1": 100.0,
                            "orient": "x",
                            "width": 20,
                            "dist": 70,
                            "scale": 0.2
                        },
                        {
                            "type": "straight",
                            "x1": 100.0,
                            "y1": 100.0,
                            "orient": "y",
                            "width": 20,
                            "dist": 70,
                            "scale": 0.2
                        },
                        {
                            "type": "turn",
                            "x1": 142.0,
                            "y1": 238.0,
                            "dist": 70,
                            "start": -90,
                            "extent": 90,
                            "width": 20,
                            "scale": 0.2
                        },
                        {
                            "type": "polygon",
                            "x1": 179.0,
                            "y1": 164.0,
                            "width": 20,
                            "scale": 0.2
                        }
                    ]
                }
            ]
        }
        result = check_format(data)
        self.assertEqual(result, "")

    def test_missing_circuits(self):
        data = {
            "name": "example"
        }
        result = check_format(data)
        self.assertEqual(result, "Falta el campo 'circuits'.")

    def test_circuits_not_list(self):
        data = {
            "circuits": {}
        }
        result = check_format(data)
        self.assertEqual(result, "El campo 'circuits' debe ser una lista.")

    def test_invalid_part_type(self):
        data = {
            "circuits": [
                {
                    "name": "circuit",
                    "parts": [
                        {
                            "type": "invalid",
                            "x1": 100.0,
                            "y1": 100.0,
                            "width": 20,
                            "scale": 0.2
                        }
                    ]
                }
            ]
        }
        result = check_format(data)
        self.assertEqual(result, "Tipo de parte inválido: invalid")

    def test_missing_required_field(self):
        data = {
            "circuits": [
                {
                    "name": "circuit",
                    "parts": [
                        {
                            "type": "straight",
                            "x1": 100.0,
                            "y1": 100.0,
                            "orient": "x",
                            "width": 20,
                            "scale": 0.2
                        }
                    ]
                }
            ]
        }
        result = check_format(data)
        self.assertEqual(result, "Falta el campo 'dist' en una parte del tipo 'straight'")


if __name__ == '__main__':
    unittest.main()
