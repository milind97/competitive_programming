t = int(input())
store = []
maxr = 0
for j in range(t):
    l, r = map(int, input().split())
    if r > maxr:
        maxr = r
    store.append((l, r))

maxval = maxr + 1
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
till_now = [0]*maxval
final = [0]*maxval
for i in range(2, maxval):
    if isprime[i]:
        till_now[i] = till_now[i-1] + 1
    else:
        till_now[i] = till_now[i-1]
    if isprime[till_now[i]]:
        final[i] = final[i-1] + 1
    else:
        final[i] = final[i-1]

for j in store:
    print(final[j[1]] - final[j[0] - 1])


