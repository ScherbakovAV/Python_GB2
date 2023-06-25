"""zip(*iterables, strict=False)"""
names = ['Иван', 'Николай', 'Пётр']
salaries = [125000, 96000, 109000]
awards = [0.1, 0.25, 0.13, 0.99]
for name, salary, award in zip(names, salaries, awards):
    print(f'{name} заработал {salary:.2f} денег и премию {salary * award:.2f}')
