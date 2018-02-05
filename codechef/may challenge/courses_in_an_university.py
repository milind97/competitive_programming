t = int(input())
while t:
    t -= 1
    n = int(input())
    arr = list(map(int, input().split()))
    print(n-max(arr))