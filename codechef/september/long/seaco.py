from sys import stdin
from itertools import accumulate


def nextpower(x):
    count = 0
    while x > 0:
        count += 1
        x >>= 1
    return 1 << count


def construct_tree(ar, seg, low, high, pos):
    if low == high:
        seg[pos] = count[low]
        return
    mid = (low + high) // 2
    construct_tree(ar, seg, low, mid, 2 * pos + 1)
    construct_tree(ar, seg, mid + 1, high, 2 * pos + 2)
    seg[pos] = 0


def traverse(seg, node, low, high, pos):
    if low == high and low == node:
        return seg[pos]
    mid = (low+high) // 2
    if seg[pos] != 0:
        seg[2*pos+1] += seg[pos]
        seg[2*pos+2] += seg[pos]
        seg[pos] = 0
    if node > mid:
        return traverse(seg, node, mid+1, high, 2*pos+2)
    else:
        return traverse(seg, node, low, mid, 2*pos+1)


def count_query(seg, qlow, qhigh, low, high, pos, val):
    if qlow <= low and qhigh >= high:
        seg[pos] += val
        return
    if qlow > high or qhigh < low:
        return
    mid = (low+high)//2
    seg[2*pos+1] += seg[pos]
    seg[2*pos+2] += seg[pos]
    seg[pos] = 0
    count_query(seg, qlow, qhigh, low, mid, 2*pos+1, val)
    count_query(seg, qlow, qhigh, mid+1, high, 2*pos+2, val)

mod = 10 ** 9 + 7
T = int(stdin.readline())
while T:
    T -= 1
    n, m = map(int, stdin.readline().split())
    a = []
    for i in range(m):
        a.append(tuple(map(int, stdin.readline().split())))
    count = [1] * m
    if m & (m - 1) == 0:
        seg = [0] * (2 * m - 1)
    else:
        seg = [0] * (2 * nextpower(m) - 1)
    construct_tree(count, seg, 0, m - 1, 0)
    for index, query in enumerate(reversed(a)):
        count[m-index-1] = traverse(seg, m-index-1, 0, m-1, 0)
        if query[0] == 2:
            count_query(seg, query[1]-1, query[2]-1, 0, m-1, 0, count[m-index-1])
            #print(seg)
    ans = [0] * (n + 1)
    for index, query in enumerate(a):
        if query[0] == 1:
            ans[query[1] - 1] += count[index]
            ans[query[2]] -= count[index]
    ans = list(accumulate(ans))[:-1]
    for i in ans:
        print(i % mod, end=" ")
    print()
