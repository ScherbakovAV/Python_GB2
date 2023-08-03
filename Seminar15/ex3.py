"""Доработаем задачу 2.
Сохраняйте в лог файл раздельно:
- уровень логирования,
- дату события,
- имя функции (не декоратора),
- аргументы вызова,
- результат"""

import logging
from typing import Callable

logging.basicConfig(level=logging.INFO, filename='log2.log', encoding='utf-8', style='{',
                    format='Уровень: {levelname}, дата: {asctime}. {msg}')
log = logging.getLogger(__name__)


def logger(func: Callable):
    def wrapper(*args, **kwargs):
        input_params = {'args': args, **kwargs}
        result = func(*args, **kwargs)
        log.info(f'Функция {func.__name__}\n Аргументы: {input_params}\n Результаты: {result}')

        return result

    return wrapper


@logger
def get_sum(number1: int, number2: int, *args, **kwargs) -> int:
    return number1 + number2


if __name__ == '__main__':
    summ = get_sum(10, 3, x=4)
    print(summ)
