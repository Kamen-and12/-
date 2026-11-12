n = int(input("Введите число = "))
for num in range(2, n):
    i = True
    for d in range(2, int(num ** 0.5) + 1):
        if num % d == 0:
            i = False
            break
    if i:
        print(num)