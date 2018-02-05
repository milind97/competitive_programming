from math import sqrt
from sys import stdin, stdout
import collections
t = int(stdin.readline())
while t:
    t -= 1
    (n, q) = map(int, stdin.readline().split())
    stock = [-1] + list(map(int, stdin.readline().split()))
    block_size = int(sqrt(n))
    queries = {}
    index = {}
    k_d = collections.defaultdict(int)
    k_d[stock[1]] = 1
    h = []
    ans = [0]*(n+2)
    ans[1] = 1
    (mo_left, mo_right) = (1, 1)
    for i in range(q):
        (l, r, k) = tuple(map(int, stdin.readline().split()))
        queries[(l, r, k)] = -1
        index[i] = (l, r, k)
        h.append((l//block_size, r, k, l))
    for hy in sorted(h):
        (r, k, l) = hy[1:]
        while mo_right < r:
            mo_right += 1
            temp = k_d[stock[mo_right]]
            k_d[stock[mo_right]] += 1
            ans[temp+1] += 1

        while mo_left < l:
            mo_left += 1
            temp = k_d[stock[mo_left-1]]
            k_d[stock[mo_left-1]] -= 1
            ans[temp] -= 1

        while mo_right > r:
            mo_right -= 1
            temp = k_d[stock[mo_right+1]]
            ans[temp] -= 1
            k_d[stock[mo_right+1]] -= 1

        while mo_left > l:
            mo_left -= 1
            temp = k_d[stock[mo_left]]
            k_d[stock[mo_left]] += 1
            ans[temp + 1] += 1

        queries[(l, r, k)] = ans[1] - ans[k+1]
    for z in range(q):
        stdout.write(str(queries[index[z]]))
        stdout.write('\n')
