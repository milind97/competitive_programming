from sys import stdin, stdout


def solve_query(start, end, low, high, pos):
    global coin, lazy
    if high < low:
        return
    if lazy[pos] != 0:
        coin[pos] = (high - low + 1) - coin[pos]
        if low != high:
            lazy[2 * pos + 1] = int(not lazy[2 * pos + 1])
            lazy[2 * pos + 2] = int(not lazy[2 * pos + 2])
        lazy[pos] = 0
    if start <= low and end >= high:
        return coin[pos]
    elif start > high or end < low:
        return 0
    else:
        mid = (low+high)//2
        return solve_query(start, end, low, mid, 2*pos + 1) + solve_query(start, end, mid+1, high, 2*pos + 2)


def update_tree(start, end, low, high, pos):
    global coin, lazy
    if high < low:
        return
    if lazy[pos] != 0:
        coin[pos] = (high - low + 1) - coin[pos]
        if low != high:
            lazy[2 * pos + 1] = int(not lazy[2 * pos + 1])
            lazy[2 * pos + 2] = int(not lazy[2 * pos + 2])
        lazy[pos] = 0

    if start <= low and end >= high:
        coin[pos] = (high - low + 1) - coin[pos]
        if low != high:
            lazy[2 * pos + 1] = int(not lazy[2 * pos + 1])
            lazy[2 * pos + 2] = int(not lazy[2 * pos + 2])
    elif start > high or end < low:
        return
    else:
        mid = (low+high)//2
        update_tree(start, end, low, mid, 2*pos + 1)
        update_tree(start, end, mid+1, high, 2*pos + 2)
        coin[pos] = (coin[2*pos + 1] + coin[2*pos + 2])

n, q = map(int, stdin.readline().split())
coin = [0]*1000000
lazy = [0]*1000000
for i in range(q):
    flag, a, b = map(int, stdin.readline().split())
    if flag == 1:
        stdout.write(str(solve_query(a, b, 0, n-1, 0)))
        stdout.write('\n')
    else:
        update_tree(a, b, 0, n-1, 0)
