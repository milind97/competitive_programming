t = int(input())
for i in range(1, t+1):
    s = input()
    ans = s[0]
    for j in range(1, len(s)):
        if s[j] < ans[0]:
            ans += s[j]
        else:
            ans = s[j] + ans
    print("Case #{}: {}".format(i, ans))
