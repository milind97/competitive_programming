from sys import stdin, stdout


def construct_tree(inpt, coin, low , high, pos):
    if low == high:
        coin[pos] = inpt[low]
        return
    mid = (low+high) // 2
    construct_tree(inpt, coin, low, mid, 2*pos + 1)
    construct_tree(inpt, coin, mid+1, high, 2*pos + 2)
    coin[pos] = coin[2+pos + 1] + coin[2*pos + 2]


def solve_query(coin, lazy, start, end, low, high, pos):
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
        mid = (low + high) // 2
        return solve_query(coin, lazy, start, end, low, mid, 2 * pos + 1) + solve_query(coin, lazy, start, end, mid + 1,
                                                                                        high, 2 * pos + 2)


def update_tree(coin, lazy, start, end, low, high, pos):
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
        mid = (low + high) // 2
        update_tree(coin, lazy, start, end, low, mid, 2 * pos + 1)
        update_tree(coin, lazy, start, end, mid + 1, high, 2 * pos + 2)
        coin[pos] = (coin[2 * pos + 1] + coin[2 * pos + 2])


def main():
    n, m = map(int, stdin.readline().split())
    inpt = list(map(int, stdin.readline().split()))
    coin = [0] * 1000000
    lazy = [0] * 1000000
    construct_tree(inpt, coin, 0, n-1, 0)
    for i in range(m):
        q = list(map(int, stdin.readline().split()))
        if len(q) == 3:
            update_tree(coin, lazy, q[1] - 1, q[1] - 1, q[2])

if __name__ == "__main__":
    main()
