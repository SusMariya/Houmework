
from math import pi
# import circle
from circle import Circle
# import rectangle
from rectangle import Rectangle


class Cylinder(Rectangle, Circle):
    def __init__(self, h, r, w=None):
        super().__init__(w, h)
        super().__init__(r)


    def get_circle_square(self):
        return f"Площадь круга: ", pi * self.r ** 2

    def get_volume(self):
        return f"Объем: ", pi * self.r ** 2 * self.h
