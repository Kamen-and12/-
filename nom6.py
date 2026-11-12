c = int(input("Количество колонок = "))
r = int(input("Количество рядов = "))
for r in range(1, r + 1):
    for c in range(1, c + 1):
        print(f"{c / r: .1f}", end=" ")
    print()