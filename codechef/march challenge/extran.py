t = int(input())
while(t):
    t -= 1
    n = int(input())
    a = list(map(int, input().split()))
    a = sorted(a)
    if a[0] != a[1]-1:
        print(a[0])
    elif a[n-2] != a[n-1]-1:
        print(a[n-1])
    else:
        for i in range(n):
            if a[i] == a[i+1]:
                print(a[i])
                break


