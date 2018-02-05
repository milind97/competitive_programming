t = int(input())
while t:
    t -= 1
    n, v1, v2 = map(int, input().split())
    t1 = (2*n) / v2
    t2 = (pow(2, 0.5)*n) / v1
    if t1 < t2:
        print('Elevator')
    else:
        print('Stairs')