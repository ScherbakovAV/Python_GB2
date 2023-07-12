import json
from os.path import isfile


def input_users_data(file_name: str) -> None:
    unique_id = set()

    if isfile(file_name):
        with open(file_name, encoding='utf-8') as file:
            file_data = json.load(file)

        for _, vol in file_data.items():
            unique_id.update(vol.keys())

    else:
        file_data = {i: {} for i in range(1, 8)}

    while True:
        user_name = input('Введите имя пользователя: ')

        user_id = input('Введите идентификатор пользователя: ')
        if user_id in unique_id:
            print('Такой идентификатор доступа есть в базе!')
            continue

        level = int(input('Введите уровень доступа (от 1 до 7): '))

        unique_id.add(user_id)

        file_data[level].update({user_id: user_name})

        with open(file_name, 'w', encoding='utf-8') as f:
            json.dump(file_data, f, ensure_ascii=False, indent=2)
