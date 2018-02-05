for i in range(int(input())):
    n, k = map(int, input().split())
    if k <= 2:
        print('impossible')
    else:
        print(('a' + 'b'*(k - 2) + 'a')*(n // k))
