t = int(input())
while t:
    t -= 1
    n, k = map(int, input().split())
    ans = set()
    index = -1
    for i in range(1, n+1):
        temp = set(list(map(int, input().split()))[1:])
        ans |= temp
        if len(ans) == k and index == -1:
            index = i
    if len(ans) == k:
        if index == n:
            print("all")
        else:
            print('some')
    else:
        print('sad')
