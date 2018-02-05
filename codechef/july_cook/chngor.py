for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for x in a:
        ans |= x
    print(ans)
