from math import pi


class Circle:
    def __init__(self, r):
        self.r = r

    def get_circle(self):
        return f"Длина окружности: ", 2 * pi * self.r

    def get_circle_square(self):
        return f"Площадь круга: ", pi * self.r ** 2

    def print_circle(self):
        print(f"Радиус: {self.r}")