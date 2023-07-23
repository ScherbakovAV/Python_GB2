"""Напишите декоратор, который сохраняет в json файл параметры декорируемой функции
и возвращаемый результат. При повторном вызове файл должен расширяться, а не перезаписываться.
Каждый ключевой параметр сохраните как отдельный ключ json словаря.
Для декорирования напишите функцию, которая может принимать как позиционные, так и ключевые аргументы.
Имя файла должно совпадать с именем декорируемой функции."""

import json
from typing import Callable
from os.path import exists


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


@logger
def get_sum(number1: int, number2: int, *args, **kwargs) -> int:
    return number1 + number2


if __name__ == '__main__':
    summ = get_sum(-5, 5, x=2, y='bye', z=False)
    print(summ)
