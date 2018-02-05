def sol(a, b, d):
    global count
    global x

q = int(input())
while(q):
    count = 0
    q -= 1
    (a, b, d) = map(int, input().split())
    x = max(a, b)
    count += d//x
    print(sol(a, b, d%x))

