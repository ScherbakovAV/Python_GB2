"""Напишите функцию, которая в бесконечном цикле запрашивает имя, личный идентификатор и уровень
доступа (от 1 до 7). После каждого ввода добавляйте новую информацию в JSON файл.
Пользователи группируются по уровню доступа. Идентификатор пользователя выступает ключом для имени.
Убедитесь, что все идентификаторы уникальны независимо от уровня доступа.
При перезапуске функции уже записанные в файл данные должны сохраняться."""
from HW8.hw8_package.ex2_func import input_users_data

if __name__ == '__main__':
    input_users_data('ex2_file.json')
