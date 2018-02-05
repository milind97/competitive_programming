for i in range(int(input())):
    n, r = map(int, input().split())
    a = list(map(int, input().split()))
    lv = 0
    hv = 10**9 + 1
    if a[0] > r:
        turn = 'l'
        hv = a[0]
    else:
        turn = 'r'
        lv = a[0]
    flag = False
    for j in range(1, n-1):
        if turn == 'l':
            if a[j] < lv or a[j] > hv:
                break
            else:
                if a[j] < r:
                    lv = a[j]
                    turn = 'r'
                else:
                    turn = 'l'
                    hv = a[j]
        if turn == 'r':
            if a[j] < lv or a[j] > hv:
                break
            else:
                if a[j] > r:
                    hv = a[j]
                    turn = 'l'
                else:
                    lv = a[j]
                    turn = 'r'
    else:
        flag = True
    if flag:
        print('YES')
    else:
        print('NO')





