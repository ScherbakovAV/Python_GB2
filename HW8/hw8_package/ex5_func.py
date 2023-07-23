import json
import pickle
from os import listdir


def all_json_to_pickle(path: str) -> None:
    files_json = [file for file in listdir(path) if file.split('.')[-1].lower() == 'json']

    for file in files_json:
        with(open(file, encoding='utf-8') as source,
             open(f'ex5.pickle', 'wb') as pickle_file
             ):
            pickle.dump(json.load(source), pickle_file)
