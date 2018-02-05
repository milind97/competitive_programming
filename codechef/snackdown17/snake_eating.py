import itertools


def search(a, low, high, k):
    if high == low:
        return low
    mid = low + ((high-low) // 2)
    if a[mid] >= k:
        return search(a, mid+1, high, k)
    else:
        return search(a, low, mid, k)


def search2(a, low, high, val, x):
    if high < low:
        return low
    if low > high:
        return high
    if high == low:
        if (low+1)*x + a[low+1] > val:
            return low
        else:
            return low+1
    mid = low + ((high - low) // 2)
    if (mid+1)*x + a[mid+1] > val:
        return search2(a, low, mid-1, val, x)
    else:
        return search2(a, mid+1, high, val, x)


t = int(input())
while t:
    t -= 1
    (n, q) = tuple(map(int, input().split()))
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    look = [x for x in itertools.accumulate(reversed(arr))][::-1]
    look.append(0)
    for i in range(q):
        ki = int(input())
        index = search(arr, 0, n-1, ki)
        value = n-index+look[index]
        index += search2(look[index:], 0, len(look[index:])-2, value, ki+1)
        print(index)
