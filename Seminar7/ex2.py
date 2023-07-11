"""Задание №2
✔ Напишите функцию, которая генерирует
псевдоимена.
✔ Имя должно начинаться с заглавной буквы,
состоять из 4-7 букв, среди которых
обязательно должны быть гласные.
✔ Полученные имена сохраните в файл."""

from random import randint, choice

__all__ = ['pseudo_names_in_file']

LETTERS_VOWS = 'aeioquy'
LETTERS_CONS = 'bcdfghjklmnprstxz'
NAME_LENGTH_MIN = 4
NAME_LENGTH_MAX = 7


def pseudo_names_in_file(num_names: int, file_name: str) -> None:
    with open(file_name, 'a', encoding='utf-8') as f:
        for _ in range(num_names):
            name = ''.join(choice(LETTERS_VOWS) if i in (1, 4, 6) else choice(LETTERS_CONS)
                           for i in range(randint(NAME_LENGTH_MIN, NAME_LENGTH_MAX)))

            f.write(name.capitalize() + '\n')


if __name__ == '__main__':
    pseudo_names_in_file(7, 'ex2_file.txt')
