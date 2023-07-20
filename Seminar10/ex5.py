'''Создайте три (или более) отдельных классов животных.
Например рыбы, птицы и т.п.
У каждого класса должны быть как общие свойства,
например имя, так и специфичные для класса.
Для каждого класса создайте метод, выводящий
информацию специфичную для данного класса.
'''


class Fish:
    MIN_PARAM = 50
    MAX_PARAM = 500

    
    def __init__(self, name: str, depth: int):
        self.__name = name
        self.__depth = depth


    def get_name(self):
        return self.__name


    def get_depth(self):
        return self.__depth


    def unique(self):
        if self.__depth < self.MIN_PARAM:
            return f'{self.__name} - мелководная рыба'
        elif self.__depth > self.MAX_PARAM:
            return f'{self.__name} - глубоководная рыба'
        else:
            return f'{self.__name} - средневодная рыба'
        


class Bird:    
    def __init__(self, name: str, wing: int):
        self.__name = name
        self.__wing = wing


    def get_name(self):
        return self.__name


    def get_wing(self):
        return self.__wing


    def unique(self):
        return self.__wing * 2


class Mammal:
    MIN_PARAM = 10
    MAX_PARAM = 80

    
    def __init__(self, name: str, speed: int):
        self.__name = name
        self.__speed = speed


    def get_name(self):
        return self.__speed


    def get_depth(self):
        return self.__depth


    def unique(self):
        if self.__speed < self.MIN_PARAM:
            return f'{self.__name} - медленное животное'
        elif self.__speed > self.MAX_PARAM:
            return f'{self.__name} - быстрейшее животное'
        else:
            return f'{self.__name} - обычное животное'


if __name__ == '__main__':
    fish1 = Fish('Карась', 10)
    fish2 = Fish('Щука', 100)
    fish3 = Fish('Удильщик', 800)

    print(fish1.unique())
    print(fish2.unique())
    print(fish3.unique())

    bird1 = Bird('Воробей', 3)
    bird2 = Bird('сорока', 30)
    bird3 = Bird('альбатрос', 60)

    print(f'Размах крыла птицы {bird1.get_name()} - {bird1.unique()}')
    print(f'Размах крыла птицы {bird2.get_name()} - {bird2.unique()}')
    print(f'Размах крыла птицы {bird3.get_name()} - {bird3.unique()}')

    mammal1 = Mammal('Ленивец', 4)
    mammal2 = Mammal('Волк', 40)
    mammal3 = Mammal('Гепард', 120)

    print(mammal1.unique())
    print(mammal2.unique())
    print(mammal3.unique())

