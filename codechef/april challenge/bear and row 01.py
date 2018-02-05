t = int(input())
while t:
    t -= 1
    s = input()
    num_1 = num_0 = time = 0
    if s[0] == '1':
        num_1 += 1
    else:
        num_0 += 1
    for i in range(1, len(s)):
        if s[i] == '0':
            num_0 += 1
        else:
            if s[i-1] == '0':
                time += (num_1 * (num_0+1))
            num_1 += 1
            num_0 = 0
    if num_0 != 0:
        time += (num_1 * (num_0 + 1))
    print(time)

