from abc import ABC, abstractmethod


class ThreeWayOrient(ABC):
    DOWN = "down"
    UP = "up"
    RIGHT = "right"
    LEFT = "left"

    @abstractmethod
    def get_points(self, x1: int, y1: int, width: int) -> list[int]:
        pass

    @abstractmethod
    def get_orient(self) -> str:
        pass


class OrientDown(ThreeWayOrient):

    def get_points(self, x1, y1, width):
        return [
            x1, y1,
            x1 + width * 3, y1,
            x1 + width * 3, y1 + width,
            x1 + width * 2, y1 + width,
            x1 + width * 2, y1 + width * 2,
            x1 + width, y1 + width * 2,
            x1 + width, y1 + width,
            x1, y1 + width
        ]

    def get_orient(self):
        return self.DOWN


class OrientUp(ThreeWayOrient):
    def get_points(self, x1, y1, width):
        return [
            x1, y1,
            x1 + width, y1,
            x1 + width, y1 - width,
            x1 + width * 2, y1 - width,
            x1 + width * 2, y1,
            x1 + width * 3, y1,
            x1 + width * 3, y1 + width,
            x1, y1 + width
        ]

    def get_orient(self):
        return self.UP


class OrientRight(ThreeWayOrient):
    def get_points(self, x1, y1, width):
        return [
            x1 + width, y1 - width,
            x1 + width * 2, y1 - width,
            x1 + width * 2, y1,
            x1 + width * 3, y1,
            x1 + width * 3, y1 + width,
            x1 + width * 2, y1 + width,
            x1 + width * 2, y1 + width * 2,
            x1 + width, y1 + width * 2
        ]

    def get_orient(self):
        return self.RIGHT


class OrientLeft(ThreeWayOrient):
    def get_points(self, x1, y1, width):
        return [
            x1, y1,
            x1 + width, y1,
            x1 + width, y1 - width,
            x1 + width * 2, y1 - width,
            x1 + width * 2, y1 + width * 2,
            x1 + width, y1 + width * 2,
            x1 + width, y1 + width,
            x1, y1 + width
        ]

    def get_orient(self):
        return self.LEFT
