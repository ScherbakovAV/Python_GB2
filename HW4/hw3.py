"""Напишите функцию, принимающую на вход только ключевые
параметры и возвращающую словарь, где ключ — значение
переданного аргумента, а значение — имя аргумента. Если
ключ не хэшируем, используйте его строковое представление."""


def pos_args_dict(**kwargs):
    invert_variables = dict()

    for key, value in kwargs.items():
        if value.__hash__:
            invert_variables[value] = key
        else:
            invert_variables[str(value)] = key

    return invert_variables


if __name__ == '__main__':
    print(pos_args_dict(var_1=5, var_2=-1.5, var_3='anything', var_4=[True, False]))
