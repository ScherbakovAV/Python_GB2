"""На семинарах по ООП был создан класс прямоугольник
хранящий длину и ширину, а также вычисляющую периметр,
площадь и позволяющий складывать и вычитать
прямоугольники беря за основу периметр.
Напишите 3-7 тестов unittest для данного класса."""

import unittest
from Seminar11.ex5 import Rectangle


class TestRectangles(unittest.TestCase):
    def setUp(self) -> None:
        self.rect1 = Rectangle(15, 20)
        self.rect2 = Rectangle(8, 8)
        self.square = Rectangle(8)

    def test_creates(self):
        self.assertEquals(Rectangle(15, 20), self.rect1)

    def test_perimeter(self):
        self.assertEquals(32, self.square.calc_perimeter())

    def test_square(self):
        self.assertEquals(300, self.rect1.calc_area())

    def test_eq_perimeters(self):
        self.assertEquals(self.rect2.calc_perimeter(), self.square.calc_perimeter())

    def test_not_eq_squares(self):
        self.assertNotEquals(self.rect1.calc_area(), self.rect2.calc_area())

    def test_sum(self):
        self.assertEquals(Rectangle(23, 28), self.rect1 + self.rect2)

    def test_sub(self):
        self.assertEquals(Rectangle(7, 12), self.rect2 - self.rect1)


if __name__ == '__main__':
    unittest.main(verbosity=2)
    # rect = Rectangle(5, 20)
    # square = Rectangle(8)
    #
    # print(rect + square)
    # print(rect - square)
    #
    # print()
    # print(f'{rect.calc_area() = }')
    # print(f'{square.calc_area() = }')
    # print(f'{rect == square = }')
    # print(f'{rect != square = }')
    # print(f'{rect < square = }')
    # print(f'{rect <= square = }')
    # print(f'{rect > square = }')
    # print(f'{rect >= square = }')
