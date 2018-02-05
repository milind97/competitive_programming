import itertools
n, u = map(int, input().split())
look = list((itertools.accumulate([x for x in range(0, n+1)])))[::-1]
print(look)
print([x for x in range(0, n+1)])
