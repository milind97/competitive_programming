def test(num, b, c):
    ans = num
    for i in range(b-1):
        ans = pow(num, ans, c)
    return ans % c

t = int(input())
while t:
    t -= 1
    x, k, m = map(int, input().split())
    if k == 1:
        print(x % m)
    else:
        cnt = 3
        a = [-1, test(x, 1, m), test(x, 2, m)]
        while True:
            temp = test(x, cnt, m)
            if temp == a[2]:
                mod = cnt - 2
                a[1] = a[mod + 1]
                a[0] = a[mod]
                break
            elif temp == a[1]:
                mod = cnt - 1
                a[0] = a[mod]
                break
            else:
                a.append(temp)
            cnt += 1
        print(a[k % mod])
