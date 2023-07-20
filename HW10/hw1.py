'''Доработаем задачи 5-6. Создайте класс-фабрику.
○ Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
○ Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.
'''

from ex6 import Bird
from ex6 import Fish
from ex6 import Mammal


class AnimalFabric():
    def __init__(self, animal_class: class, *args, **kwargs):
        
        
