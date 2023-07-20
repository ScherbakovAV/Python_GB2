'''Напишите класс для хранения информации о человеке:
ФИО, возраст и т.п. на ваш выбор.
У класса должны быть методы birthday для увеличения
возраста на год, full_name для вывода полного ФИО и т.п. на
ваш выбор.
Убедитесь, что свойство возраст недоступно для прямого
изменения, но есть возможность получить текущий возраст.
'''


class Person:
    def __init__(self, second_name: str, first_name: str, age: int, phone: str, patronymic: str = None):
        self.second_name = second_name
        self.first_name = first_name
        self.__age = age
        self.phone = phone
        if patronymic is None:
            self.patronymic = None
        else:
            self.patronymic = patronymic


    def birthday_up(self):
        self.__age += 1


    def get_age(self):
        return self.__age


    def get_full_name(self):
        if self.patronymic is None:
            return f'{self.second_name} {self.first_name}'
        else:
            return f'{self.second_name} {self.first_name} {self.patronymic}'


if __name__ == '__main__':
    person1 = Person('Щербаков', 'Анатолий', 37, '8(988)333-44-11', 'Владимирович')
    person2 = Person('John', 'Smith', 29, '+7(988)222-44-11')

    print(person1.get_full_name())
    print(person1.get_age())
    person1.birthday_up()
    print(person1.get_age())
    print(person1.phone)

    print(person2.get_full_name())
    print(person2.get_age())
    person2.birthday_up()
    print(person2.get_age())
    print(person2.phone)

    # print(person2.__age)

