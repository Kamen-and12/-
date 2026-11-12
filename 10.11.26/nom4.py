n = int(input())
a = 1
for i in range (1,n+1):
    for j in range (1,i+1):
        if a <= n:
            print(a, end=" ")
            a += 1
    print()
    if a > n:
        break