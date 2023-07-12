import csv
import pickle


def pickle_to_csv(file_name):
    with open(file_name, 'rb') as pickle_file:
        data = pickle.load(pickle_file)
    users_data = []

    for level, user_info in data.items():
        for user_id, user_name in user_info.items():
            users_data.append({'level': int(level), 'id': user_id, 'name/hash': user_name})

    with open(f'ex6.csv', 'w', encoding='utf-8') as csv_file:
        csv_writer = csv.DictWriter(csv_file, dialect='excel',
                                    fieldnames=('level', 'id', 'name/hash'),
                                    lineterminator='\n',
                                    quoting=csv.QUOTE_ALL)

        csv_writer = csv.DictWriter(csv_file, dialect='excel', fieldnames=('level', 'id', 'name/hash'), lineterminator='\n')
        csv_writer.writeheader()
        csv_writer.writerows(users_data)
