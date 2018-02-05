import heapq
import collections
from sys import stdin
t = int(stdin.readline())
while t:
    t -= 1
    n, d = map(int, stdin.readline().split())
    h = []
    day = collections.defaultdict(list)
    sad_sum = collections.defaultdict(int)
    for i in range(n):
        di, ti, si = map(int, stdin.readline().split())
        sad_sum[di] += -(si*ti)
        day[di].append((-si, ti))
    sadness = 0
    min_sadness = 0
    for j in range(1, d+1):
        for x in day[j]:
            heapq.heappush(h, x)
        sadness += sad_sum[j]
        #print('s:', sadness)
        if h:
            x, y = heapq.heappop(h)
            #min_sadness -= (sadness - x)
            #print('min_s:', min_sadness)
            sadness -= x
            if y != 1:
                heapq.heappush(h, (x, y - 1))
    if h:
        min_sadness -= sadness
    print(min_sadness)