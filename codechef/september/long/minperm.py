t = int(input())
while t:
    t -= 1
    n = int(input())
    a = list(range(1, n+1))
    if n % 2 == 0:
        for i in range(0, n-1, 2):
            a[i], a[i+1] = a[i+1], a[i]
    else:
        for i in range(0, n-2, 2):
            a[i], a[i+1] = a[i+1], a[i]
        a[-2], a[-1] = a[-1], a[-2]
    for x in a:
        print(x, end=" ")
    print()

