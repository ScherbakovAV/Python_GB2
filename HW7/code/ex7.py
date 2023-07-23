"""Задание №7 семинара 7
✔ Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
✔ Каждая группа включает файлы с несколькими расширениями.
✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки."""

from os import makedirs, listdir, rename

__all__ = ['files_sorting']


def files_sorting(folder_for_sort: str) -> None:
    extensions = {'videos': ['avi', 'mpg', '3gp', 'mkv', 'mov', 'wmv'],
                  'pictures': ['jpeg', 'jpg', 'bmp', 'gif', 'png'],
                  'texts': ['doc', 'rtf', 'docx', 'md', 'txt'],
                  'musics': ['mp3', 'wav', 'ogg', 'wma'],
                  'binary': ['bin']}
    files = listdir(folder_for_sort)

    for file in files:
        for file_type, ext in extensions.items():
            if file.split('.')[-1].lower() in ext:
                makedirs(f'{folder_for_sort}\\sorted\\{file_type}', exist_ok=True)
                rename(f'{folder_for_sort}\\{file}', f'{folder_for_sort}\\sorted\\{file_type}\\{file}')

    print('Сортировка прошла успешно')
