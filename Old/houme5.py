# 1
from math import *
a = int(input("Ведите длинну первой сторны: "))
b = int(input("Ведите длинну второй сторны: "))
c = int(input("Ведите значение угла в градусах: "))
print("Площадь треугольника: ", (a * b * 0.5 * sin(radians(c))))

# 2
from math import *


def distance(x1, y1, x2, y2):
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


x1 = float(input("Ведите x1: "))
y1 = float(input("Ведите y1: "))
x2 = float(input("Ведите x2: "))
y2 = float(input("Ведите y2: "))
print("Расстояние между точками", round(distance(x1, y1, x2, y2), 2))