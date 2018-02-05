for i in range(int(input())):
    a = []
    for j in range(3):
        x, y, z = map(int, input().split())
        a.append((x, y, z))
    flag = False
    a.sort()
    for t in range(2):
        if a[t][0] > a[t+1][0] or a[t][1] > a[t+1][1] or a[t][2] > a[t+1][2] or a[t] == a[t+1]:
            break
    else:
        flag = True
    #print(a)
    if flag:
        print('yes')
    else:
        print('no')