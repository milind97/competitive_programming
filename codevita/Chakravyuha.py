n = int(input())
a = [[0 for i in range(n)] for j in range(n)]
k = 0
count = 1
power = [(0, 0)]
while k < n:
    i = j = k
    while j < n-k:
        a[i][j] = count
        if count % 11 == 0:
            power.append((i, j))
        count += 1
        j += 1
    j -= 1
    i += 1
    while i < n-k:
        a[i][j] = count
        if count % 11 == 0:
            power.append((i, j))
        count += 1
        i += 1
    i -= 1
    j -= 1
    while j >= k:
        a[i][j] = count
        if count % 11 == 0:
            power.append((i, j))
        count += 1
        j -= 1
    j += 1
    i -= 1
    while i >= k+1:
        a[i][j] = count
        if count % 11 == 0:
            power.append((i, j))
        count += 1
        i -= 1
    i += 1
    k += 1
for i in range(n):
    for j in range(n):
        print(a[i][j], end='\t')
    print()
print("Total Power points :", len(power))
for points in power:
    print(points)

