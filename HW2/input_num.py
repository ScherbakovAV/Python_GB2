def positive_num_input(message, number_type=1):
    number = -1

    while number < 0:
        try:
            if number_type == 1:
                number = float(input(f'{message}: '))
            elif number_type == 2:
                number = int(input(f'{message}: '))

        except ValueError:
            if number_type == 1:
                message = 'Ошибка ввода, введите положительное число...'
            elif number_type == 2:
                message = 'Ошибка ввода, введите целое положительное число...'

            continue

    return number
