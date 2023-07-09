"""Задание №1
✔ Напишите функцию, которая заполняет файл
(добавляет в конец) случайными парами чисел.
✔ Первое число int, второе - float разделены вертикальной чертой.
✔ Минимальное число - -1000, максимальное - +1000.
✔ Количество строк и имя файла передаются как аргументы функции.
"""

from random import randint, uniform

MIN_NUM = -1000
MAX_NUM = 1000


def rand_numbers_in_file(num_str: int, file_name: str) -> None:
    with open(file_name, 'a', encoding='utf-8') as f:
        for _ in range(num_str):
            f.write(f'{randint(MIN_NUM, MAX_NUM)} | {uniform(MIN_NUM, MAX_NUM)}\n')


if __name__ == '__main__':
    rand_numbers_in_file(5, 'ex1_file.txt')
