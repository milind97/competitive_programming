def add(final_s, ch, count, val):
    if count % val:
        final_s += ch*(count % val)
    else:
        final_s += ch*val
    return final_s


t = int(input())
while t:
    t -= 1
    s = input()
    x, y = map(int, input().split())
    ca = cb = 0
    for i in s:
        if i == 'a':
            ca += 1
        else:
            cb += 1
    #print('ca, cb:', ca, cb)
    #print('x, y:', x, y)
    ga = (lambda p: (p//x) + 1 if p % x else p // x)(ca)
    gb = (lambda p: (p//y) + 1 if p % y else p // y)(cb)
    bigger, smaller = (lambda p, q: ('ga', 'gb') if p >= q else ('gb', 'ga'))(ga, gb)
    fnl_str = ''
    #print(ga, gb, bigger)
    if ga == gb:
        fnl_str = ('a'*x + 'b'*y)*(ga - 1)
        fnl_str = add(fnl_str, 'a', ca, x)
        fnl_str = add(fnl_str, 'b', cb, y)
    elif x == 1 and y == 1:
        if bigger == 'ga':
            fnl_str = 'ab'*gb + 'a*'*(ga - gb - 1) + 'a'
        else:
            fnl_str = 'ba' * ga + 'b*' * (gb - ga - 1) + 'b'
    else:
        if smaller == 'ga':
            t1 = ca // (gb-1)
            t2 = ca % (gb-1)
            if t1 < 1:
                fnl_str = ('b'*y + 'a')*t2 + ('b'*y + '*')*(gb-1 - t2)
                fnl_str = add(fnl_str, 'b', cb, y)
            elif t1 == 1 and t2 == 0:
                fnl_str = ('b'*y + 'a'*x)*(gb-2) + 'b'*y
                fnl_str = add(fnl_str, 'a', ca, x)
                fnl_str = add(fnl_str, 'b', cb, y)
            else:
                fnl_str = ('b'*y + 'a'*t1)*(gb-1 - t2) + ('b'*y + 'a'*(t1+1))*t2
                fnl_str = add(fnl_str, 'b', cb, y)
        else:
            t1 = cb // (ga - 1)
            t2 = cb % (ga - 1)
            if t1 < 1:
                fnl_str = ('a' * x + 'b') * t2 + ('a' * x + '*') * (ga - 1 - t2)
                fnl_str = add(fnl_str, 'a', ca, x)
            elif t1 == 1 and t2 == 0:
                fnl_str = ('a' * x + 'b' * y) * (ga - 2) + 'a' * x
                fnl_str = add(fnl_str, 'b', cb, y)
                fnl_str = add(fnl_str, 'a', ca, x)
            else:
                fnl_str = ('a' * x + 'b' * t1) * (ga - 1 - t2) + ('a' * x + 'b' * (t1+1)) * t2
                fnl_str = add(fnl_str, 'a', ca, x)
    print(fnl_str)
