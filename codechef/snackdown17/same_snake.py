t = int(input())
while t:
    t -= 1
    x11, y11, x12, y12 = map(int, input().split())
    x21, y21, x22, y22 = map(int, input().split())
    flag = False
    if (x11 == x21 and y11 == y21) or (x12 == x22 and y12 == y22) or (x11 == x22 and y11 == y22) or (
            x12 == x21 and y12 == y21):
        flag = True
    elif y11 == y12:
        min1 = min(x11, x12)
        max1 = max(x11, x12)
        if y21 == y22 and y21 == y11:
            min2 = min(x21, x22)
            max2 = max(x21, x22)
            print("min1,max1, min2,max2:", min1, max1, min2, max2)
            if min2 <= max1 and max2 >= min1:
                flag = True
    else:
        min1 = min(y11, y12)
        max1 = max(y11, y12)
        if x21 == x22 and x21 == x11:
            min2 = min(y21, y22)
            max2 = max(y21, y22)
            print("min1,max1, min2,max2:", min1, max1, min2, max2)
            if min2 <= max1 and max2 >= min1:
                flag = True
    if flag:
        print("yes")
    else:
        print("no")
