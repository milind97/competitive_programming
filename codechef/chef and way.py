import queue as Q
import math
(n, k) = map(int, input().split())
a = list(map(int, input().split()))
m = (10**9) + 7
ans = [0]*n
ans[0] = a[0]
for i in range(1, min(n, k+1)):
    ans[i] = (a[0]*a[i])
for i in range(k+1, n):
    q = Q.PriorityQueue(k)
    for j in range(i-k, i):
        q.put((math.log(ans[j]), j))
    temp2 = ()
    temp2 = q.get()
    ans[i] = (a[i]*ans[int(temp2[1])])
print(ans[n-1] % m)