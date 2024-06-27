from circuit_pieces.draggable_piece import DraggablePiece
from circuit_pieces.three_way_orient import ThreeWayOrient, OrientDown, OrientUp, OrientLeft, OrientRight


class ThreeWay(DraggablePiece):

    def __init__(self, circuit_parts_editor, x1, y1, orient=ThreeWayOrient.DOWN):
        """
        Creates the 3-way intersection piece and draws it.

        Parameters:
        canvas (tkinter.Canvas): The canvas where the piece will be drawn.
        x1 (int): The x-coordinate of the first point of the intersection.
        y1 (int): The y-coordinate of the first point of the intersection.
        """
        super().__init__(circuit_parts_editor)
        w = self.width  # Length of each individual line.
        if orient == ThreeWayOrient.UP:
            self.orient = OrientUp()
        elif orient == ThreeWayOrient.RIGHT:
            self.orient = OrientRight()
        elif orient == ThreeWayOrient.LEFT:
            self.orient = OrientLeft()
        else:
            self.orient = OrientDown()
        points = self.orient.get_points(x1, y1, w)
        self.piece = self.canvas.create_polygon(points, fill='black')
        self.bind_events()

    def rotate(self):
        old_orient = self.orient.get_orient()
        if old_orient == ThreeWayOrient.UP:
            self.orient = OrientRight()
        elif old_orient == ThreeWayOrient.RIGHT:
            self.orient = OrientDown()
        elif old_orient == ThreeWayOrient.DOWN:
            self.orient = OrientLeft()
        elif old_orient == OrientLeft.LEFT:
            self.orient = OrientUp()

        x1, y1 = self.__get_first_point()

        new_points = self.orient.get_points(x1, y1, self.width)
        self.canvas.coords(self.piece, *new_points)

    def __get_first_point(self):
        points = self.canvas.coords(self.piece)
        x1 = points[0]
        y1 = points[1]
        w = self.width
        if self.orient.get_orient() == ThreeWayOrient.RIGHT:
            # Make the first point the same as the other orients
            x1 -= w
            y1 += w
        return x1, y1

    def get_piece_type(self):
        return "three-way"

    def get_piece_info(self):
        x1, y1 = self.__get_first_point()

        piece_info = {
            "type": self.get_piece_type(),
            "orient": self.orient.get_orient(),
            "x1": x1,
            "y1": y1,
            "width": self.width,
            "scale": self.scale
        }
        return piece_info
