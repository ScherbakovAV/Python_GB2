my_list = [4, 8, 2, 9, 1, 7, 2]
res = reversed(my_list) # это не лист, а итератор
print(type(res), res)

rev_list = list(reversed(my_list)) # чтобы получить лист
print(rev_list)

for item in reversed(my_list):
    print(item)
