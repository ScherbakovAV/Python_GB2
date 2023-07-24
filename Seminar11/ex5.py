"""Дорабатываем класс прямоугольник из прошлого семинара.
- Добавьте возможность сложения и вычитания.
- При этом должен создаваться новый экземпляр
прямоугольника.
- Складываем и вычитаем периметры, а не длину и ширину.
- При вычитании не допускайте отрицательных значений."""


class Rectangle:
    def __init__(self, width: float, height: float = None):
        self.width = width
        if height is None:
            self.height = width
        else:
            self.height = height

    def calc_perimeter(self):
        return 2 * (self.width + self.height)

    def calc_area(self):
        return self.width * self.height

    def __add__(self, other):
        perimeter = self.calc_perimeter() + other.calc_perimeter()
        width = self.width + other._width
        height = perimeter / 2 - width
        return Rectangle(width, height)

    def __sub__(self, other):
        width = abs(self.width - other._width)
        perimeter = abs(self.calc_perimeter() - other.calc_perimeter())
        height = perimeter / 2 - width
        return Rectangle(width, height)

    def __str__(self):
        return f'Периметр = {self.calc_perimeter()}, ширина = {self.width}, длина = {self.height}'

    def __eq__(self, other):
        return self.calc_area() == other.calc_area()

    def __lt__(self, other):
        return self.calc_area() < other.calc_area()

    def __le__(self, other):
        return self.calc_area() <= other.calc_area()


if __name__ == '__main__':
    rect = Rectangle(5, 20)
    square = Rectangle(8)

    print(rect + square)
    print(rect - square)

    print()
    print(f'{rect.calc_area() = }')
    print(f'{square.calc_area() = }')
    print(f'{rect == square = }')
    print(f'{rect != square = }')
    print(f'{rect < square = }')
    print(f'{rect <= square = }')
    print(f'{rect > square = }')
    print(f'{rect >= square = }')
