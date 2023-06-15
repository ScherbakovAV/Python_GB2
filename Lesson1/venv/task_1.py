import sys

name = 'Anatoliy'
age = None
print(id(name))
a = 3
print(id(a))
a = 'Hello, world'
print(id(a))
print(a)

''' print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False) // 
    * - распаковка объектов
    sep - разделитель
    По умолчанию в end перенос строки
result = input([prompt]) '''

print(name, age, a, 456, 'text')
print(name, age, a, 456, 'text', sep=' =^.^= ')
print(name, age, a, 456, 'text', sep=' =^.^= ', end='#')

res = input('Print your text: ')
print('You printed', res)

age = int(input('How old are you? '))
how_old = 18 - age
print(how_old, 'Осталось до совершеннолетия')

ADULT = 18


