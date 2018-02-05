from sys import stdin


def nextpower(x):
    count = 0
    while x > 0:
        count += 1
        x >>= 1
    return 1 << count


def find_minmax(a, b):
    return min(a[0], b[0]), max(a[1], b[1])


def construct_tree(input, seg, low, high, pos):
    if low == high:
        seg[pos] = (input[low], input[low])
        return
    mid = (low+high) // 2
    construct_tree(input, seg, low, mid, 2*pos+1)
    construct_tree(input, seg, mid+1, high, 2*pos+2)
    seg[pos] = find_minmax(seg[2*pos + 1], seg[2*pos + 2])


def query(seg, qlow, qhigh, low, high, pos):
    if qlow <= low and qhigh >= high:
        return seg[pos]
    if qlow > high or qhigh < low:
        return 0, 0
    mid = (low+high) // 2
    return find_minmax(query(seg, qlow, qhigh, low, mid, 2*pos+1), query(seg, qlow, qhigh, mid+1, high, 2*pos+2))


def main():
    n, q = map(int, stdin.readline().split())
    arr = list(map(int, stdin.readline().split()))
    if n & n-1 == 0:
        seg = [0]*(2*n - 1)
    else:
        seg = [0]*(2*nextpower(n) - 1)
    construct_tree(arr, seg, 0, n-1, 0)
    for i in range(q):
        a, b, c, d = map(int, stdin.readline().split())
        if a <= c <= b:
            a1 = list(sorted(arr[a-1:c-1]))
            a2 = list(sorted(arr[b:d]))
            x, y = query(seg, c-1, b-1, 0, n-1, 0)
            l = 0
            r = d-b-1
            check = True
        elif c <= a <= d:
            a1 = list(sorted(arr[c - 1:a - 1]))
            a2 = list(sorted(arr[d:b]))
            x, y = query(seg, a-1, d-1, 0, n-1, 0)
            l = 0
            r = b-d-1
            check = True
        else:
            a1 = list(sorted(arr[a - 1:b]))
            a2 = list(sorted(arr[c - 1:d]))
            l = 0
            r = b - a
            check = False
        flag = 0
        while r >= l and flag < 2:
            if a1[l] != a2[l]:
                if check:
                    if (a1[l] < x and a2[l] < x) or (a1[l] > y and a2[l] > y):
                        flag += 1
                    elif (a1[l] == x and a2[l] != y) or (a2[l] == x and a1[l] != y):
                        flag += 1
                    elif (a1[l] == y and a2[l] != x) or (a2[l] == y and a1[l] != x):
                        flag += 1
                    elif (a1[l] == x and a2[l] == y) or (a2[l] == x and a1[l] == y):
                        flag += 0
                    else:
                        flag += 2
                else:
                    flag += 1
            if a1[r] != a2[r] and l != r:
                if check:
                    if (a1[r] <= x and a2[r] <= x) or (a1[r] >= y and a2[r] >= y):
                        flag += 1
                    elif (a1[r] == x and a2[r] != y) or (a2[r] == x and a1[r] != y):
                        flag += 1
                    elif (a1[r] == y and a2[r] != x) or (a2[r] == y and a1[r] != x):
                        flag += 1
                    elif (a1[r] == x and a2[r] == y) or (a2[r] == x and a1[r] == y):
                        flag += 0
                    else:
                        flag += 2
                else:
                    flag += 1
            l += 1
            r -= 1
        if flag >= 2:
            print('NO')
        else:
            print('YES')

if __name__ == '__main__':
    t = int(stdin.readline())
    while t:
        t -= 1
        main()
