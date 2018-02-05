def solve(x):
    if x % 11 == x:
        return 2*x - 1
    l = len(str(x))
    temp = int('1'*l)
    if x % temp == x:
        l -= 1
        temp = int('1'*l)
    t1 = x // temp
    return t1*l + t1 - 1 + solve(x % temp)

n = int(input())
for i in range(n):
    num = int(input())
    print(solve(num))
