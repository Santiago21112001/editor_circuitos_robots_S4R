from robot import Robot


class RobotsManager:
    def __init__(self):
        self.__robots = [Robot("mobile2")]

    def get_robots(self):
        return self.__robots.copy()

    def add_robot(self, name: str):
        self.__robots.append(Robot(name))

    def delete_robot(self, index: int) -> None:
        if len(self.__robots) <= 1:
            raise ValueError("Debe haber al menos 1 robot")
        self.__robots.pop(index)

    def update_robot_element(self, index: int, element_index: int, pin: str):
        self.__robots[index].update_element(element_index, pin)

    def add_light(self, index: int):
        self.__robots[index].add_light()

    def delete_light(self, index: int, light_index: int):
        self.__robots[index].delete_light(light_index)

    def to_json(self):
        robots = []
        for robot in self.__robots:
            robots.append(robot.get_data())
        return {"robots": robots}

    def load_json_data(self, data):
        robots = data["robots"]
        robot = Robot("a")
        robot.set_data(robots[0])
        self.__robots = [robot]
