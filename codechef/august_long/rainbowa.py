k = int(input())
while k:
    k -= 1
    n = int(input())
    a = list(map(int, input().split()))
    t = 0
    f = False
    if n % 2 == 0:
        l = n//2
    else:
        l = n//2 + 1
    for i in range(l):
        if a[i] == t + 1:
            t += 1
        elif a[i] == t:
            continue
        else:
            f = True
            break
    if f or t != 7:
        print('no')
    else:
        if a == a[::-1]:
            print('yes')
        else:
            print('no')



