"""Доработайте класс прямоугольник из прошлых семинаров.
- Добавьте возможность изменять длину и ширину
прямоугольника и встройте контроль недопустимых значений
(отрицательных).
- Используйте декораторы свойств."""


class Rectangle:
    def __init__(self, width: float, height: float = None):
        self._width = width
        if height is None:
            self._height = width
        else:
            self._height = height

    def calc_perimeter(self):
        return 2 * (self._width + self._height)

    def calc_area(self):
        return self._width * self._height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value > 0:
            self._width = value
        else:
            raise ValueError('Значение ширины должно быть > 0')

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value > 0:
            self._height = value
        else:
            raise ValueError('Значение ширины должно быть > 0')

    def __add__(self, other):
        perimeter = self.calc_perimeter() + other.calc_perimeter()
        width = self._width + other.width
        height = perimeter / 2 - width
        return Rectangle(width, height)

    def __sub__(self, other):
        width = abs(self._width - other.width)
        perimeter = abs(self.calc_perimeter() - other.calc_perimeter())
        height = perimeter / 2 - width
        return Rectangle(width, height)

    def __str__(self):
        return f'Периметр = {self.calc_perimeter()}, ширина = {self._width}, длина = {self._height}'

    def __eq__(self, other):
        return self.calc_area() == other.calc_area()

    def __lt__(self, other):
        return self.calc_area() < other.calc_area()

    def __le__(self, other):
        return self.calc_area() <= other.calc_area()


if __name__ == '__main__':
    rect = Rectangle(5, 20)
    print(f'{rect.width = }, {rect.height = }')
    rect.width, rect.height = 7, 10
    print(f'{rect.width = }, {rect.height = }')
    try:
        rect.width = 0
        print(f'{rect.width = }')
    except Exception as e:
        print(e)
    print(f'{rect.width = }, {rect.height = }')
