def solve(a, mid):
    low = high = 0
    ans = temp = t2 = 0
    for x in range(len(a)):
        if a[x] < mid:
            temp = mid - a[x]
            low += temp
        else:
            temp = mid - a[x]
            high -= temp
        t2 += temp
        ans += abs(t2)
    if low == high:
        return ans
    else:
        return -1


t = int(input())
while t:
    t -= 1
    n, d = map(int, input().split())
    ar = list(map(int, input().split()))
    ans = 0
    mv = sum(ar) // n
    for i in range(d):
        temp = [0] * (n // d + 1)
        j = i
        cnt = 0
        while j < n:
            temp[cnt] = ar[j]
            j += d
            cnt += 1
        # print(temp)
        if temp[-1] == 0:
            del (temp[-1])
        t1 = solve(temp, mv)
        if t1 == -1:
            print(-1)
            break
        else:
            ans += t1
    else:
        print(ans)