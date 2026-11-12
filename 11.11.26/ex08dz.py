c = 0 #общее число строк с котом
f = -1 #если кот не встретится 
l= 0 #начальное значение линии
while True:
    a = input()
    if a == "СТОП":
        break
    l += 1
    if "кот" in a or "Кот" in a:
        c += 1
        if f == -1:
            f = l
print(c, f)