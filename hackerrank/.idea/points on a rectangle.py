q=int(input())
while(q):
    q -= 1
    n = int(input())
    l=[]
    max_x = -10**9
    max_y = -10**9
    min_x = 10**9
    min_y = 10**9
    for i in range(n):
        (x,y)=map(int,input().split())
        l.append((x,y))
        max_x = max(max_x,x)
        max_y = max(max_y,y)
        min_x = min(min_x,x)
        min_y = min(min_y,y)
    for point in l:
        if (not(((point[0]==max_x or point[0]==min_x) and (min_y<=point[1]<=max_y)) or ((point[1]==min_y or point[1]==max_y) and (min_x<=point[0]<=max_x)))):
            print("NO")
            break
    else:
        print("YES")