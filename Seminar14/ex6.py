### На ДЗ

"""На семинаре 13 был создан проект по работе с
пользователями (имя, id, уровень).
Напишите 3-7 тестов pytest для данного проекта.
Используйте фикстуры."""

import json
import os.path

from Seminar13.ex5 import Project
from Seminar13.ex4 import UserData, data_from_json
import pytest

FILE = 'ex6.json'


# @pytest.fixture
# def get_file():
#     new_data = {
#         1: {100: 'Нео'},
#         2: {101: 'Дипси'},
#         3: {102: 'Дамбо'}
#     }
#     with open(FILE, 'w', encoding='utf-8') as f:
#         json.dump(new_data, f, ensure_ascii=True)
#     return new_data
#
#
# @pytest.fixture
# def add_users():
#     new_project = Project()
#     return new_project.load_json(FILE)
#
#
# def test_write_json():
#     with open(FILE, 'w', encoding='utf-8') as f:
#         json.dumps(setup, f)
#     assert os.path.exists(FILE)
#
#
# def test_load_json():
#     test_result = data_from_json(FILE)
#     # test_set = test_user.data_from_json(FILE)
#     assert test_result == setup
#
#
# def test_enter_user():
#     new_pr = Project()
#     new_pr.load_json(FILE)
#     new_pr.enter('Рембо', 104)
#     assert new_pr == setup
#
#
# def test_add_not_unique_user():
#     new_pr = Project()
#     new_pr.load_json(FILE)
#     new_pr.enter('Нео', 100)
#     assert new_pr != setup


if __name__ == '__main__':
    pytest.main(['-vv'])
    # project1 = Project()
    # project1.load_json('ex4_file.json')
    # print(project1.enter('Мурка', 145))
    # # print(project1.enter('Максим', 11))
    # print(f'Добавлен {project1.add_user("test", 458, 9)}')
    # # print(f'Добавлен {project1.add_user("new", 34, 1)}')
    # print(project1.enter('test', 458))
