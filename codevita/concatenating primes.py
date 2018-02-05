from sys import stdin, stdout

maxval = 10**5 + 1
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


def main():
    n = int(stdin.readline())
    a = []
    count = 0
    ans = set()
    for x in range(1, n+1):
        if isprime[x]:
            a.append(x)
    for x in range(len(a)):
        for y in range(len(a)):
            temp = int(str(a[x]) + str(a[y]))
            if isprime[temp]:
                ans.add(temp)
    stdout.write(str(len(ans)) + '\n')


if __name__ == "__main__":
    main()