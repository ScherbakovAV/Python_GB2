"""
Напишите программу, которая получает целое число и возвращает
его шестнадцатеричное строковое представление.
Функцию hex используйте для проверки своего результата.
"""
def input_n():
    system: int = 0
    while system not in (2, 8):
        system = int(input(f'В какую систему счисления перевести число?\n'
                           f'Двоичная - введите "2"\n'
                           f'Восьмеричная - введите "8"'))

    return system


def dec_to_n(number: int, system: int) -> str:
    tmp_num: int = number
    new_num: str = ''

    while tmp_num != 0:
        mod: str = str(tmp_num % system)
        new_num = mod + new_num
        tmp_num //= system

    return new_num
