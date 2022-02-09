class Rectangle:
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def get_rect_perimeter(self):
        res = 2 * (self.w + self.h)
        print(f'Периметр: , {res}')
        return res

    def get_rect_aria(self):
        res = self.w * self.h
        print(f'Площадь: {res}')
        return res

    def print_rect(self):
        print(f"Стороны: {self.w}, {self.h}")