from os import getcwd

from Seminar7.ex1 import rand_numbers_in_file
from Seminar7.ex2 import pseudo_names_in_file
from Seminar7.ex3 import convert
from Seminar7.ex4 import gen_ext
from HW7.code.ex5and6 import gen_files
from HW7.code.ex7 import files_sorting
from HW7.code.hw1 import group_renamer

if __name__ == '__main__':
    ex_num = input(f'Выберите номер задачи:\n'
                   f'1: Задача №1 семинара (Заполнение файла случайными парами чисел)\n'
                   f'2: Задача №2 семинара (генерация псевдоимён в файл)\n'
                   f'3: Задача №3 семинара (перемножение данных предыдущих задач в файл)\n'
                   f'4: Задача №4 семинара (создание файлов с бинарными данными с указанным расширением)\n'
                   f'5: Задачи №5,6 семинара (создание файлов с бинарными данными с разными расширениями)\n'
                   f'6: Задача №7 семинара (сортировка файлов по директориям)\n'
                   f'7: Задача с домашней работы (групповое переименование файлов)\n')

    match ex_num:
        case('1'):
            rand_numbers_in_file(8, 'ex1_file.txt')
        case('2'):
            pseudo_names_in_file(10, 'ex2_file.txt')
        case('3'):
            convert('ex2_file.txt', 'ex1_file.txt', 'ex3_file.txt')
        case('4'):
            gen_ext('bin', getcwd(), num_files=2)
        case('5'):
            gen_files(folder=f'{getcwd()}', bin=2, txt=1, doc=1)
        case('6'):
            files_sorting(getcwd())
        case('7'):
            group_renamer([1, 3], 'txt', 'md', file_name_digits_count_end=3, file_name_add='_renamed_')
