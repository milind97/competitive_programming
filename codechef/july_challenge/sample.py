def blsearch(a, num):
    high = len(a) - 1
    low = 0
    if not a:
        return -1
    if num < a[0]:
        return -1
    if num > a[high]:
        return high

    while high >= low:
        if high - low <= 1:
            if a[high] <= num:
                return high
            else:
                return low
        midval = (low+high) // 2
        if a[midval] > num:
            high = midval - 1
        else:
            low = midval
    return -1

a = [11, 11, 11]
print(blsearch(a, 11))
