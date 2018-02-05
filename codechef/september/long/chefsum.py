import itertools

t = int(input())
while t:
    t -= 1
    n = int(input())
    a = list(map(int, input().split()))
    a1 = list(itertools.accumulate(a))
    a2 = list(itertools.accumulate(a[::-1]))[::-1]
    ans = 0
    minv = a1[0] + a2[0]
    for i in range(1, n):
        if a1[i] + a2[i] < minv:
            ans = i
            minv = a1[i] + a2[i]
    print(ans+1)
