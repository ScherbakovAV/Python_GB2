link = 'https://habr.com/ru/users/dzhoker1/posts/'
urls = link.split('/')
print(urls)

a, b, c = input('Введите три числа через пробел: ').split()
print(c, b, a)

a, b, c, *_ = input('Введите более трёх чисел через пробел: '). split()
