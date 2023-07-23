"""Напишите функцию группового переименования файлов. Она должна:
✔ принимать параметр желаемое конечное имя файлов.
При переименовании в конце имени добавляется порядковый номер.
✔ принимать параметр количество цифр в порядковом номере.
✔ принимать параметр расширение исходного файла.
Переименование должно работать только для этих файлов внутри каталога.
✔ принимать параметр расширение конечного файла.
✔ принимать диапазон сохраняемого оригинального имени. Например, для диапазона
[3, 6] берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется
желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
"""
from os import getcwd, listdir, rename

__all__ = ['group_renamer']


def group_renamer(original_name_save_range: list[int], ext_for_rename: str, ext_final: str,
                  file_name_digits_count_end: int = 2, file_name_add: str = '') -> None:
    files_list = listdir(getcwd())
    files_for_rename_list = list()

    for file in files_list:
        if file.split('.')[-1].lower() == ext_for_rename:
            files_for_rename_list.append(file)

    if len(files_for_rename_list) > 0:
        for i in range(len(files_for_rename_list)):
            name_max_range = original_name_save_range[1] \
                if len(files_for_rename_list[i].split('.')[0]) >= original_name_save_range[1] \
                else len(files_for_rename_list[i].split('.')[0])

            rename(f'{files_for_rename_list[i]}',
                   f'{files_for_rename_list[i][original_name_save_range[0] - 1 : name_max_range]}'
                   f'{file_name_add}{"0" * (file_name_digits_count_end - 1)}{i + 1}.{ext_final}')

        print(f'Переименование файлов с расширением .{ext_for_rename} успешно произведено')

    else:
        print(f'Файлов с расширением .{ext_for_rename} в каталоге нет!')
