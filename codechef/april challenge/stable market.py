import math
from sys import stdin, stdout
import collections
t = int(stdin.readline())
while t:
    t -= 1
    (n, q) = map(int, stdin.readline().split())
    stock = [-1] + list(map(int, stdin.readline().split()))
    block_size = int(math.sqrt(n))
    queries = {}
    index = {}
    h = []
    dq = collections.deque()
    dq.append(1)
    k_d = [0]*(n+1)
    k_d[1] = 1
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
            if stock[mo_right] != stock[mo_right-1]:
                dq.append(1)
                k_d[1] += 1
            else:
                temp = dq.pop()
                dq.append(temp+1)
                k_d[temp+1] += 1

        while mo_left < l:
            mo_left += 1
            temp = dq.popleft()
            k_d[temp] -= 1
            if temp > 1:
                dq.appendleft(temp-1)

        while mo_right > r:
            mo_right -= 1
            temp = dq.pop()
            k_d[temp] -= 1
            if temp > 1:
                dq.append(temp-1)

        while mo_left > l:
            mo_left -= 1
            if stock[mo_left] != stock[mo_left+1]:
                dq.appendleft(1)
                k_d[1] += 1
            else:
                temp = dq.popleft()
                dq.appendleft(temp+1)
                k_d[temp+1] += 1
        queries[(l, r, k)] = k_d[k]
    for z in range(q):
        stdout.write(str(queries[index[z]]))
        stdout.write('\n')
