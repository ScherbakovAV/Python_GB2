""" Создайте несколько переменных разных типов.
Проверьте к какому типу относятся созданные переменные."""

a = 3
b = 5.5
c = 'str'
d = True
e = (1, 2, 3)
f = [1, 2, 3]

arr = [a, b, c, d, e, f]


def print_type(lst):
    for item in lst:
        print(f'Переменная {item} - {type(item)}')


print_type(arr)
