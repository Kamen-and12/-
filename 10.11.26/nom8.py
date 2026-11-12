h = int(input("Введите высоту = "))
w = int(input("Введите ширину = "))
c = input("Введите символ = ")
for i in range(h):
    if i == 0 or i == h - 1:
        print(c * w)
    else:
        print(c + " " * (w - 2) + c)