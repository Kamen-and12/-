import itertools
counter = 0

for i in itertools.count():
    row = input('Введите строку: ')

    counter += 1

    if 'Кот' in row or 'кот' in row:
        print(counter)
        break

    if 'СТОП' in row:
        print(-1)
        break
