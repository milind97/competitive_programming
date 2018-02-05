maxv = 10**9 + 1
minv = -1
def nextpower(x):
    count = 0
    while x > 0:
        count += 1
        x >>= 1
    return 1 << count


def construct_tree(inpt, seg, low, high, pos):
    if low == high:
        seg[pos] = (inpt[low], inpt[low])
        return
    mid = (low+high) // 2
    construct_tree(inpt, seg, low, mid, 2*pos+1)
    construct_tree(inpt, seg, mid+1, high, 2*pos+2)
    seg[pos] = (min(seg[2*pos + 1][0], seg[2*pos + 2][0]), max(seg[2*pos + 1][1], seg[2*pos + 2][1]))


def rangequerymin(seg, qlow, qhigh, low, high, pos):
    if qlow <= low and qhigh >= high:
        return seg[pos][0]
    if qlow > high or qhigh < low:
        return maxv
    mid = (low + high) // 2
    return min(rangequerymin(seg, qlow, qhigh, low, mid, 2 * pos + 1), rangequerymin(seg, qlow, qhigh, mid + 1, high, 2 * pos + 2))


def rangequerymax(seg, qlow, qhigh, low, high, pos):
    if qlow <= low and qhigh >= high:
        return seg[pos][1]
    if qlow > high or qhigh < low:
        return minv
    mid = (low + high) // 2
    return max(rangequerymax(seg, qlow, qhigh, low, mid, 2 * pos + 1), rangequerymax(seg, qlow, qhigh, mid + 1, high, 2 * pos + 2))


def main():
    n = int(input())
    a = list(map(int, input().split()))
    if n & n-1 == 0:
        seg = [0]*(2*n - 1)
    else:
        seg = [0]*(2*nextpower(n) - 1)
    construct_tree(a, seg, 0, n-1, 0)
    ans = 0
    for i in range(n-1):
        
        print('A', 0, i)
        t1 = rangequerymax(seg, 0, i, 0, n-1, 0)
        print('t1', t1)
        t2 = 0
        for j in range(i+1, n):
            print(i+1, j)
            t2 += rangequerymin(seg, i+1, j, 0, n-1, 0)
            print('t2', t2)
        ans += t1*t2
    print(ans)


if __name__ == '__main__':
    main()