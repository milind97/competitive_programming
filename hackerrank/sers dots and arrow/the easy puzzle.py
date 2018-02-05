def lcm(a, b):
    l = max(a, b)
    m = min(a, b)
    if (l % a == 0 and l % b == 0):
        return (l)
    else:
        x = gcd(a, b)
        if x==1:
            return(l*m)
        else:
            return(m*x)


def gcd(a, b):
    l = max(a, b)
    m = min(a, b)
    if l % m == 0:
        return m
    else:
        return(gcd(l, l % m))


t = int(input())
while (t):
    t -= 1
    (n, k) = map(int, input().split())
    l = list(map(int, input().split()))
    ans = 1
    for i in range(len(l)):
        ans = (lcm(ans, l[i]))
    if ans % k == 0:
        print("YES")
    else:
        print("NO")