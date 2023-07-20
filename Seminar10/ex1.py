'''Создайте класс окружность.
Класс должен принимать радиус окружности при создании
экземпляра.
У класса должно быть два метода, возвращающие длину
окружности и её площадь.'''

from math import pi


class Circle:
    def __init__(self, radius: float):
        self.r = radius


    def circle_lenght(self):
        return 2 * pi * self.r


    def circle_area(self):
        return pi * self.r ** 2 / 4


circle_test1 = Circle(1)
circle_test2 = Circle(4.5)

print(circle_test1.circle_lenght())
print(circle_test1.circle_area())
print(circle_test2.circle_lenght())
print(circle_test2.circle_area())
