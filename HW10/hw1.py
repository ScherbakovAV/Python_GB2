'''Доработаем задачи 5-6. Создайте класс-фабрику.
○ Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
○ Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.
'''

from ex6 import Bird
from ex6 import Fish
from ex6 import Mammal


class AnimalFabric():
    def __init__(self, animal_type: str, name: str, uniq: int):
        self.animal_type = animal_type
        self.name = name
        self.unique_param = uniq


    def unique(self):
        pass
    
        
    def creating_animal(self):
        if self.animal_type == 'Bird':
            return Bird(self.name, self.unique_param)
        elif self.animal_type == 'Fish':
            return Fish(self.name, self.unique_param)
        elif self.animal_type == 'Mammal':
            return Mammal(self.name, self.unique_param)


if __name__ == '__main__':
    animal1 = AnimalFabric('Bird', 'Ласточка', 20)
    bird1 = animal1.creating_animal()
    print(bird1.unique())
