"""Дорабатываем задачу 1.
Превратите внешнюю функцию в декоратор. Он должен проверять, входят ли переданные в функцию
угадайку числа в диапазоны [1, 100] и [1, 10].
Если не входят, вызывать функцию со случайными числами из диапазонов."""
from random import randint
from typing import Callable


def checking_params(func: Callable):
    min_num, max_num, min_count, max_count = 1, 100, 1, 10

    def wrapper(number: int, count: int, *args, **kwargs):
        if number > max_num or number < min_num:
            number = randint(min_num, max_num)

        if count > max_count or number < min_count:
            number = randint(min_count, max_count)

        res = func(number, count, *args, *kwargs)
        return res

    return wrapper


@checking_params
def guessing_numbers(number: int, counts: int) -> Callable[[], None]:
    def guessing_question():
        for count in range(1, counts + 1):
            inp_number = int(input(f'Угадайте число от 1 до 100.\n'
                                   f'Попытка № {count}: '))
            if inp_number == number:
                print('Вы победили!')
                return
            else:
                message = 'Загаданное число больше' if number > inp_number else 'Загаданное число меньше'
                print(f'Неверно! {message}\n')
        print(f'Вы не угадали! Загаданное число - {number}')

    return guessing_question


if __name__ == '__main__':
    result = guessing_numbers(125, 5)
    result()
