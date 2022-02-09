
from math import pi
# import circle
from  d_z35.shape import circle
# import rectangle
from d_z35.shape import rectangle


class Cylinder(rectangle.Rectangle, circle.Circle):
    def __init__(self, r, h):
        circle.Circle.__init__(self, r)
        rectangle.Rectangle.__init__(self, self.get_circle_circumference(), h)


    # def get_circle_square(self):
    #     res = pi * self.r ** 2
    #     print(f"Площадь круга: , {res}")
    #     return res

    def get_volume(self):
        res = pi * self.r ** 2 * self.h
        print(f"Объем: , {round(res, 2)}")
        return res

    def print_circle(self):
        print(f'Основание : {self.r}, высота: {self.h}')
