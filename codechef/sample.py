def solve(a, mid):
    low = high = 0
    point = 0
    for x in range(len(a)):
        if a[x] < mid:
            low += mid - a[x]
        else:
            high += a[x] - mid
        if low != high:
            point = x
    print(point, low)
    if low == high:
        return low*(point+1)
    else:
        return -1


ar = list(map(int, input().split()))
print(solve(ar, sum(ar)//len(ar)))
