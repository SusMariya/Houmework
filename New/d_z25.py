import math


class Sphere:
    def __init__(self, radius=0, x=0, y=0, z=0):
        self.radius = radius
        self.x = x
        self.y = y
        self.z = z

    def set_radius(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius

    def get_volume(self):
        return (4 / 3) * math.pi * (self.radius ** 3)

    def get_square(self):
        return 4 * math.pi * self.radius ** 2

    def get_center(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def is_point_inside(self, x, y, z):
        if (self.x - x) ** 2 + (self.y - y) ** 2 + (self.z - z) ** 2 <= self.radius ** 2:
            return True
        return False


sf = Sphere()
sf.set_radius(0.6)
print("Радиус сферы: ", sf.get_radius())
print("Объем сферы: ", sf.get_volume())
print("Площадь внешней поверхности сферы: ", sf.get_square())
print("Координаты центра: ", sf.get_center(0, 0, 0))
print("Координаты точки в пространстве(0, -1.5, 0): ", sf.is_point_inside(0, -1.5, 0))
sf.set_radius(1.6)
print("Радиус сферы: ", sf.get_radius())
print("Координаты точки в пространстве(0, -1.5, 0): ", sf.is_point_inside(0, -1.5, 0))
