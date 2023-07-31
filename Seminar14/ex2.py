"""Напишите для задачи 1 тесты doctest. Проверьте
следующие варианты:
- возврат строки без изменений
- возврат строки с преобразованием регистра без потери
символов
- возврат строки с удалением знаков пунктуации
- возврат строки с удалением букв других алфавитов
- возврат строки с учётом всех вышеперечисленных пунктов
(кроме п. 1)"""

from string import ascii_letters
import doctest


def del_symbols(text: str) -> str:
    """
    >>> del_symbols('my python')
    'my python'
    >>> del_symbols('My Python')
    'my python'
    >>> del_symbols('My Python!')
    'my python'
    >>> del_symbols('MyПайтон!')
    'my'
    >>> del_symbols('Hello world! Меня зовут Пайтон!')
    'hello world   '
    """
    text_formatted = ''.join(symbol for symbol in text if symbol in (set(ascii_letters + ' ')))
    return text_formatted.lower()


if __name__ == '__main__':
    doctest.testmod(verbose=True)
