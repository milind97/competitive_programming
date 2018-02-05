t = int(input())
while(t):
    t -= 1
    n = int(input())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    (sum1, sum2) = (0, 0)
    for i in range(n):
        if i%2 == 0:
            sum1 += x[i]
            sum2 += y[i]
        else:
            sum1 += y[i]
            sum2 += x[i]
    print(min(sum1, sum2))