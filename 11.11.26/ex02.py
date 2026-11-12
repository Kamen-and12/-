rows = int(input('Введите количество строк: '))

found = False

for i in range(rows):
    row = input('Введите строку: ')

    if 'Кот' in row or 'кот' in row:
        found = True
        break

print('МЯУ' if found else 'НЕТ')
