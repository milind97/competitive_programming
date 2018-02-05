import math
t = int(input())
while(t):
    t -= 1
    n = int(input())
    a = []
    for i in range(n):
        a.append([])
        a[i] = list(map(int, input().split()))
    c0 = 0
    for i in range(n):
        for j in range(n):
            if a[i][j] == 0:
                c0 += 1
    print(n - 1 - int((math.sqrt(1+(4*c0)) - 1) // 2))
