from sys import stdin


def bsearch(a, num, low, high):

    if high-low <= 1:
        if a[high] > num:
            if a[low] > num:
                return low-1
            else:
                return low
        else:
            return high
    mid = low + (high - low)//2
    if a[mid] > num:
        return bsearch(a, num, low, mid - 1)
    else:
        return bsearch(a, num, mid, high)


t = int(stdin.readline())
while t:
    t -= 1
    p, q, r = map(int, stdin.readline().strip().split())
    X = list(map(int, stdin.readline().strip().split()))
    Y = list(map(int, stdin.readline().strip().split()))
    Z = list(map(int, stdin.readline().strip().split()))
    X.sort()
    Z.sort()
    x1 = [0]*(p+1)
    z1 = [0]*(r+1)
    sum = 0
    for i in range(p):
        sum += X[i]
        x1[i] = sum
    sum = 0
    for i in range(r):
        sum += Z[i]
        z1[i] = sum
    c = 10**9 + 7
    summation = 0
    for i in range(q):
        nx = bsearch(X, Y[i], 0, p - 1)
        nz = bsearch(Z, Y[i], 0, r - 1)
        temp1 = ((nx + 1)*Y[i] + x1[nx]) % c
        temp2 = ((nz + 1)*Y[i] + z1[nz]) % c
        summation += (temp1 * temp2) % c
        summation %= c
    print(summation % c)
