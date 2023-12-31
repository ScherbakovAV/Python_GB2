"""
Создайте в переменной data список значений разных типов перечислив их через
запятую внутри квадратных скобок. Для каждого элемента в цикле выведите:
✔ порядковый номер начиная с единицы.
✔ значение.
✔ адрес в памяти.
✔ размер в памяти.
✔ хэш объекта.
✔ результат проверки на целое число только если он положительный.
✔ результат проверки на строку только если он положительный.
Добавьте в список повторяющиеся элементы и сравните на результаты. """

import sys

data = [1, 5.5, 'new str', True, (2, 4, 3), 1, 'new str', True]

for i, item in enumerate(data, start=1):
    check_int = ', это целое число' if isinstance(item, int) else ''
    check_str = ', это строка' if isinstance(item, str) else ''

    print(f'Порядковый номер - {i},'
          f'Значение - {item}, '
          f'Адрес в памяти - {id(item)}, '
          f'Размер в памяти - {sys.getsizeof(item)}, '
          f'Хэш - {hash(item)}'
          f'{check_int}'
          f'{check_str}')
