"""Добавьте в модуль с загадками функцию, которая принимает на вход строку (текст загадки)
и число (номер попытки, с которой она угадана).
Функция формирует словарь с информацией о результатах отгадывания.
Для хранения используйте защищённый словарь уровня модуля.
Отдельно напишите функцию, которая выводит результаты угадывания из защищённого словаря в удобном для чтения виде.
Для формирования результатов используйте генераторное выражение.
"""

"""Добавьте в модуль с загадками функцию, которая хранит словарь списков.
Ключ словаря - загадка, значение - список с отгадками.
Функция в цикле вызывает загадывающую функцию, чтобы передать ей все свои загадки.
"""

_result = {}


def guessing(text: str, variants: list[str], counts: int) -> int:
    print(f'Добрый день! Ваша загадка на сегодня:\n{text}')

    for count in range(1, counts + 1):
        answer = input(f'Попытка №{count}... Введите отгадку: ')
        if answer.lower() in variants:
            print('Вы угадали!!!')
            return count

    print(f'Вы не угадали за {counts} попыток... Позор!')
    return 0


def guesses_dict(g_dict: dict[str, list[str]], count: int = 3) -> None:
    for key, value in g_dict.items():
        res = guessing(key, value, count)
        result_score(key, res)
        print(f'\nCode {res}')

    printing_statistic()


def result_score(txt: str, count_num: int) -> None:
    _result.update({txt: count_num})


def printing_statistic():
    res = (f'Загадка {key} отгадана за {value} попыток' if value > 0
           else f'Загадка {key} не отгадана за все попытки'
           for key, value in _result.items())
    print('Статистика:\n')
    print('\n'.join(res))


if __name__ == '__main__':
    guesses = {'Зимой и летом одним цветом': ['елка', 'ёлка', 'ель', 'елочка' 'ёлочка', 'сосна'],
               'Не лает, не кусает, а в дом не пускает': ['замок', 'замочек'],
               'Сидит дед, во сто шуб одет': ['лук', 'луковица'],
               'Висит груша нельзя скушать': ['лампа', 'лампочка']}

    guesses_dict(guesses)
