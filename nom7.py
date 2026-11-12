n = int(input("Введите число = "))
total = 0
for i in range(1, n + 1):
    p = 0
    for j in range(i, 0, -2):
        p += j
    total += i ** p
print(f"Сумма = {total}")