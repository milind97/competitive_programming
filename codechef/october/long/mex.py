t = int(input())
while t:
    t -= 1
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    i = val = 0
    #print(a)
    while i < n:
        #print('i, a[i], val, k:', i, a[i], val, k)
        if a[i] > val:
            if a[i] - val > k:
                if k != 0:
                    val += k - 1
                    k = 0
                else:
                    break
            else:
                k -= a[i] - val
                val = a[i]
        elif a[i] == val -1:
            val -= 1
        val += 1
        i += 1
    print(val+k)
