"""Вспоминаем задачу 3 из прошлого семинара. Мы сформировали текстовый файл с псевдоименами и произведением чисел.
Напишите функцию, которая создаёт из созданного ранее файла новый с данными в формате JSON.
Имена пишите с большой буквы. Каждую пару сохраняйте с новой строки.
"""
from HW8.hw8_package.ex1_func import text_to_json

if __name__ == '__main__':
    text_to_json('ex1_source.txt')