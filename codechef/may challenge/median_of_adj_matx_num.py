from itertools import count
t = int(input())
while t:
    t -= 1
    n = int(input())
    arr = list(map(int, input().split()))
    if n == 1:
        print(max(arr))
        for j in arr:
            print(j, end=" ")
        print()
    else:
        med = (n+1)//2
        arr.sort()
        max_v = arr[-med]
        ans = [0]*(2*n)
        temp = 2*med-1
        end = -med
        while end <= -1:
            ans[temp] = arr[end]
            temp += 2
            end += 1
        cnt = 0
        for i in count(0):
            if ans[i] == 0:
                ans[i] = arr[cnt]
                cnt += 1
            if cnt == 2*n-med:
                break
        print(max_v)
        for j in ans:
            print(j, end=" ")
        print()

