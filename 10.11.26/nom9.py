n = int(input("Количество космических аппаратов = "))
for i in range(1, n + 1):
    for s in range(i - 1, -1, -1): #секунды
        print(f"Осталось секунд: {s}")
    print(f"Пуск {i}")