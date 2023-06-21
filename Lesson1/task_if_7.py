year = int(input('Введите год в формате yyyy: '))
if year % 4 != 0:
    print('Обычный год')
elif year % 100 == 0:
    if year % 4000 != 0:
        print('Год високосный')
    else:
        print('Год Обычный')
else:
    print('Год високосный')
