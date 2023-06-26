"""Задание №2
✔ Напишите функцию, которая принимает строку текста.
✔ Сформируйте список с уникальными кодами Unicode каждого
символа введённой строки отсортированный по убыванию"""


def sort_unicode(text: str) -> list[int]:
    symbol_set = set()
    for symbol in text:
        symbol_set.add(ord(symbol))

    return sorted(symbol_set, reverse=True)


if __name__ == '__main__':
    txt = input('Enter txt:  ')
    print(sort_unicode(txt))
