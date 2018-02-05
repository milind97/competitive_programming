p, q = map(int, input().split(','))
a1, a2 = map(int, input().split(','))
b1, b2 = map(int, input().split(','))
c1, c2 = map(int, input().split(','))
count1 = 0
t1 = max(a1, a2)
t2 = min(a1, a2)
stop = False
if t1//t2 > 0:
    t3 = 0
    while t3 <= t1//t2:
        if t2 == a1:
            if p*t3 + a1 == a2:
                count1 = t3
                stop = True
                break
        else:
            if q*t3 + a2 == a1:
                count1 = t3
                stop = True
                break
        t3 += 1
if not stop:
    while p*count1 + a1 != q*count1 + a2 and p*count1 <= p*q:
        count1 += 1
print(count1)
count2 = 0
t1 = max(b1, b2)
t2 = min(b1, b2)
stop = False
if t1//t2 > 0:
    t3 = 0
    while t3 <= t1//t2:
        if t2 == b1:
            if p*t3 + b1 == b2:
                count2 = t3
                stop = True
                break
        else:
            if q*t3 + b2 == b1:
                count2 = t3
                stop = True
                break
        t3 += 1
if not stop:
    while p*count2 + b1 != q*count2 + b2 and p*count2 <= p*q:
        count2 += 1
print(count2)
count3 = 0
t1 = max(c1, c2)
t2 = min(c1, c2)
stop = False
if t1//t2 > 0:
    t3 = 0
    while t3 <= t1//t2:
        if t2 == c1:
            if p*t3 + c1 == c2:
                count3 = t3
                stop = True
                break
        else:
            if q*t3 + c2 == c1:
                count3 = t3
                stop = True
                break
        t3 += 1
if not stop:
    while p*count3 + c1 != q*count3 + c2 and p*count3 <= p*q:
        count3 += 1
print(count3)
a = p*count1 + a1
b = p*count2 + b1
c = p*count3 + c1
print(a, b, c)
print(2*a + b - c)
