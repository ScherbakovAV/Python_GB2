""" Задание №1 (№8 семинара)
Нарисовать в консоли ёлку спросив у пользователя количество рядов."""

from input import num_input_check as num_input
from input import is_natural_num as is_natural


def print_tree(start, stop, rows):
    for i in range(start, stop):
        print(' ' * (rows - 1), '*' * i, '*' * (i - 1), sep='')
        rows -= 1
    print()


def draw_tree(text):
    tree_rows = num_input(text)

    if is_natural(tree_rows) and tree_rows < 51:
        start = 1
        end = tree_rows + 1
        print_tree(start, end, tree_rows)

    elif tree_rows > 30:
        draw_tree('Число слишком большое, введите число от 1 до 50')

    else:
        draw_tree('Вы ввели число меньше 1, введите положительное число')
