"""Объедините функции из прошлых задач. Функцию угадайку задекорируйте:
* декораторами для сохранения параметров,
* декоратором контроля значений
* декоратором для многократного запуска.
Выберите верный порядок декораторов."""

import json
from os.path import exists
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


def logger(func: Callable):
    f_name = f'{func.__name__}.json'
    if exists(f_name):
        with open(f_name, 'r', encoding='utf-8') as file:
            data = json.load(file)
    else:
        data = []

    def wrapper(*args, **kwargs):
        json_dict = {'args': args, **kwargs}
        result = func(*args, **kwargs)
        json_dict['result'] = result
        data.append(json_dict)

        with open(f_name, 'w', encoding='utf-8') as f:
            json.dump(data, f)

        return result

    return wrapper


def counter(num: int = 1):
    def deco(func: Callable):
        results = []

        def wrapper(*args, **kwargs):
            for count in range(num):
                results.append(func(*args, **kwargs))
            return results

        return wrapper

    return deco


@counter(3)
@checking_params
@logger
def guessing_numbers(number: int, counts: int) -> bool:
    for count in range(1, counts + 1):
        inp_number = int(input(f'Угадайте число от 1 до 100.\n'
                               f'Попытка № {count}: '))
        if inp_number == number:
            print('Вы победили!')
            return True
        else:
            message = 'Загаданное число больше' if number > inp_number else 'Загаданное число меньше'
            print(f'Неверно! {message}\n')

    print(f'Вы не угадали! Загаданное число - {number}')
    return False


if __name__ == '__main__':
    print(guessing_numbers(40, 5))
