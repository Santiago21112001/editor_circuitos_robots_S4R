from robot import Robot


class RobotsManager:
    ACTUATOR_DATA = {
            "name": "actuator",
            "elements": [
                {
                    "name": "servo",
                    "pin": "8"
                },
                {
                    "name": "button joystick",
                    "pin": "9"
                },
                {
                    "name": "x joystick",
                    "pin": "A0"
                },
                {
                    "name": "y joystick",
                    "pin": "A1"
                },
                {
                    "name": "button left",
                    "pin": "6"
                },
                {
                    "name": "button right",
                    "pin": "7"
                }
            ]
        }

    ARDUINO_BOARD_DATA = {
            "name": "arduinoBoard",
            "elements": []
        }

    def __init__(self):
        self.__robots = [Robot("mobile2")]
        actuator = Robot("actuator")
        actuator.set_data(self.ACTUATOR_DATA)
        self.__robots.append(actuator)

    def get_robots(self):
        return self.__robots.copy()

    def add_robot(self, name: str):
        self.__robots.append(Robot(name))

    def delete_robot(self, index: int) -> None:
        if len(self.__robots) <= 1:
            raise ValueError("Debe haber al menos 1 robot")
        self.__robots.pop(index)

    def set_robot_name(self, index: int, name: str):
        if not name:
            raise ValueError("El nuevo nombre está vacío.")
        # Check that there is no robot with the new name.
        for robot in self.__robots:
            if robot.get_name() == name:
                raise ValueError("Ya hay un robot con ese nombre.")

        # Change the name of the selected robot.
        self.__robots[index].set_name(name)

    def set_robot_element(self, index: int, element_index: int, pin: str):
        self.__robots[index].set_element(element_index, pin)

    def add_light(self, index: int):
        self.__robots[index].add_light()

    def delete_light(self, index: int, light_index: int):
        self.__robots[index].delete_light(light_index)

    def to_json(self):
        robots = []
        for robot in self.__robots:
            robots.append(robot.get_data())
        robots.append(self.ARDUINO_BOARD_DATA)
        return {"robots": robots}

    def load_json_data(self, data):
        self.__robots.clear()
        robots_data = data["robots"]
        for robot_data in robots_data:
            if robot_data["name"] != self.ARDUINO_BOARD_DATA["name"]:
                robot = Robot("robot")
                robot.set_data(robot_data)
                self.__robots.append(robot)
