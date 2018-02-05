t = int(input())
while t:
    t -= 1
    n = int(input())
    tp = (n - 92681)//2
    if n % 2 != 0:
        a = [1 for i in range(tp)] + list(range(1, 92682)) + [1 for i in range(tp)]
    else:
        a = [1 for i in range(tp+1)] + list(range(1, 92682)) + [1 for i in range(tp)]
    for i in a:
        print(i, end=' ')
    print()

