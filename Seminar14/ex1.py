"""Создайте функцию, которая удаляет из текста все символы
кроме букв латинского алфавита и пробелов.
Возвращается строка в нижнем регистре"""

from string import ascii_letters


def del_symbols(text: str) -> str:
    text_formatted = ''.join(symbol for symbol in text if symbol in (set(ascii_letters + ' ')))
    return text_formatted.lower()


if __name__ == '__main__':
    new_txt = 'Hello world! Меня зовут Пайтон!'
    print(del_symbols(new_txt))
