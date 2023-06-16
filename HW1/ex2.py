""" Задание №1 (№9 семинара)
Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке."""


def is_digit(num):
    if 1 <= num <= 9:
        return True
    return False


def draw_table(row, col, start):

    for row_num in range(start, row + 1):
        col_num = col

        while col_num <= col + 3:
            result = col_num * row_num

            if is_digit(result) and is_digit(row_num) and is_digit(col_num):
                print(f'{col_num} X {row_num}  =  {result}', end='    ')
            if not is_digit(result) and is_digit(row_num) and is_digit(col_num):
                print(f'{col_num} X {row_num}  = {result}', end='    ')
            if not is_digit(result) and not is_digit(row_num) and is_digit(col_num):
                print(f'{col_num} X {row_num} = {result}', end='    ')

            col_num += 1

        print()
    print()


def mult_table():
    print('\n', ' ' * 20, 'ТАБЛИЦА УМНОЖЕНИЯ\n')
    start_col1 = 2
    start_col2 = 6
    start = 2
    rows = 10

    draw_table(rows, start_col1, start)
    draw_table(rows, start_col2, start)
