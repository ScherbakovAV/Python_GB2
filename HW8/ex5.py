"""Напишите функцию, которая ищет json файлы в указанной
директории и сохраняет их содержимое в виде
одноимённых pickle файлов."""
from os import getcwd

from HW8.hw8_package.ex5_func import all_json_to_pickle

if __name__ == '__main__':
    all_json_to_pickle(getcwd())
