"""Задание №3
✔ Напишите функцию, которая открывает на чтение созданные
в прошлых задачах файлы с числами и именами.
✔ Перемножьте пары чисел. В новый файл сохраните
имя и произведение:
✔ если результат умножения отрицательный, сохраните имя
записанное строчными буквами и произведение по модулю
✔ если результат умножения положительный, сохраните имя
прописными буквами и произведение округлённое до целого.
✔ В результирующем файле должно быть столько же строк,
сколько в более длинном файле.
✔ При достижении конца более короткого файла,
возвращайтесь в его начало."""

__all__ = ['convert']


def convert(names_file: str, nums_name: str, result_file: str) -> None:
    with(open(names_file, encoding='utf-8') as f_names,
         open(nums_name, encoding='utf-8') as f_nums,
         open(result_file, 'w', encoding='utf-8') as f_res
         ):
        data_nums = f_nums.readlines()
        data_names = f_names.readlines()

        for i in range(min(len(data_nums), len(data_names))):
            int_value, float_value = data_nums[i].split('|')
            int_value = int(int_value)
            float_value = float(float_value)
            mult_res = int_value * float_value

            if mult_res < 0:
                res = f'{data_names[i][:-2].lower()} {str(abs(mult_res))}'
            else:
                res = f'{data_names[i][:-2].upper()} {str(round(mult_res))}'

            f_res.write(res + '\n')

        str_n = min(len(data_nums), len(data_names))
        len_dif = abs(len(data_nums) - len(data_names))
        is_long_names = len(data_names) > len(data_nums)

        if is_long_names:
            short, long = data_nums, data_names
        else:
            short, long = data_names, data_nums

        for i in range(len_dif):
            if is_long_names:
                int_value, float_value = short[i].split('|')
                int_value = int(int_value)
                float_value = float(float_value)
                mult_res = int_value * float_value

                if mult_res < 0:
                    res = f'{long[str_n + i][:-2].lower()} {str(abs(mult_res))}'
                else:
                    res = f'{long[str_n + i][:-2].upper()} {str(round(mult_res))}'

            else:
                int_value, float_value = long[str_n + i].split('|')
                int_value = int(int_value)
                float_value = float(float_value)
                mult_res = int_value * float_value

                if mult_res < 0:
                    res = f'{short[str_n + i][:-2].lower()} {str(abs(mult_res))}'
                else:
                    res = f'{short[str_n + i][:-2].upper()} {str(round(mult_res))}'

            f_res.write(res + '\n')


if __name__ == '__main__':
    convert('ex2_file.txt', 'ex1_file.txt', 'ex3_file.txt')
