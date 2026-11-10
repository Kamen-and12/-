import math
k = float(input("Длина палки (больше 3) = "))
h = float(input("Шаг = "))
y = 2
while y <= 3:
    if y <= k:
        alpha_rad = math.acos(y / k)
        alpha_deg = math.degrees(alpha_rad)
        print(f"При y = {y: .2f} м, угол a = {alpha_deg: .2f} градусов")
    else:
        print(f"При y = {y: .2f} м, угол не найден (y > x)")
    y += h