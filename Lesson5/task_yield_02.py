def factorial(n):
    number = 1
    for i in range(1, n + 1):
        number *= i
        yield number


for j, num in enumerate(factorial(10), start=1):
    print(f'{j} ! = {num}')
