t = int(input())
for i in range(1, t+1):
    n = int(input())
    a = []
    ans = n
    if n == 0:
        print("Case #{}: {}".format(i, "INSOMNIA"))
    else:
        while len(a) != 10:
            num = ans
            while num > 0:
                temp = num % 10
                if temp not in a:
                    a.append(temp)
                num //= 10
            ans += n
        print("Case #{}: {}".format(i, ans - n))

