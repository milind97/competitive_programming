t = int(input())
while t:
    t -= 1
    s = input().strip()
    revs = ''.join([str(int(not int(x)))  for x in s])
    flag = True
    count = 0
    for x in range(len(s)-1, -1, -1):
        if flag:
            if s[x] == '1':
                count += 1
                flag = False
        else:
            if revs[x] == '1':
                count += 1
                flag = True
    print(count)
