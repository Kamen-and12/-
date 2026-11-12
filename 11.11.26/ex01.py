a = int(input('Введите начальное число: '))
b = int(input('Введите конечное число: '))

def create():
    if a > b:
        print('Начальное число не может быть больше конечного')
        return

    for i in range(a, b + 1):
        if (i % 3 == 0) and (i % 5 == 0):
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)

create()