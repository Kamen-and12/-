n = int(input())
a = 0
b = 0
for i in range (1,n+1):
    k = int(input())
    h = 100000
    for j in range (k):
        t = int(input())
        if t < h:
            h = t
    if h > a:
        a = h
        b = i
print(b,a)