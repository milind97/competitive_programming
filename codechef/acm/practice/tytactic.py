import collections


def nextpower(x):
    count = 0
    while x > 0:
        count += 1
        x >>= 1
    return 1 << count


def dfs(node, d, mp, time, rng):
    x = time
    mp[node] = time
    for v in d[node]:
        x = dfs(v, d, mp, x+1, rng)
    rng[node-1] = (time, x)
    return x


def construct_tree(inpt, seg, low, high, pos):
    if low == high:
        seg[pos] = inpt[low]
        return
    mid = (low+high) // 2
    construct_tree(inpt, seg, low, mid, 2*pos+1)
    construct_tree(inpt, seg, mid+1, high, 2*pos+2)
    seg[pos] = seg[2*pos + 1] + seg[2*pos + 2]


def rangequery(seg, qlow, qhigh, low, high, pos):
    if qlow <= low and qhigh >= high:
        return seg[pos]
    if qlow > high or qhigh < low:
        return 0
    mid = (low + high) // 2
    return rangequery(seg, qlow, qhigh, low, mid, 2 * pos + 1) + rangequery(seg, qlow, qhigh, mid + 1, high, 2 * pos + 2)


def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    d = collections.defaultdict(list)
    mp = {}
    for i in range(n-1):
        x, y = map(int, input().split())
        d[x].append(y)
    rng = [()]*n
    dfs(1, d, mp, 1, rng)
    if n & n - 1 == 0:
        seg = [0] * (2 * n - 1)
    else:
        seg = [0] * (2 * nextpower(n) - 1)
    arr = [0]*n
    print(d)
    print(mp)
    print(rng)
    print(seg)
    for i in range(1, n+1):
        arr[mp[i] - 1] = a[i - 1]
    print(arr)
    construct_tree(arr, seg, 0, n - 1, 0)

    for i in range(m):
        temp = list(input().split())
        if len(temp) == 2:
            t1 = int(temp[1]) - 1
            x, y = rng[t1]
            print(x, y, t1)
            print(rangequery(seg, x-1, y-1, 0, n-1, 0))


if __name__ == '__main__':
    main()
