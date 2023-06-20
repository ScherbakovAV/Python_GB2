def positive_num_input(message):
    number = -1

    while number < 0:
        try:
            number = float(input(f'{message}: '))

        except ValueError:
            message = 'Ошибка ввода, введите положительное число...'

            continue

    return number
