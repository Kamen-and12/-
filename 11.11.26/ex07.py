n = int(input("Количество команд ="))
w = "Евразия" #война
p = "Остазия" #мир
for _ in range(n):
    c = input("Введите команду = ")
    if c == "С кем война?":
        print(w)
    elif c == "С кем мир?":
        print(p)
    elif c == "Меняем":
        w, p = p, w