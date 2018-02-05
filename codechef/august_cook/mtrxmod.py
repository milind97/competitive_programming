n, q = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
a0 = 0
ans = [0]*n
for k in a[0]:
    print(-k, end=' ')
print()
for j in range(q):
    p = int(input())
    p -= 1
    f = list(map(int, input().split()))
    for k, val in enumerate(f):
        if k == 0:
            ans[p] = -val
        elif k == p:
            ans[k] = -(abs(val) + abs(ans[p]))
        elif k > p:
            ans[k] = ans[p] - val
    for k in ans:
        print(k, end=' ')
    print()






