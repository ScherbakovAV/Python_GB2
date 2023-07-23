"""Вспоминаем задачу 3 из прошлого семинара. Мы сформировали текстовый файл с псевдоименами и произведением чисел.
Напишите функцию, которая создаёт из созданного ранее файла новый с данными в формате JSON.
Имена пишите с большой буквы. Каждую пару сохраняйте с новой строки.
"""
import json


def text_to_json(file_name: str) -> None:
    with(open(file_name, encoding='utf-8') as source,
         open(f'ex1.json', 'w') as json_file
         ):
        file_dict = {line.split(' ')[0].capitalize(): float(line.split(' ')[1][:-1])
                     for line in source.readlines()}
        json.dump(file_dict, json_file, ensure_ascii=False, indent=2)


if __name__ == '__main__':
    text_to_json('ex3_sem7_file.txt')
