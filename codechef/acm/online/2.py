import math


for i in range(int(input())):
    n, s = map(int, input().split())
    if s == 0:
        a = [0]*n
        for j in a:
            print(j, end=' ')
        print()
    else:
        if n == 1:
            print(-1)
        else:
            t1 = s**2 * n
            if n % 2 == 0:
                t1 /= n
            else:
                t1 /= n-1
            t1 = math.sqrt(t1)
            if n % 2 == 0:
                a = [-t1]*(n//2) + [t1]*(n//2)
            else:
                a = [-t1]*(n//2) + [0] + [t1]*(n//2)
            for j in a:
                print(j, end=' ')
            print()
            #t2 = 0
            #for j in a:
            #    t2 += j**2
            #t2 = math.sqrt(t2/n)
            #print(t2)

