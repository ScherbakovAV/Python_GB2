import fractions
import sys
from HW2 import Ex1, Ex1_inteface, Ex2, Ex3, input_num

if __name__ == '__main__':
    task = input(f'Введите номер задачи:\n'
                 f'1 - банкомат\n'
                 f'2 - конвертер чисел в шестнадцатеричное представление\n'
                 f'3 - сумма и произведение дробей\n')
    match task:
        case '1':
            Ex1_inteface.menu(Ex1.total_score, Ex1.count)

        case '2':
            num = input_num.positive_num_input('Введите число для перевода '
                                               'из двоичной системы счисления в шестнадцатеричную', 2)
            num_hex = Ex2.dec_to_hex(num)
            print(f'Это число в шестнадцатеричном представлении - {num_hex}')
            print(f'Проверка встроенной функцией hex: {Ex2.check_hex(num_hex, num)}')

        case '3':
            fraction_str1 = Ex3.add_fraction(1)
            fraction_number1 = Ex3.str_fraction_split(fraction_str1)

            fraction_str2 = Ex3.add_fraction(2)
            fraction_number2 = Ex3.str_fraction_split(fraction_str2)

            num1_check = fractions.Fraction(int(fraction_number1[0]), int(fraction_number1[1]))
            num2_check = fractions.Fraction(int(fraction_number2[0]), int(fraction_number2[1]))

            print(f'{fraction_str1} + {fraction_str2} = '
                  f'{Ex3.list_fractions_to_str(Ex3.fraction_sum(fraction_number1, fraction_number2))}\n'
                  f'(проверка = {num1_check + num2_check})')
            print(f'{fraction_str1} x {fraction_str2} = '
                  f'{Ex3.list_fractions_to_str(Ex3.fraction_mult(fraction_number1, fraction_number2))}\n'
                  f'(проверка = {num1_check * num2_check})')

        case _:
            sys.exit()
