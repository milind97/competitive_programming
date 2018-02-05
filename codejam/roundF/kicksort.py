t = int(input())
for i in range(1, t+1):
    n = int(input())
    a = list(map(int, input().split()))
    flag = False
    ll = 1
    ul = n
    while len(a) >= 2:
        mid = (len(a)-1) // 2
        if a[mid] == ll:
            ll += 1
            del(a[mid])
        elif a[mid] == ul:
            ul -= 1
            del(a[mid])
        else:
            flag = True
            break
    if flag:
        print("Case #{}: {}".format(i, 'No'))
    else:
        print("Case #{}: {}".format(i, 'Yes'))

