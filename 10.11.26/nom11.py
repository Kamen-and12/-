budget = int(input("Введите выделенные субсидии (Тыс. рублей) = "))
g = int(input("Введите нужное количество голов = "))
for b in range(1, budget // 20 + 1):
    for c in range(0, budget // 10 + 1):
        t = g - b - c
        if t >= 0 and b * 20 + c * 10 + t * 5 == budget:
            print(f" Куплено: Быков = {b}, Коров = {c}, Телят = {t}")