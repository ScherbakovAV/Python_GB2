"""Задание №3
✔ Функция получает на вход строку из двух чисел через пробел.
✔ Сформируйте словарь, где ключом будет
символ из Unicode, а значением — целое число.
✔ Диапазон пар ключ-значение от наименьшего из введённых
пользователем чисел до наибольшего включительно."""


def symbols_number(num_text: str) -> dict[str, int]:
    num1, num2 = map(int, num_text.split())
    num_dict = dict()

    for i in range(min(num1, num2), max(num1, num2) + 1):
        num_dict[chr(i)] = i

    return num_dict


if __name__ == '__main__':
    txt = input('Введите два числа диапазона через пробел: ')
    print(symbols_number(txt))
