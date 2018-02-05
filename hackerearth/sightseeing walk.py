def search(element,stop):
    global M
    if element==stop:
        return False
    for i in range(M):
        if(path[i][1]==element):
            if path[i][0]==stop:
                return True
            else:
                return(search(path[i][0],stop))
    else:
        return False
T=int(input())
while(T > 0):
    T = T - 1
    N = int(input())
    M = int(input())
    H={}
    for i in range(1,N+1):
        H[i]=(int(input()))
    path={}
    for i in range(M):
        temp=[]
        temp.append(int(input()))
        temp.append(int(input()))
        temp=tuple(temp)
        path[i]=temp
    tempH=H
    maxdiff=0
    for i in range(1,N+1):
        maxheight=i
        for j in range(N):
            if(search(maxheight,j+1)):
                diff=H[maxheight]-H[j+1]
                print(H[maxheight],j+1,diff)
                if(diff>maxdiff):
                    maxdiff=diff
        print(H[maxheight],maxdiff)
    print(maxdiff)



