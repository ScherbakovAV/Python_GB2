"""
Напишите программу, которая получает целое число и возвращает
его шестнадцатеричное строковое представление.
Функцию hex используйте для проверки своего результата.
"""

import input

SYSTEM = 16


def dec_to_hex(number: int):
    tmp_num: int = number
    new_num: str = ''

    while tmp_num != 0:
        mod = tmp_num % SYSTEM

        if 0 <= mod <= 9:
            new_num = str(mod) + new_num
        if mod == 10:
            new_num = 'a' + new_num
        if mod == 11:
            new_num = 'b' + new_num
        if mod == 12:
            new_num = 'c' + new_num
        if mod == 13:
            new_num = 'd' + new_num
        if mod == 14:
            new_num = 'e' + new_num
        if mod == 15:
            new_num = 'f' + new_num

        tmp_num //= SYSTEM

    new_num = '0x' + new_num

    return new_num


def check_hex(number_hex: str, number: int):
    if number_hex == hex(number):
        check_result = 'пройдена'

    else:
        check_result = 'результат ошибочен'

    return check_result


num = input.positive_num_input('Введите число для перевода из двоичной системы счисления в шестнадцатеричную', 2)
num_hex = dec_to_hex(num)
print(f'Это число в шестнадцатеричном представлении - {num_hex}')
print(f'Проверка встроенной функцией hex: {check_hex(num_hex, num)}')
