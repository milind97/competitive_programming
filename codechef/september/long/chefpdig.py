import collections
t = int(input())
while t:
    t -= 1
    n = input()
    d = collections.defaultdict(int)
    for s in n:
        d[int(s)] += 1
    count = ''
    #print(d)
    for i in range(6, 10):
        #print('d[i]', d[i])
        if d[i] > 0:
            l = 0
            r = 10
            if i == 6:
                l = 5
            elif i == 9:
                r = 1
            for j in range(l, r):
                if j != i:
                    if d[j] > 0:
                        count += chr(int(str(i) + str(j)))
                else:
                    if d[i] > 1:
                        count += chr(int(str(i) + str(j)))
    print(count)
