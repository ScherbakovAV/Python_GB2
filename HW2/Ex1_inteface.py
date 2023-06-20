import Ex1
from Ex1_input import positive_num_input as inp_num


def menu(total_money, counts):
    total = total_money
    count = counts

    print('________Банкомат________')

    while True:
        Ex1.print_total_cash(total)

        print(f'Выберите задачу:\n'
              '1. Пополнить счёт\n'
              '2. Снять наличные\n'
              'Любая другая клавиша: выход из программы')

        operation = input()

        match operation:

            case '1':
                money = inp_num('Введите сумму пополнения, кратную 50')

                res_add = Ex1.operation_add_to_total(money, count, total)
                total = res_add[0]
                count = res_add[1]

                continue

            case '2':
                if total > 0:
                    money = inp_num('Введите сумму для снятия, кратную 50 (внимание, взимается процент на снятие 1,5%!)')

                    res_remove = Ex1.operation_take_from_total(money, count, total)
                    total = res_remove[0]
                    count = res_remove[1]

                else:
                    print('Снятие наличных недоступно, недостаточно средств!\n')

                continue

            case _:
                break


menu(Ex1.total_score, Ex1.count)
