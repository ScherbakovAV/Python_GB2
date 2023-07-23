import pickle


def csv_to_pickle(file_name):
    with open(file_name, encoding='utf-8') as file:
        data = file.readlines()

    data_fields = data[0][:-1].split(',')
    form_data = []

    for item in data[1:]:
        level, user_id, user_name = item[:-1].split(',')
        form_data.append({data_fields[0]: level, data_fields[1]: user_id, data_fields[2]: user_name})

    print(f'{form_data}\n{pickle.dumps(form_data)}')
