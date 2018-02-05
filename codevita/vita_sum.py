import math
mod = 10**9 + 7
n, k = map(int, input().split())
sum = 0
if k % 2 == 0:
    for i in range(0, k+1, 2):
        f = math.factorial
        product = f(n) / (f(i)*f(n-i))
        product %= mod
        sum += product
else:
    for i in range(0, k, 2):
        f = math.factorial
        product = f(n) / (f(i)*f(n-i))
        product %= mod
        sum += product
print(int(sum))