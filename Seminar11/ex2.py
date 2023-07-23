""" Создайте класс Архив, который хранит пару свойств,
например, число и строку.
- При создании нового экземпляра класса, старые данные из ранее
созданных экземпляров сохраняются в пару списков-архивов.
- list-архивы также являются свойствами экземпляра"""


class Archive:
    """Класс, хранящий пару свойств (число (num) и строку (text)).\n
    При создании нового экземпляра класса, старые данные из ранее созданных
    экземпляров сохраняются в пару списков-архивов, которые также являются свойствами экземпляра
    """

    __instance = None

    def __init__(self, num: int, text: str):
        self.num = num
        self.text = text

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.num_list = []
            cls.__instance.text_list = []
        else:
            cls.__instance.num_list.append(cls.__instance.num)
            cls.__instance.text_list.append(cls.__instance.text)
        return cls.__instance

    def __str__(self):
        return f'Текст: {self.text}, число: {self.num}, ' \
               f'архив текста: {self.text_list}, архив чисел: {self.num_list}'

    def __repr__(self) -> str:
        return f'Archive({self.num}, \'{self.text}\')'


if __name__ == '__main__':
    arch1 = Archive(1, 'test')
    print(arch1.num_list)
    print(arch1.text_list)

    arch2 = Archive(2, 'Hi!')
    print(arch2.num_list)
    print(arch2.text_list)

    arch3 = Archive(3, 'guys!')
    print(arch3.num_list)
    print(arch3.text_list)

    print(Archive.__doc__)
    # print(help(Archive))

    print(arch3)
    print(f'{arch3 = }')
    print(repr(arch3))
