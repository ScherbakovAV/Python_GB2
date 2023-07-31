"""Напишите для задачи 1 тесты unittest. Проверьте
следующие варианты:
- возврат строки без изменений
- возврат строки с преобразованием регистра без потери
символов
- возврат строки с удалением знаков пунктуации
- возврат строки с удалением букв других алфавитов
- возврат строки с учётом всех вышеперечисленных пунктов
(кроме п. 1)"""

from string import ascii_letters
import unittest


class TestSymbols(unittest.TestCase):
    def test_no_changed(self):
        self.assertEquals('my python', del_symbols('my python'))

    def test_lower_reg(self):
        self.assertEquals('my python', del_symbols('My Python'))

    def test_del_punctuations(self):
        self.assertEquals('my python', del_symbols('My Python!'))

    def test_another_lang(self):
        self.assertEquals('my', del_symbols('MyПайтон!'))

    def test_all_in_one(self):
        self.assertEquals('hello world   ', del_symbols('Hello world! Меня зовут Пайтон!'))


def del_symbols(text: str) -> str:
    text_formatted = ''.join(symbol for symbol in text if symbol in (set(ascii_letters + ' ')))
    return text_formatted.lower()


if __name__ == '__main__':
    unittest.main(verbosity=2)
