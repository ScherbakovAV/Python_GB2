"""
Пользователь вводит строку текста. Вывести каждое слово с новой строки.
✔ Строки нумеруются начиная с единицы.
✔ Слова выводятся отсортированными согласно кодировке Unicode.
✔ Текст выравнивается по правому краю так, чтобы у самого длинного
слова был один пробел между ним и номером строки.
"""

inp = sorted(input('Введите предложение: ').split())

longest_word_len = 0

for el in inp:
    if len(el) > longest_word_len:
        longest_word_len = len(el)

for index, el in enumerate(inp, 1):
    print(f'{index}.{el:>{longest_word_len + 1}}')
