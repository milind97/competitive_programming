t = int(input())
while t:
    t -= 1
    n, k = map(int, input().split())
    pos = k
    k = 0
    while n-k >= 2:
        t1 = pow(2, n-k)
        temp = pos // t1
        t2 = pos % t1
        if t2 % 2 == 0:
            pos = temp*t1 + t2//2
        else:
            pos = temp*t1 + t1//2 + (t2-1)//2
        k += 1
        #print('pos:', pos)
    print(pos)

