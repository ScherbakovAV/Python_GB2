"""Возьмите задачу о банкомате из семинара 2. Разбейте её
на отдельные операции — функции. Дополнительно сохраняйте
все операции поступления и снятия средств в список."""

MULT = 50
PERCENT = 0.985
EXTRA_PERCENT = 1.03
RICH_PERCENT = 0.9
MIN_CASH = 30
MAX_CASH = 600
BONUS_COUNT = 3
MAX_SCORE = 5_000_000


def bonus_cash(total_cash: float | int, count_num: int) -> float:
    if count_num % BONUS_COUNT == 0:
        tmp_cash = total_cash
        total_cash *= EXTRA_PERCENT
        operations_add_to_list(f'+ {total_cash - tmp_cash:.2f} (3 % за каждую третью операцию)')
        print(f'За каждую третью операцию начисляется 3%. '
              f'Вам дополнительно начислено {total_cash - tmp_cash} на остаток по счёту.')

    return total_cash


def operation_add_to_total(money: float | int, count_num: int, total: float | int) -> list[float | int] | None:
    if is_multiplicity(money):
        count_num += 1
        total += money
        print(f'Сумма {money} успешно внесена на счёт')
        operations_add_to_list(f'+ {money} (внесение на счёт)')

        return [total, count_num]

    else:
        print('Сумма должна быть кратна 50!')

        return None


def take_cash(cash: float | int) -> float | int:
    take_off_sum = cash * (1 - PERCENT)

    if take_off_sum > MAX_CASH:
        cash -= MAX_CASH

    elif take_off_sum < MIN_CASH:
        cash -= MIN_CASH

    else:
        cash *= PERCENT

    return cash


def operation_take_from_total(money: float | int, count_num: int, total: float | int) -> list[float | int] | None:
    cash_to_take = take_cash(money)

    if is_multiplicity(money) and not is_overrun(money, total):
        percents = money - cash_to_take
        count_num += 1
        operations_add_to_list(f'- {cash_to_take} (выдача наличных)')
        operations_add_to_list(f'- {percents} (списание процентов на снятие)')

        print(f'Выдано {cash_to_take}, списано процентов {percents}')
        total -= money

        return [total, count_num]

    elif is_overrun(money, total):
        print(f'Превышен лимит. Вы можете снять сумму не более {total}!')

        return

    else:
        print('Сумма должна быть кратна 50!')

        return


def is_multiplicity(cash: float | int) -> bool:
    return True if cash % 50 == 0 and cash != 0 else False


def is_overrun(cash_with_percents: float | int, total_cash: float | int) -> bool:
    return cash_with_percents > total_cash


def rich_tax(total_cash: float | int) -> float | int:
    rich_remove = (total_cash - MAX_SCORE) * (1 - RICH_PERCENT)

    if total_cash > MAX_SCORE:
        operations_add_to_list(f'- {rich_remove:.2f} (налог на богатство 10% на сумму выше 5 млн.)')
        print(f'Вы очень богаты, надо поделиться!\n'
              f'С суммы свыше 5 000 000 Вашего счёта снято 10% '
              f'({rich_remove:.2f})')
        total_cash -= (total_cash - MAX_SCORE) * (1 - RICH_PERCENT)
        print_total_cash(total_cash)

    return total_cash


def print_total_cash(total_cash: float | int) -> None:
    print(f'На Вашем счёте {total_cash:.2f}...\n')


def operations_add_to_list(data: str) -> None:
    global operations_list
    operations_list.append(data)


def operations_print() -> None:
    print('Начальный остаток на счёте: 0.00')
    global operations_list

    for items in operations_list:
        print(items)


def menu() -> None:
    total = 0
    count = 0

    print('________Банкомат________')

    while True:
        print_total_cash(total)

        print(f'Выберите задачу:\n'
              '1. Пополнить счёт\n'
              '2. Снять наличные\n'
              '3. Показать операции текущей сессии\n'
              'Любая другая клавиша: выход из программы')

        operation = input()

        match operation:

            case '1':
                total = rich_tax(total)

                money = float(input('Введите сумму пополнения, кратную 50   '))

                res_add = operation_add_to_total(money, count, total)

                if res_add is not None:
                    count = res_add[1]
                    total = bonus_cash(res_add[0], count)

            case '2':
                if total > 0:
                    total = rich_tax(total)

                    money = float(input('Внимание! Дополнительно взимается сбор 1.5% от суммы снятия, '
                                  'но не менее 30 и не более 600.\nВведите сумму для снятия, кратную 50   '))

                    res_remove = operation_take_from_total(money, count, total)

                    if res_remove:
                        count = res_remove[1]
                        total = bonus_cash(res_remove[0], count)

                else:
                    print('Снятие наличных недоступно, недостаточно средств!\n')

            case '3':
                operations_print()

            case _:
                break


if __name__ == '__main__':
    operations_list = []
    menu()
