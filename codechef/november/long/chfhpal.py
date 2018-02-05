st = 'abcdefghijklmnopqrstuvwxyz'
s0 = 'aabb'
s1 = 'aaababbb'
s2 = 'aababb'

for i in range(int(input())):
    n, a = map(int, input().split())
    if a == 1:
        print(n, 'a'*n)
    elif a == 2:
        if n == 1:
            print(1, 'a')
        elif n == 2:
            print(1, 'ab')
        elif n == 3 or n == 4:
            print(2, s0[:n])
        elif 4 < n < 9:
            print(3, s1[:n])
        else:
            print(4, s2*(n//6) + s2[:(n % 6)])
    else:
        s = st[:a]
        print(1, s*(n//a) + s[:(n % a)])
    #print(st, s0, s1, s2)



