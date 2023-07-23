"""Создайте функцию-замыкание, которая запрашивает два целых числа:
 * от 1 до 100 для загадывания,
 * от 1 до 10 для количества попыток.
Функция возвращает функцию, которая через консоль просит
угадать загаданное число за указанное число попыток.  """

from typing import Callable


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
    result = guessing_numbers(25, 5)
    result()
