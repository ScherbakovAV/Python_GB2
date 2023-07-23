'''Создайте класс прямоугольник.
Класс должен принимать длину и ширину при создании
экземпляра.
У класса должно быть два метода, возвращающие периметр
и площадь.
Если при создании экземпляра передаётся только одна
сторона, считаем что у нас квадрат.'''


class Rectangle:
    def __init__(self, a: int, b: int = None):
        self.side_a = a
        if b is None:
            self.side_b = a
        else:
            self.side_b = b


    def perimeter(self):
        return 2 * (self.side_a + self.side_b)


    def area(self):
        return self.side_a * self.side_b


rect = Rectangle(3, 5)
square = Rectangle(4)

print(f'P(rect) = {rect.perimeter()}')
print(f'S(rect) = {rect.area()}')
print(f'P(square) = {square.perimeter()}')
print(f'S(square) = {square.area()}')
