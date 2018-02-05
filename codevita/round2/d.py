m, x = map(int, input().split())
a = []
total = 0
for i in range(m):
    t1 = int(input())
    total += t1
    a.append((t1, m-i))
if total > x:
    print('Thank you, your order for {0} eggs are accepted'.format(x))
else:
    print('Sorry, we can only supply {0} eggs'.format(total-1))
    x = total - 1
d = {}
for j in reversed(sorted(a)):
    if x == 0:
        d[j] = (0, j[0])
    if x > j[0]:
        d[j] = (j[0], 0)
        x -= j[0]
    else:
        d[j] = (x, j[0]-x)
        x = 0
for k in a:
    print(k[0], d[k][0], d[k][1])

