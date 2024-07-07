import unittest

from robot_model.robots_manager import RobotsManager


class TestRobotsManager(unittest.TestCase):

    def setUp(self):
        # The robots 'mobile2' and 'actuator' are added in __init__ of RobotsManager
        self.manager = RobotsManager()

    def test_add_robot_success(self):
        initial_count = len(self.manager.get_robots())
        new_robot_name = "mobile3"
        self.manager.add_robot(new_robot_name)
        robots = self.manager.get_robots()
        self.assertEqual(len(robots), initial_count + 1)
        self.assertEqual(robots[-1].get_name(), new_robot_name)

    def test_add_robot_duplicate_name(self):
        with self.assertRaises(ValueError) as context:
            self.manager.add_robot("mobile2")
        self.assertEqual(str(context.exception), "Ya hay un robot con el nombre 'mobile2'.")


if __name__ == '__main__':
    unittest.main()
