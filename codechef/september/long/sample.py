from sys import stdin
t = int(stdin.readline())
while t:
    t -= 1
    n, q = map(int, stdin.readline().split())
    d = {}
    a = [-1]*(n+1)
    a[1] =  0
    ans = True
    for x in range(1, n+1):
        d[(x, x)] = 0
    for x in range(q):
        i, j, val = map(int, stdin.readline().split())
        if j < i:
            i, j = j, i
        if (i, j) in d and d[(i, j)] != val:
            ans = False
        if (j, i) in d and d[(j, i)] != val:
            ans = False
        d[(i, j)] = val
        d[(j, i)] = val
        #a.append((i, j))
    #print('before', d)
    if ans:
        #print(d)
        #a.sort()
        #print(a)
        ans = False
        for x in range(1, n):
            for y in range(x+1, n+1):
                if (x, y) in d:
                    if a[x] != -1 and a[y] != -1 and d[(x, y)] != abs(a[y] - a[x]):
                        break
                    elif a[x] == -1 and a[y] != -1:
                        a[x] = abs(a[y] - d[(x, y)])
                    elif a[y] == -1 and a[x] != -1:
                        a[y] = abs(a[x] - d[(x, y)])
            else:
                continue
            break
        else:
            ans = True
    print(a)
    if ans:
        print('yes')
    else:
        print('no')