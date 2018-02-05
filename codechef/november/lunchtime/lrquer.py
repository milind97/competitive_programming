import bisect


def nextpower(x):
    count = 0
    while x > 0:
        count += 1
        x >>= 1
    return 1 << count


def merge(a, b):
    final = [0]*(len(a) + len(b))
    i = j = k = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            final[k] = a[i]
            i += 1
        else:
            final[k] = b[j]
            j += 1
        k += 1
    while i < len(a):
        final[k] = a[i]
        k += 1
        i += 1
    while j < len(b):
        final[k] = b[j]
        k += 1
        j += 1
    return final


def update(seg, low, high, index, val, pos):
    if low == high and low == index:
        x = seg[pos][0]
        seg[pos] = [val]
        return x
    mid = (low + high) // 2
    if mid >= index:
        x = update(seg, low, mid, index, val, 2*pos + 1)
    else:
        x = update(seg, mid+1, high, index, val, 2*pos + 2)
    del(seg[pos][bisect.bisect_left(seg[pos], x)])
    bisect.insort(seg[pos], val)
    return x


def closest(a, val):
    index = bisect.bisect_left(a, val)
    if index == len(a):
        return a[index-1]
    elif a[index] == val or index == 0 or a[index] - val >= val - a[index-1]:
        return a[index]
    else:
        return a[index-1]


def query(arr, seg, qlow, qhigh, low, high, pos):
    x = (arr[qlow] + arr[qhigh]) // 2
    if qlow <= low and qhigh >= high:
        return closest(seg[pos], x)
    if qlow > high or qhigh < low:
        return 10**9 + 1
    mid = (low + high) // 2
    y = query(arr, seg, qlow, qhigh, low, mid, 2*pos + 1)
    z = query(arr, seg, qlow, qhigh, mid+1, high, 2*pos + 2)
    if abs(x-y) > abs(x-z):
        return z
    else:
        return y


def construct_tree(arr, seg, low, high, pos):
    if low == high:
        seg[pos] = [arr[low]]
        return
    mid = (low+high) // 2
    construct_tree(arr, seg, low, mid, 2*pos+1)
    construct_tree(arr, seg, mid+1, high, 2*pos+2)
    seg[pos] = merge(seg[2*pos + 1], seg[2*pos + 2])


def main():
    for _ in range(int(input())):
        n, q = map(int, input().split())
        a = list(map(int, input().split()))
        if n & n - 1 == 0:
            seg = [0] * (2 * n - 1)
        else:
            seg = [0] * (2 * nextpower(n) - 1)
        construct_tree(a, seg, 0, n-1, 0)
        #print(seg)
        for i in range(q):
            t, l, r = map(int, input().split())
            if t == 1:
                ans = query(a, seg, l-1, r-1, 0, n-1, 0)
                print((ans-a[l-1]) * (a[r-1]-ans))
            else:
                a[l-1] = r
                update(seg, 0, n - 1, l-1, r, 0)
                #print(seg)


if __name__ == '__main__':
    main()
    #a = [1, 3, 6, 7]
    #print(closest(a, 8))
