import unittest
from robot import Robot


class TestRobot(unittest.TestCase):

    def setUp(self):
        self.robot = Robot("test_robot")

    def test_set_element_duplicate_name(self):
        with self.assertRaises(ValueError):
            self.robot.set_element(1, "8")

    def test_set_element_success(self):
        self.robot.set_element(1, "1")
        elements = self.robot.get_elements()
        self.assertEqual(elements[1]["pin"], "1")

    def test_add_light_limit(self):
        # Add 2 lights in order to reach the limit
        self.robot.add_light()
        self.robot.add_light()

        # Trying adding a new light should raise an error
        with self.assertRaises(ValueError) as context:
            self.robot.add_light()
        self.assertEqual(str(context.exception), "No pueden haber más de 4 sensores de luz.")

    def test_add_light_success(self):
        # Add 1 light in order to have 1 ext light
        self.robot.add_light()

        initial_count = len(self.robot.get_elements())
        self.robot.add_light()
        elements = self.robot.get_elements()
        self.assertEqual(len(elements), initial_count + 1)
        self.assertTrue(any(e["name"] == "light 4" for e in elements))


if __name__ == '__main__':
    unittest.main()
