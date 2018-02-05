import sys
sys.setrecursionlimit(10**9)
def sol(a, b, d):
    global l
    if d in l.keys():
        return l[d]
    else:
        l[d] = (min((1+sol(a, b, d-a)),(1+sol(a, b, d-b))))
        return l[d]
q = int(input())
while(q):
    l = {}
    q -= 1
    (a, b, d) = map(int, input().split())
    x = min(a, b)
    l[0] = 0
    l[a] = 1
    l[b] = 1
    for i in range(1, x):
        l[i] = 2
    if d<a or d<b:
        l[d] = 2
    print(sol(a,b,d))

