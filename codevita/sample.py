p, q = map(int, input().split(','))
a1, a2 = map(int, input().split(','))
#b1, b2 = map(int, input().split(','))
#c1, c2 = map(int, input().split(','))
count11 = 0
t1 = max(a1, a2)
t2 = min(a1, a2)
stop = False
if t1//t2 > 0:
    t3 = 0
    while t3 <= t1//t2:
        if t2 == a1:
            if p*t3 + a1 == a2:
                stop = True
                break
        else:
            if q*t3 + a2 == a1:

                stop = True
                break
        t3 += 1
count11 = t3
count1 = 0
if not stop:
    while p*count1 + a1 != q*count1 + a2 and p*count1 <= p*q:
        count1 += 1
        count11 += 1
print(count1)