t = int(input())
for i in range(1, t+1):
    n = int(input())
    mod = 2**33
    ans = 1
    base = 2
    if n >= 33:
        print("Case {}: {}".format(i, 2**33 - 1))
    else:
        while n>0:
            if n%2 == 1:
                ans = (ans*base) % mod
            base = (base*base) % mod
            n //= 2
        ans = (ans - 1) % mod
        print("Case {}: {}".format(i, ans))