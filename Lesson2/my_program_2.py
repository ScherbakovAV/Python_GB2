user_str = input('Введите текст ')
if user_str.isdigit():
    print(int(user_str))
    print(int(user_str, base=8))
    print(int(user_str, base=16))
else:
    if user_str.isascii():
        print('Это текст на ASII')
    else:
        print('Этот текст не на ASCII')
