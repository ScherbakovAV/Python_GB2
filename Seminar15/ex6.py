"""Напишите код, который запускается из командной строки и получает на вход
путь до директории на ПК.
Соберите информацию о содержимом в виде объектов namedtuple.
Каждый объект хранит:
- имя файла без расширения или название каталога
- расширение, если это файл
- флаг каталога
- название родительского каталога.
В процессе сбора сохраните данные в текстовый файл используя
логирование"""
# Не доделана, на ДЗ

import os.path
from os import listdir
import argparse
import logging
from collections import namedtuple

logging.basicConfig(filename='log6.log', level=logging.INFO, encoding='utf-8')
logger = logging.getLogger(__name__)

file = namedtuple(typename='file', field_names='file_path, ext, folder, parent_folder')


def directory_info(file_p: str):
    files_list = listdir(file_p)
    p = file_p.split(os.path.pathsep)
    for item in files_list:
        if os.path.isfile(item):
            temp = item.split('.')
            obj = file(temp[0], temp[1], p[-1], f'\\'.join(p[:-1]))
        else:

            obj = file(item, '', p[-1], f'{os.path.pathsep}'.join(p[:-1]))
        logger.info(obj)


print(directory_info(r'E:\Geek Brains\Git\Python_education2\Seminar15'))
