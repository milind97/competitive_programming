def ans(sum,total,req):
    global boxes
    if req:
        for j in range(1,total+1):
            ans(sum-j,total,req-1)
            if boxsum(boxes)+j==sum:
                boxes=boxes+[j]
                return
        else:
            return

    else:
        return
def boxsum(l):
    a=0
    for i in range(len(l)):
       a=a+l[i]
    return (a)
t=int(input())
boxes=[]
for i in range(t):
    boxes=[]
    line=list(map(int,input().split()))
    (n,k,b)=(line[0],line[1],line[2])
    ans(n,k,b)
    if boxes==[]:
        print(-1)
    else:
        for i in range(len(boxes)):
            print(boxes[i],end=" ")
        print()



