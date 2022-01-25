from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def print_info(self):
        pass

    @abstractmethod
    def print_sq(self):
        pass

    @abstractmethod
    def print_per(self):
        pass

    @abstractmethod
    def print_draw(self):
        pass


class Sqare(Shape):
    def __init__(self, name, a, color):
        self.name = name
        self.a = a
        self.color = color

    def print_sq(self):
        return self.a ** 2

    def print_per(self):
        return self.a * 4

    def print_draw(self):
        for i in range(self.a):
            print(self.a * '*')

    def print_info(self):
        print(
            f"=== {self.name}===\nСторона: {self.a}\nЦвет: {self.color}\nПлощадь: {self.print_sq()}\nПериметр: {self.print_per()}")
        self.print_draw()

class Rectangle(Shape):
    def __init__(self, name, a, b, color):
        self.name = name
        self.a = a
        self.b = b
        self.color = color

    def print_sq(self):
        return self.a * self.b

    def print_per(self):
        return (self.a + self.b) * 2

    def print_draw(self):
        for i in range(self.a):
            print(self.b * '*')

    def print_info(self):
        print(
            f"=== {self.name}===\nДлина: {self.a}\nШирина: {self.b}\nЦвет: {self.color}\nПлощадь: {self.print_sq()}\nПериметр: {self.print_per()}")
        self.print_draw()



class Triaangle(Shape):
    def __init__(self, name, a, b, c, color):
        self.name = name
        self.a = a
        self.b = b
        self.c = c
        self.color = color

    def print_sq(self):
        p = (self.a + self.b + self.c) / 2
        return round(((p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5), 2)

    def print_per(self):
        return self.a + self.b + self.c

    def print_draw(self):
        for i in range(self.c):
            print(' ' * (self.c - i - 1) + '*' * (i * 2 + 1))

    def print_info(self):
        print(
            f"=== {self.name}===\nСторона 1: {self.a}\nСторона 2: {self.b}\nСторона 3: {self.c}\nЦвет: {self.color}\nПлощадь: {self.print_sq()}\nПериметр: {self.print_per()}")
        self.print_draw()


sq = Sqare("Квадрат", 3, "red")
sq1 = Rectangle("Прямоугольник", 3, 7, "green")
sq2 = Triaangle("Треугольник", 11, 6, 6, "yellow")
for i in (sq, sq1, sq2):
    i.print_info()
    print()
