from sys import stdin, stdout
from math import sqrt
import heapq
t = int(stdin.readline())
while t:
    t -= 1
    n, q = map(int, stdin.readline())
    stock = list(map(int, stdin.readline()))
    block_size = int(sqrt(n))
    queries = {}
    h = []
    k_d = {j: 0 for j in range(n+1)}
    counter = (0, 0)
    stock_d = {(stock[0], 0): 1}
    (mo_left, mo_right) = (1, -1)
    min_size = []
    max_size = [-1]
    num_segment = counter[1] - counter[0] + 1
    for i in range(q):
        temp = tuple(map(int, stdin.readline()))
        queries[temp] = -1
        heapq.heappush(h, ((temp[0]//block_size, temp[1]), temp))
    while h:
        (l, r, k) = heapq.heappop(h)[1]
        while mo_right < r-1:
            mo_right += 1
            if stock[mo_right] != stock[mo_right-1]:
                k_d[stock_d[(stock[mo_right-1], counter[1])]] += 1
                heapq.heappush(min_size, stock_d[(stock[mo_right-1], counter[1])])
                counter[1] += 1
                stock_d[(stock[mo_right], counter[1])] += 1
            else:
                stock_d[(stock[mo_right], counter[1])] += 1
            if -1*stock_d[(stock[mo_right], counter[1])] <= max_size[0]:
                heapq.heappush(max_size, -1*stock_d[(stock[mo_right], counter[1])])

        while mo_left < l-1:
            mo_left += 1
            if stock[mo_left] != stock[mo_left-1]:
                if stock_d[(stock[mo_left-1], counter[0])] == min_size[0]:
                    heapq.heappop(min_size)
                k_d[stock_d[(stock[mo_left-1], counter[0])]] -= 1
                stock_d[(stock[mo_left-1], counter[0])] -= 1
                counter[0] += 1
            else:
                stock_d[(stock[mo_left], counter[0])] -= 1
                if stock_d[(stock[mo_left], counter[0])] == -1*(max_size[0] - 1)
                    heapq.heappushpop(max_size, stock_d[(stock[mo_left], counter[0])])

            if stock_d[(stock[mo_right], counter[1])] > max_size:
                max_size = stock_d[(stock[mo_right], counter[1])]







