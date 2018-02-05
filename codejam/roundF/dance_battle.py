t = int(input())
for i in range(1, t+1):
    e, n = map(int, input().split())
    a = list(map(int, input().split()))
    h = 0
    idx = 0
    a.sort()
    while a and idx < len(a):
        if e > a[idx]:
            e -= a[idx]
            h += 1
            idx += 1
        elif h > 0 and idx != len(a)-1:
            e += a[-1]
            h -= 1
            del(a[-1])
        else:
            idx += 1
    print("Case #{}: {}".format(i, h))


















