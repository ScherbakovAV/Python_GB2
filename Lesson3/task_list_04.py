a = 42
b = 'Hello'
c = [1, 3, 5, 7]
my_list = [None]
# my_list.extend(a) # не сработает
print(my_list)
my_list.extend(b)
print(my_list)
my_list.extend(c)
print(my_list)
my_list.extend(my_list)
print(my_list)
