def is_prime(num):
    if num == 2 or num == 3: return True
    if num < 2 or num % 2 == 0: return False
    if num < 9: return True
    if num % 3 == 0: return False
    r = int(num ** 0.5)
    f = 5
    while f <= r:
        if num % f == 0: return False
        if num % (f + 2) == 0: return False
        f += 6
    return True


def sample(s, base):
    return sum(int(x) * (base ** y) for y, x in enumerate(s[::-1]))


def divisor(x):
    for m in range(2, x//2+1):
        if x%m == 0:
            return m
t = int(input())
for i in range(1, t + 1):
    (n, j) = map(int, input().split())
    a = [False]*9
    temp = 2**(n-1) + 1
    print("Case #{}:".format(i))
    for k in range(temp, (temp-1)*2, 2):
        numbers = [sample(bin(k)[2:], i) for i in range(2, 11)]
        b = [is_prime(l) for l in numbers]
        if a == b:
            ans = [divisor(z) for z in numbers]
            print(bin(k)[2:], end=" ")
            for c in range(9):
                print(ans[c], end=" ")
            print()
            j -= 1
        if j == 0:
            break


