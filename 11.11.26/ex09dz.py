tx = int(input("Введите координату x = "))
ty = int(input("Введите координату y = "))
x, y = 0, 0
c = 0
f = -1
if x == tx and y == ty:
    f = 0
while True:
    d = input()
    if d == "стоп":
        break
    steps = int(input())
    c += 1
    if d == "юг":
        y -= steps
    elif d == "север":
        y += steps
    elif d == "запад":
        x -= steps
    elif d == "восток":
        x += steps
    if f == -1 and x == tx and y == ty:
        f = c
print(f)