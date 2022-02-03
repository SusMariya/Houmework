class Rectangle:
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def get_rect_perimeter(self):
        return f'Периметр: ', 2 * (self.w + self.h)

    def get_square(self):
        return self.w * self.h

    def print_rect(self):
        print(f"Стороны: {self.w}, {self.h}")