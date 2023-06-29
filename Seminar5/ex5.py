"""Задание №5
✔ Напишите программу, которая выводит
на экран числа от 1 до 100.
✔ При этом вместо чисел, кратных трем,
программа должна выводить слово «Fizz»
✔ Вместо чисел, кратных пяти — слово «Buzz».
✔ Если число кратно и 3, и 5, то программа
должна выводить слово «FizzBuzz».
✔ *Превратите решение в генераторное выражение."""

for num in range(1, 101):
    if num % 15 == 0:
        print('FizzBuzz', end=' ')
    elif num % 3 == 0:
        print('Fizz', end=' ')
    elif num % 5 == 0:
        print('Buzz', end=' ')
    else:
        print(num, end=' ')

print()
print(*('FizzBuzz' if num % 15 == 0 else 'Fizz' if num % 3 == 0 else 'Buzz' if num % 5 == 0 else num
        for num in range(1, 101)))
