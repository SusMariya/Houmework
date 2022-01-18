from abc import ABC, abstractmethod
import math


class Root(ABC):
    @abstractmethod
    def calk_root(self, *args):
        pass


class LinearEquation(Root):
    def calk_root(self, a, b):
        if a != 0:
            x = -b / a
            print(f"The root of '3x+7=0' are:{round(x, 2)}")
        elif a == 0 and b != 0:
            print("No roots")
        elif a == 0 and b == 0:
            print("Roots")


class QuadEquation(Root):
    def calk_root(self, a, b, c):
        d = b ** 2 - 4 * a * c
        if d > 0:
            x1 = (-b - math.sqrt(d) / (a * 2))
            x2 = (-b + math.sqrt(d) / (a * 2))
            print(f"The root of '1x^2-2x-3=0' are: {x1}, {x2}")
        elif d == 0:
            x = -b / (a * 2)
            print(f"Root = {x}")
        else:
            print("No roots")


root1 = LinearEquation()
root1.calk_root(3, 7)
root2 = QuadEquation()
root2.calk_root(1, 2, -3)