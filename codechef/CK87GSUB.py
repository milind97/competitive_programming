t = int(input())
while t:
    t -= 1
    s = input()
    ans = i = count = 0
    first = ''
    while i < len(s)-1:
        j = i+1
        count = 0
        while j < len(s):
            if s[j] != s[i]:
                break
            count += 1
            j += 1
        if s[j] == first:
            ans += 1
        first = s[i]
        i = j
        count -= 1
        ans += count*(count-1) // 2
    print(ans)





