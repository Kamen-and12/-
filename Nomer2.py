S = int(input("Количество дней = "))
a = 0
b = 10
for day in range (S):
    a += b
    b *= 1.1
print(f"Дистанция за {S} дней = {a: .3f} км")