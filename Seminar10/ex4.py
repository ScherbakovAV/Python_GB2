'''Создайте класс Сотрудник.
Воспользуйтесь классом человека из прошлого задания.
У сотрудника должен быть:
○ шестизначный идентификационный номер
○ уровень доступа вычисляемый как остаток от деления
суммы цифр id на семь'''

from ex3 import Person


class Employer(Person):
    DEFAULT_ID = 100_000
    MAX_LEVEL = 7

    
    def __init__(self, second_name: str, first_name: str, age: int, phone: str, id: int, patronymic: str = None):
        super().__init__(second_name, first_name, age, phone, patronymic)
        if 100_000 <= id <= 999_999:
            self.id = id
        else:
            self.id = DEFAULT_ID


    def get_age(self):
        return sum(int(digit) for digit in str(self.id)) % self.MAX_LEVEL


if __name__ == '__main__':
    emp = Employer('Иванов', 'Иван', 42, '8-999-987-11-11', 100257, 'Иванович')

    print(emp.get_full_name())
    print(emp.id)
    print(emp.get_age())
