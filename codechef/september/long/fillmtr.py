t = int(input())
while t:
    t -= 1
    n, q = map(int, input().split())
    d = {}
    a = []
    ans = True
    for x in range(q):
        i, j, val = map(int, input().split())
        if j < i:
            i, j = j, i
        if (i, j) in d and d[(i, j)] != val:
            ans = False
        if (j, i) in d and d[(j, i)] != val:
            ans = False
        if i == j and val != 0:
            ans = False
        d[(i, j)] = val
        d[(j, i)] = val
        a.append((i, j))
    if ans:
        #print(d)
        #a.sort()
        #print(a)
        ans = False
        for x in range(q-1):
            for y in range(x+1, q):
                print(a[x], a[y])
                if a[x][0] == a[y][0]:
                    if (a[x][1], a[y][1]) not in d:
                        d[(a[x][1], a[y][1])] = abs(d[a[x]] - d[a[y]])
                        d[(a[y][1], a[x][1])] = abs(d[a[x]] - d[a[y]])
                    else:
                        if abs(d[a[x]] - d[a[y]]) != d[(a[x][1], a[y][1])]:
                            break
                elif a[x][0] == a[y][1]:
                    if (a[x][1], a[y][0]) not in d:
                        d[(a[x][1], a[y][0])] = abs(d[a[x]] - d[a[y]])
                        d[(a[y][0], a[x][1])] = abs(d[a[x]] - d[a[y]])
                    else:
                        if abs(d[a[x]] - d[a[y]]) != d[(a[x][1], a[y][0])]:
                            break
                elif a[x][1] == a[y][0]:
                    if (a[x][0], a[y][1]) not in d:
                        d[(a[x][0], a[y][1])] = abs(d[a[x]] - d[a[y]])
                        d[(a[y][1], a[x][0])] = abs(d[a[x]] - d[a[y]])
                    else:
                        if abs(d[a[x]] - d[a[y]]) != d[(a[x][0], a[y][1])]:
                            break
                elif a[x][1] == a[y][1]:
                    if (a[x][0], a[y][0]) not in d:
                        d[(a[x][0], a[y][0])] = abs(d[a[x]] - d[a[y]])
                        d[(a[y][0], a[x][0])] = abs(d[a[x]] - d[a[y]])
                    else:
                        if abs(d[a[x]] - d[a[y]]) != d[(a[x][0], a[y][0])]:
                            break
            else:
                continue
            break
        else:
            ans = True
    if ans:
        print('yes')
    else:
        print('no')




