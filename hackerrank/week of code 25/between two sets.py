(n, m) = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
min_b = min(b)
max_a = max(a)
count = 0
for i in range(max_a,min_b+1):
    for x in range(n):
        if i%a[x] != 0:
            break
    else:
        for y in range(m):
            if b[y]%i != 0:
                break
        else:
            count += 1
print(count)