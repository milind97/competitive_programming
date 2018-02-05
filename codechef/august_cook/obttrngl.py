t = int(input())
while t:
    t -= 1
    k, a, b = map(int, input().split())
    if a > b:
        a, b = b, a
    temp = b-a
    #print(temp)
    if temp == k/2:
        print(0)
    elif temp < k/2:
        print(temp-1)
    else:
        print(k - temp - 1)
