"""Соберите пакет с играми из тех файлов, что уже были созданы в рамках курса"""

from HW1.tasks.ex5 import guessing_game, random_int_number
from HW9.scripts.ex6 import guessing_numbers
from Seminar6.ex6 import guesses_dict

if __name__ == '__main__':
    game = input('Выберите игру:\n'
                 '1 - Угадайка чисел версия 1 (ДЗ1)\n'
                 '2 - Угадайка загадок (семинар 6)\n'
                 '3 - Угадайка чисел версия 2 с декоратором (ДЗ9)')
    match game:
        case('1'):
            guessing_game(random_int_number())

        case ('2'):
            guesses = {'Зимой и летом одним цветом': ['елка', 'ёлка', 'ель', 'елочка' 'ёлочка', 'сосна'],
                       'Не лает, не кусает, а в дом не пускает': ['замок', 'замочек'],
                       'Сидит дед, во сто шуб одет': ['лук', 'луковица'],
                       'Висит груша нельзя скушать': ['лампа', 'лампочка']}
            guesses_dict(guesses)

        case('3'):
            print(guessing_numbers.__name__)
            print(guessing_numbers(40, 5))

