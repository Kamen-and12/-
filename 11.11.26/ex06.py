import itertools

additive = 0
counter = 0

found = False
local_counter = 0

for i in itertools.count():
    value = int(input('Введите число: '))

    if value == 0:
        break

    additive += value
    counter += 1

    if additive == 10 and found == False:
        found = True
        local_counter = counter

print(local_counter)
        