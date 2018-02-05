t = int(input())
while t:
    t -= 1
    n, p =  map(int, input().split())
    a = list(map(int, input().split()))
    x = p//2
    y = p//10
    cx = cy = 0
    for i in a:
        if i >= x:
            cx += 1
        elif i <= y:
            cy += 1
    if cy == 2and cx == 1:
        print('yes')
    else:
        print('no')