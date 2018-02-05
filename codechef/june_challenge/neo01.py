t = int(input())
while t:
    t -= 1
    n = int(input())
    ans = maxans = 0
    sump = count = 0
    neg = 0
    for x in reversed(sorted(map(int, input().split()))):
        if x >= 0:
            sump += x
            count += 1
            maxans = sump*count
        else:
            ans = (sump+x)*(count+1)
            if ans >= maxans:
                maxans = ans
                sump += x
                count += 1
            else:
                neg += x
    print(maxans+neg)


