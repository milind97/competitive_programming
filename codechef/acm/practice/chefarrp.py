t = int(input())
while t:
    t -= 1
    n = int(input())
    a = list(map(int, input().split()))
    count = n
    for x in range(n-1):
        sv = a[x]
        mv = a[x]
        for y in range(x+1, n):
            sv += a[y]
            mv *= a[y]
            if sv == mv:
                count += 1
    print(count)




