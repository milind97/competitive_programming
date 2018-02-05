T = int(input())
while(T):
    T -= 1
    n = int(input())
    a = list(map(int, input().split()))
    due = 0
    for i in range(len(a)):
        due += 1000
        if a[i] == 0:
            due += 100
        else:
            due -= 1000
            if(due != 0):
                due += 100
    print(due)
