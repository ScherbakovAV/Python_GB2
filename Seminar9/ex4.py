"""Создайте декоратор с параметром.
Параметр - целое число, количество запусков декорируемой функции."""

from typing import Callable


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
def get_sum(number1: int, number2: int, *args, **kwargs) -> int:
    return number1 + number2


if __name__ == '__main__':
    print(get_sum(10, 4))
