from operator import itemgetter
import math
t = int(input())
for i in range(1, t+1):
    n, k = map(int, input().split())
    a = []
    for j in range(n):
        a.append(tuple(map(int, input().split())))
    a = sorted(a, key = itemgetter(0))
    b = sorted(a, key = lambda x: x[0]+x[1])[::-1]
    a = b[:]
    temp = n
    for index in range(n-1):
        if b[index] == b[index + 1] and k < temp:
            a.remove(b[index+1])
            temp -= 1
        elif k == temp:
            break
    p = math.pi
    ans = 0
    for c in range(k-1):
        ans += p*(a[c][0]**2 - a[c+1][0]**2) + 2*p*a[c][0]*a[c][1]
    ans += p*(a[k-1][0]**2) + 2*p*a[k-1][0]*a[k-1][1]
    print("Case #{}: {}".format(i, ans))