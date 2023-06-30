"""Напишите однострочный генератор словаря, который принимает
на вход три списка одинаковой длины: имена str, ставка int,
премия str с указанием процентов вида «10.25%». В результате
получаем словарь с именем в качестве ключа и суммой
премии в качестве значения. Сумма рассчитывается
как ставка умноженная на процент премии"""

if __name__ == '__main__':
    names = ['Анна', 'Иван', 'Андрей', 'Софья', 'Елена']
    salaries = [35_320, 51_180, 18_120, 55_050, 32_340]
    percents = ['15.20%', '10.32%', '5.50%', '0.00%', '20.00%']

    bonuses = {names[i]: round(salaries[i] * (float(percents[i][:-1:]) / 100), 2)
               for i in range(len(salaries))
               if len(names) == len(salaries) == len(percents)}

    print(bonuses)
