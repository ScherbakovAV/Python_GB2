"""Напишите функцию, которая сохраняет созданный в
прошлом задании файл в формате CSV."""
import csv
import json


def json_to_scv(file_name: str) -> None:
    users_data = []

    with(open(file_name, encoding='utf-8') as json_file,
         open('ex3.csv', 'w', encoding='utf-8') as csv_file
         ):
        for level, user_info in json.load(json_file).items():
            for user_id, user_name in user_info.items():
                users_data.append({'level': int(level), 'id': user_id, 'name': user_name})
        csv_writer = csv.DictWriter(csv_file, dialect='excel', fieldnames=('level', 'id', 'name'), lineterminator='\n')
        csv_writer.writeheader()
        csv_writer.writerows(users_data)


if __name__ == '__main__':
    json_to_scv('ex2_file.json')
