"""Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
Дополните id до 10 цифр незначащими нулями. В именах первую букву сделайте прописной.
Добавьте поле хеш на основе имени и идентификатора. Получившиеся записи сохраните в json файл,
где каждая строка csv файла представлена как отдельный json словарь.
Имя исходного и конечного файлов передавайте как аргументы функции."""
from os import getcwd

from HW8.hw8_package.ex4_func import csv_to_json

if __name__ == '__main__':
    csv_to_json(f'{getcwd()}\\..\\Seminar8\\ex3.csv', 'ex4.json')
