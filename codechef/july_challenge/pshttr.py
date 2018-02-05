from sys import stdin


def blsearch(a, num):
    high = len(a) - 1
    low = 0
    if not a:
        return -1
    if num < a[0]:
        return -1
    if num > a[high]:
        return high

    while high >= low:
        if high - low <= 1:
            if a[high] <= num:
                return high
            else:
                return low
        midval = (low+high) // 2
        if a[midval] > num:
            high = midval - 1
        else:
            low = midval
    return -1


def main():
    n = int(stdin.readline())
    d = {i: {} for i in range(1, n+1)}
    start = True
    for i in range(n-1):
        u, v, c = map(int, stdin.readline().strip().split())
        if start:
            root = u
            start = False
        d[u][v] = c
        d[v][u] = c
    if start:
        start = []
    else:
        start = [root]
    #start = [3]
    xor_arr = [[]]*(n+1)
    cum_xor = [[]]*(n+1)
    check = set()
    while start:
        x = start.pop()
        check.add(x)
        for z in d[x].keys():
            if z in check:
                continue
            xor_arr[z] = xor_arr[x] + [d[x][z]]
            start.append(z)
            xor_arr[z].sort()
            for j in range(len(xor_arr[z])):
                if j == 0:
                    cum_xor[z] = [xor_arr[z][j]]
                else:
                    #print(xor_arr[z][j-1], xor_arr[z][j])
                    cum_xor[z].append(cum_xor[z][j-1] ^ xor_arr[z][j])
    #print(xor_arr)
    #print(cum_xor)
    m = int(stdin.readline())
    for k in range(m):
        u, v, k = map(int, stdin.readline().strip().split())
        t1 = blsearch(xor_arr[u], k)
        t2 = blsearch(xor_arr[v], k)
        #print(t1, t2)
        if t1 == -1:
            t1 = 0
        else:
            t1 = cum_xor[u][t1]
        if t2 == -1:
            t2 = 0
        else:
            t2 = cum_xor[v][t2]
        print(t1 ^ t2)


if __name__ == "__main__":
    t = int(stdin.readline())
    while t:
        t -= 1
        main()
