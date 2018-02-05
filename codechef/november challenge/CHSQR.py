t = int(input())
while(t):
    t -= 1
    k = int(input())
    a = {}
    for i in range(1, k+1):
        a[i] = {}
        for j in range(1, k+1):
            a[i][j] = 0
    x = (k+1)//2
    a[x][x] = k
    a[1][x] = 1
    a[x][1] = 1
    num = 0
    while(num<=k):
        num += 1
        for i in range(1, k+1):
            if num in a[i].values():
                pass
            else:
                for j in range(1, k+1):
                    if a[i][j] == 0:
                        for z in range(1, k+1):
                            if a[z][j] == num:
                                break
                        else:
                            a[i][j] = num
                            break
    for i in range(1, k + 1):
        for j in range(1, k + 1):
            print(a[i][j], end=" ")
        print()



