import json

ID_DIGITS = 10


def csv_to_json(input_file: str, output_file: str) -> None:
    csv_data = []
    with open(input_file, encoding='utf-8') as file_csv:
        for line in file_csv.readlines()[1:]:
            level, user_id, user_name = line[:-1].split(',')
            level = int(level)
            user_id = user_id.zfill(ID_DIGITS)
            user_name = user_name.capitalize()
            user_hash = f'{hash(user_id + user_name)}'
            csv_data.append([level, user_id, user_name, user_hash])

    json_dict = {int(i): {} for i in range(1, 8)}
    for item in csv_data:
        json_dict[item[0]][item[1]] = f'{item[2]} / {item[3]}'

    with open(output_file, 'w', encoding='utf-8') as file_json:
        json.dump(json_dict, file_json, ensure_ascii=False, indent=2)
