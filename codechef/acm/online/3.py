from __future__ import division
from sys import stdin

for i in range(int(stdin.readline())):
    n, k = map(int, stdin.readline().split())
    ans = 0
    if n == 1:
        ans = 2*k
    else:
        t1 = n - 1
        c = 2
        ans = 2
        while t1 > 0:
            ans += 2 * c * ((k-1)**(c-1)) * t1
            t1 -= 1
            c += 1
        ans /= (k**(n-1))
    print(ans)