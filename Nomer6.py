for b in range(11):
    for k in range(21):
        t = 100 - b - k
        if t >= 0:
            c = 10 * b + 5 * k + 0.5 * t
            if c == 100:
                print(f"Быков = {b}, Коров = {k}, Телят = {t}")