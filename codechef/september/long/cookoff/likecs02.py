t = int(input())
while t:
    t -= 1
    n = int(input())
    if n % 2 == 0:
        l = n - n//2 + 1
    else:
        l = n - n//2
    r = n + n//2 + 1
    for i in range(l, r):
        print(i, end=' ')
    print()