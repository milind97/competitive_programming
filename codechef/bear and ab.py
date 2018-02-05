import collections
t = int(input())
while t:
    t -= 1
    n, k = map(int, input().split())
    s = input()
    cnt_b = 0
    d = collections.defaultdict(int)
    for i in s:
        if i == 'a':
            d[cnt_b] += 1
        if i == 'b':
            cnt_b += 1
    x = sum(d.values()) * cnt_b
    y = 0
    for key in d.keys():
        y += key*d[key]
    print((x*(k*(k+1)//2)) - y*k)
