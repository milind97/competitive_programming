t = int(input())
while t:
    t -= 1
    s = input().split()
    if len(s) == 1:
        print(s[0].capitalize())
    else:
        ans = ''
        for i in range(len(s)):
            if i != len(s)-1:
                ans += s[i].capitalize()[0] + '. '
            else:
                ans += s[i].capitalize()
        print(ans)

