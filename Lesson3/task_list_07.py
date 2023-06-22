my_list = [2, 4, 6, 8, 10, 12, 2, 4, 14, 2]
spam = my_list.index(4)
print(spam)
eggs = my_list.index(4, spam + 1, 90) # нет ошибки при выходе за пределы
print(eggs)
err = my_list.index(3)
