from sys import stdin, stdout

maxval = 10**6 + 1
isprime = [True]*maxval
spf = [0] * maxval
prime = []
isprime[0] = isprime[1] = False
for i in range(2, maxval):
    if isprime[i]:
        prime.append(i)
        spf[i] = i
    j = 0
    while j < len(prime) and i*prime[j] < maxval and prime[j] <= spf[i]:
        isprime[i*prime[j]] = False
        spf[i*prime[j]] = prime[j]
        j += 1


class Node:

    def __init__(self):
        self.dict, self.presum = [], []


def merge(a, b):
    z = Node()
    i = j = sum = 0
    m = len(a.dict)
    n = len(b.dict)
    while i < m and j < n:
        if a.dict[i][0] < b.dict[j][0]:
            z.dict.append((a.dict[i][0], a.dict[i][1]))
            sum += a.dict[i][1]
            z.presum.append(sum)
            i += 1
        elif a.dict[i][0] == b.dict[j][0]:
            z.dict.append((a.dict[i][0], a.dict[i][1]+b.dict[j][1]))
            sum += a.dict[i][1]+b.dict[j][1]
            z.presum.append(sum)
            i += 1
            j += 1
        else:
            z.dict.append((b.dict[j][0], b.dict[j][1]))
            sum += b.dict[j][1]
            z.presum.append(sum)
            j += 1
    if i < m:
        for x in range(i, m):
            z.dict.append((a.dict[x][0], a.dict[x][1]))
            sum += a.dict[x][1]
            z.presum.append(sum)
    else:
        for x in range(j, n):
            z.dict.append((b.dict[x][0], b.dict[x][1]))
            sum += b.dict[x][1]
            z.presum.append(sum)
    z.presum.append(0)
    return z


def construct_tree(input, seg, low, high, pos):
    if low == high:
        seg[pos] = get_factors(input[low])
        return
    mid = (low+high) // 2
    construct_tree(input, seg, low, mid, 2*pos+1)
    construct_tree(input, seg, mid+1, high, 2*pos+2)
    seg[pos] = merge(seg[2*pos + 1], seg[2*pos + 2])


def get_factors(x):
    global spf
    temp = Node()
    sum = index = 0
    while x != 1:
        if index == 0:
            temp.dict.append((spf[x], 1))
            index = 1
            sum = 1
        elif spf[x] == temp.dict[index-1][0]:
            temp.dict[index-1] = (temp.dict[index-1][0], temp.dict[index-1][1]+1)
            sum += 1
        else:
            index += 1
            temp.presum.append(sum)
            temp.dict.append((spf[x], 1))
            sum += 1
        x //= spf[x]
    temp.presum.append(sum)
    temp.presum.append(0)
    return temp


def nextpower(x):
    count = 0
    while x > 0:
        count += 1
        x >>= 1
    return 1 << count


def rangequery(seg, qlow, qhigh, low, high, pos, x, y):
    if qlow <= low and qhigh >= high:
        l1 = blsearch(seg[pos].dict, x)
        r1 = busearch(seg[pos].dict, y)
        if l1 == -1 or r1 == -1:
            return 0
        else:
            return seg[pos].presum[r1] - seg[pos].presum[l1-1]
    if qlow > high or qhigh < low:
        return 0
    mid = (low+high) // 2
    return rangequery(seg, qlow, qhigh, low, mid, 2*pos+1, x, y) + rangequery(seg, qlow, qhigh, mid+1, high, 2*pos+2, x, y)


def blsearch(a, num):
    high = len(a) - 1
    low = 0
    if num > a[high][0]:
        return -1
    if num < a[0][0]:
        return 0
    while high >= low:
        midval = (low+high) // 2
        if a[midval][0] == num:
            return midval
        elif a[midval][0] < num:
            low = midval + 1
        else:
            if a[midval-1][0] < num:
                return midval
            else:
                high = midval - 1
    return -1


def busearch(a, num):
    high = len(a) - 1
    low = 0
    if num >= a[high][0]:
        return high
    if num < a[0][0]:
        return -1
    while low <= high:
        if high-low <= 1:
            if a[high][0] > num:
                return low
            else:
                return high
        midval = (low+high) // 2
        if a[midval][0] > num:
            high = midval - 1
        else:
            low = midval
    return -1


def main():
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    if n & n-1 == 0:
        seg = [0]*(2*n - 1)
    else:
        seg = [0]*(2*nextpower(n) - 1)
    construct_tree(a, seg, 0, n-1, 0)
    q = int(stdin.readline())
    for i in range(q):
        l, r, x, y = map(int, stdin.readline().split())
        stdout.write(str(rangequery(seg, l - 1, r - 1, 0, n - 1, 0, x, y)) + '\n')

if __name__ == '__main__':
        main()

