def cal(s, x):
    count = 0
    for i in s:
        if i == x:
            count += 1
    return count

t = int(input())
while t:
    t -= 1
    t1 = input()
    t2 = input()
    a = set(t1)
    b = set(t2)
    if a != b:
        if a & b == set() and len(t1) > len(a):
            print("A")
        elif a > b:
            print('A')
        else:
            c = a - b
            for y in c:
                if cal(t1, y) > 1:
                    print('A')
                    break
            else:
                print('B')
    else:
        print('B')
