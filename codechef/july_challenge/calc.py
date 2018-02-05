t = int(input())
while t:
    t -= 1
    n, b = map(int, input().split())
    mid = n//2
    r = mid % b
    ll = mid - r
    ul = ll + b
    print(max((ul*(n-ul)//b), (ll*(n-ll)//b)))
