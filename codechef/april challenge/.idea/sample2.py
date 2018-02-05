from itertools import groupby
from operator import itemgetter

M = 2 ** 17
B = [0] * (M + 1)


def reset():
    global B
    B = [0] * (M + 1)


def update(idx, val):
    idx += 1
    while idx <= M:
        B[idx] += val
        idx += idx & -idx


def read(idx):
    r = 0
    idx += 1
    while idx > 0:
        r += B[idx]
        idx -= idx & -idx
    return r


for _ in range(int(input())):
    N, Q = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    q = [[0, i] + [int(x) for x in input().split()] for i in range(Q)]
    print(a)
    groups = []
    i = 0
    for (g, (_, l)) in enumerate(groupby(a)):
        j = i
        gc = len(groups)
        for _ in l:
            a[j] = gc
            j += 1
        groups.append([1, gc, i, j - 1, j - i])
        i = j
    print(groups)
    print(a)
    reset()
    q.extend(groups)
    q.sort(key=itemgetter(4, 0), reverse=True)
    print(q)
    for x in q:
        print("X ; ", x)
        if x[0]:
            update(x[1], 1)
        else:
            y, z = a[x[2] - 1] + 1, a[x[3] - 1] - 1
            r = read(z) - read(y - 1) if z >= y else 0
            if z + 1 == y - 1:
                if x[3] - x[2] + 1 >= x[4]:
                    r += 1
            else:
                if groups[y - 1][3] - x[2] + 1 + 1 >= x[4]:
                    r += 1
                if x[3] - 1 - groups[z + 1][2] + 1 >= x[4]:
                    r += 1
            x[-1] = r
    print(q)
    for x in sorted(x for x in q if x[0] == 0):
        print(x[-1])