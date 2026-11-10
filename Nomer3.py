n = int(input("Периоды деления (по 3ч) = "))
a = 1
for i in range (1, n+1):
    a *= 2
    print(f"Через {3 * i} часов будет {a} амеб")