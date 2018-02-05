n = int(input())
a = list(map(int, input().split()))
temp = a[:]
l = sorted(a[:])
swaps = 0
for i in range(len(a)-1):
    j = a.index(l[i])
    if(j != i):
        (a[i], a[j]) = (a[j], a[i])
        swaps += 1
result = swaps
swaps = 0
l = list(reversed(l))
for i in range(len(temp)-1):
    j = temp.index(l[i])
    if (j != i):
        (temp[i], temp[j]) = (temp[j], temp[i])
        swaps += 1
print(min(result,swaps))