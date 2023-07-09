"""Задание №4
✔ Создайте функцию, которая создаёт файлы с указанным расширением.
Функция принимает следующие параметры:
✔ расширение
✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
✔ минимальное число случайных байтов, записанных в файл, по умолчанию 256
✔ максимальное число случайных байтов, записанных в файл, по умолчанию 4096
✔ количество файлов, по умолчанию 42
✔ Имя файла и его размер должны быть в рамках переданного диапазона."""

from random import choices, randint
from string import ascii_lowercase, digits
from os import getcwd, listdir


def gen_ext(ext: str, directory: str, name_len_min: int = 6, name_len_max: int = 30, bytes_min: int = 256,
            bytes_max: int = 4096, num_files: int = 42) -> None:

    for i in range(num_files):
        name = ''.join(choices(ascii_lowercase + digits + '_', k=randint(name_len_min, name_len_max)))
        data = bytes(randint(0, 255) for _ in range(randint(bytes_min, bytes_max)))
        file_name = f'{name}.{ext}'

        if file_name not in listdir(directory):
            with open(f'{directory}\\{file_name}', 'wb') as f:
                f.write(data)
            print(f'Файл {file_name} успешно создан в директории {directory}')
        else:
            print(f'Файл {file_name} существует, новый файл не записан!')


if __name__ == '__main__':
    gen_ext('bin', getcwd(), num_files=2)
