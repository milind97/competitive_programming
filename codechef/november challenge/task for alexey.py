def gcd(a, b):
    if b%a == 0:
        return a
    else:
        return gcd(b%a, a)

def solution(a, n):
    global z
    for i in range(n-1):
        for j in range(i+1, n):
            if j in z:
                break
            lcm = (a[i] * a[j])/gcd(a[i], a[j])
            if i == 0 and j == 1:
                minlcm = lcm
            if minlcm > lcm:
                minlcm = lcm
            if j != n-1:
                if lcm == a[j]:
                    z.append(j)
                if lcm <= a[j+1]:
                    break
    return minlcm

t = int(input())
while(t):
    t -= 1
    z = []
    n = int(input())
    a = list(map(int, input().split()))
    a = sorted(a)
    if a[0] == 1:
        print(a[1])
    else:
        print(int(solution(a, n)))




