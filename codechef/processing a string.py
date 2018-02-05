t = int(input())
while(t):
    t -= 1
    s = input()
    sum=0
    for i in range(len(s)):
        try:
            int(s[i])
        except(ValueError):
            pass
        else:
            sum += int(s[i])
    print(sum)
