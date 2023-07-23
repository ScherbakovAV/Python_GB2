""" Создайте класс Моя Строка, где:
- будут доступны все возможности str
- дополнительно хранятся имя автора строки и время создания (time.time)"""

from time import time


class MyString(str):
    """Класс, которому доступны все возможности str.
    В экземплярах класса дополнительно хранятся:\n
    - имя автора строки (author_name)\n
    - время создания (time_created)"""

    def __new__(cls, value: str, author_name: str):
        instance = super().__new__(cls, value)
        instance.author_name = author_name
        instance.time_created = time()
        print(f'Класс {cls} создан')
        return instance


if __name__ == '__main__':
    new_str = MyString('Hello, everybody!', 'It`s me')
    print(new_str)
    print(f'{new_str.author_name = }')
    print(f'{new_str.time_created = }')

    print(MyString.__doc__)
    # print(help(MyString))
