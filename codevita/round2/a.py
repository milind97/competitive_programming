def cal(n, base):
    if n >= base:
        return ((2 * (base ** 3) + 2 * (base ** 2) + (base ** 2) + base) // 6) + n - base
    else:
        return cal(base, base) - cal(base-n, base-n)


t = int(input())
while t:
    t -= 1
    n, b = map(int, input().split())
    a = list(map(int, input().split()))
    if n % 2 == 0:
        l = r = n//2
    else:
        l = n//2 + 1
        r = n//2
    maxval = 0
    pos = -1
    for i in range(l):
        if a[i] > maxval:
            maxval = a[i]
            pos = i
    t1 = maxval + l - pos - 1
    maxval = 0
    pos = -1
    for i in range(r, n):
        if a[i] > maxval:
            maxval = a[i]
            pos = i
    t2 = maxval + pos - r
    #print('t1, t2:', t1, t2)
    midval = max(t1, t2)
    mincost = 0
    count = 0
    for i in range(midval - l + 1, midval + 1):
        #print('fd', i-a[count])
        mincost += cal(i - a[count], b)
        #print(mincost)
        count += 1
    if n % 2 == 0:
        for j in range(midval, midval-r, -1):
            mincost += cal(j - a[count], b)
            count += 1
    else:
        for j in range(midval - 1, midval - r - 1, -1):
            mincost += cal(j - a[count], b)
            count += 1
    #print(count)
    print(mincost*1000)




