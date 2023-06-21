'''
if __name__ == '__main__':
    num = int(input('Введите целое число... '))
    num2: str = dec_to_n(num, input_n())
    print(num2)
    print(f'Это число в двоичном представлении - {bin(num)}')
    print(f'Это число в восьмеричном представлении - {oct(num)}')
    print(f'Это число в десятичном представлении - {int(num2, base=2)}')
'''