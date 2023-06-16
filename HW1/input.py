def num_input_check(message, param=1):
    while True:
        try:
            mess = input(f'{message}: ')

            if param == 1:
                return int(mess)

            return float(mess)

        except ValueError:
            if param == 1:
                message = 'Ошибка ввода, введите целое число...'
            else:
                message = 'Ошибка ввода, введите число...'
            continue


def is_natural_num(number):
    if number >= 1 and number % 1 == 0:
        return True
    return False
