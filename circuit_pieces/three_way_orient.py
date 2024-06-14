from abc import ABC, abstractmethod


class Orient(ABC):
    DOWN = "down"
    UP = "up"
    RIGHT = "right"
    LEFT = "left"

    @abstractmethod
    def get_points(self, x1: int, y1: int, w: int) -> list[int]:
        pass

    @abstractmethod
    def get_orient(self) -> str:
        pass


class OrientDown(Orient):

    def get_points(self, x1, y1, w):
        return [
            x1, y1,
            x1 + w * 3, y1,
            x1 + w * 3, y1 + w,
            x1 + w * 2, y1 + w,
            x1 + w * 2, y1 + w * 2,
            x1 + w, y1 + w * 2,
            x1 + w, y1 + w,
            x1, y1 + w
        ]

    def get_orient(self):
        return self.DOWN


class OrientUp(Orient):
    def get_points(self, x1, y1, w):
        return [
            x1, y1,
            x1 + w, y1,
            x1 + w, y1 - w,
            x1 + w * 2, y1 - w,
            x1 + w * 2, y1,
            x1 + w * 3, y1,
            x1 + w * 3, y1 + w,
            x1, y1 + w
        ]

    def get_orient(self):
        return self.UP


class OrientRight(Orient):
    def get_points(self, x1, y1, w):
        return [
            x1 + w, y1 - w,
            x1 + w * 2, y1 - w,
            x1 + w * 2, y1,
            x1 + w * 3, y1,
            x1 + w * 3, y1 + w,
            x1 + w * 2, y1 + w,
            x1 + w * 2, y1 + w * 2,
            x1 + w, y1 + w * 2
        ]

    def get_orient(self):
        return self.RIGHT


class OrientLeft(Orient):
    def get_points(self, x1, y1, w):
        return [
            x1, y1,
            x1 + w, y1,
            x1 + w, y1 - w,
            x1 + w * 2, y1 - w,
            x1 + w * 2, y1 + w * 2,
            x1 + w, y1 + w * 2,
            x1 + w, y1 + w,
            x1, y1 + w
        ]

    def get_orient(self):
        return self.LEFT
