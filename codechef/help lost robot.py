t = int(input())
while(t):
    t -= 1
    (x1,y1,x2,y2) = map(int,input().split())
    if x1==x2:
        if y1 < y2:
            print("up")
        else:
            print("down")
    elif y1==y2:
        if x1 < x2:
            print("right")
        else:
            print("left")
    else:
        print("sad")