"""Задание №4
✔ Функция получает на вход список чисел.
✔ Отсортируйте его элементы in place без использования
встроенных в язык сортировок.
✔ Как вариант напишите сортировку пузырьком.
Её описание есть в википедии."""


def sort_num(num_list: list[int]) -> None:
    for i in range(len(num_list) - 1):
        for j in range(i + 1, len(num_list)):
            if num_list[i] > num_list[j]:
                tmp = num_list[i]
                num_list[i] = num_list[j]
                num_list[j] = tmp


if __name__ == '__main__':
    el = [5, 2, 6, 7, 3, -1, 0]
    sort_num(el)
    print(el)
