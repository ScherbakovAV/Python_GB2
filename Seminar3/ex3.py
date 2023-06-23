"""
✔ Создайте вручную кортеж содержащий элементы разных типов.
✔ Получите из него словарь списков, где:
- ключ — тип элемента,
- значение — список элементов данного типа.
"""

data = (4, 6, 'aaaa', 5.5, True, 5.5, 1.11, 'kkk')
print(data)
words = {}

for item in data:
    types1 = type(item)

    if types1 in words:
        words[types1].append(item)

    else:
        words[types1] = [item]

print(words)
