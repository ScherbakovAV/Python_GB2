result = ''
NUM_ONE = 1
NUM_TEN = 10
NUM_HUNDRED = 100
NUM_THOUSAND = 1000
SQUARE = 2

while True:
    num = int(input('Введите число от 1 до 999...'))

    if NUM_ONE <= num < NUM_TEN:
        result = f'Это цифра, {num ** SQUARE}'
        break
    elif NUM_TEN <= num < NUM_HUNDRED:
        tmp1 = num // NUM_TEN
        tmp2 = num % NUM_TEN
        result = f'Это двузначное число, {tmp1 * tmp2}'
        break
    elif NUM_HUNDRED <= num < NUM_THOUSAND:
        tmp1 = num // NUM_HUNDRED
        tmp2 = num // NUM_TEN % NUM_TEN
        tmp3 = num % NUM_TEN
        result = f'Это трёхзначное число, {tmp3 * NUM_HUNDRED + tmp2 * NUM_TEN + tmp1}'
        break
    else:
        print('Ошибка, введено  число не из диапазона')
        continue

print(result)
