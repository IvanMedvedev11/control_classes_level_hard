class Rect:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def calculate_area(self):
        return self.a * self.b
class Square:
    def __init__(self, a):
        self.a = a
    def calculate_area(self):
        return self.a * self.a
rect = Rect(2, 3)
square = Square(2)
for figure in [rect, square]:
    print(f"Площадь: {figure.calculate_area()}")
