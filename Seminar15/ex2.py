"""На семинаре про декораторы был создан логирующий
декоратор. Он сохранял аргументы функции и результат её
работы в файл.
Напишите аналогичный декоратор, но внутри используйте
модуль logging"""

import logging
from typing import Callable

logging.basicConfig(level=logging.INFO, filename='log2.log', encoding='utf-8')
log = logging.getLogger(__name__)


def logger(func: Callable):
    def wrapper(*args, **kwargs):
        info = {'args': args, **kwargs}
        result = func(*args, **kwargs)
        info['result'] = result
        log.info(info)

        return result

    return wrapper


@logger
def get_sum(number1: int, number2: int, *args, **kwargs) -> int:
    return number1 + number2


if __name__ == '__main__':
    summ = get_sum(10, 3, x=4)
    print(summ)
