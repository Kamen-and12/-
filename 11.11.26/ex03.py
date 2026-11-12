import itertools
found = -1
counter = 0

for i in itertools.count():
    row = input('Введите строку: ')

    counter += 1

    if 'Кот' in row or 'кот' in row:
        found = counter

    if 'СТОП' in row:
        break

print(found)
