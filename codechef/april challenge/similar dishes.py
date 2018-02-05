t = int(input())
while t:
    t -= 1
    a = set(input().split())
    b = set(input().split())
    if len(a & b) >= 2:
        print("similar")
    else:
        print("dissimilar")
