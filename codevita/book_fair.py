n, k = map(int, input().split(','))
y = k + 1
max_till = [0]*n
maxval = [0]*n
for i in range(n):
    if i <= k:
        max_till[i] = int(input())
    else:
        max_till[i] = maxval[i-y] + int(input())
    if max_till[i] > maxval[i - 1]:
        maxval[i] = max_till[i]
    else:
        maxval[i] = maxval[i - 1]
print(maxval[-1])

