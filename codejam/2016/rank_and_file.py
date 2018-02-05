t = int(input())
for i in range(1, t+1):
    n = int(input())
    ans = []
    d = {j: 0 for j in range(1, 2501)}
    for j in range(2*n-1):
        for num in list(map(int, input().split())):
            d[num] += 1
    for x in range(1, 2501):
        if d[x]%2 != 0:
            ans.append(x)
    print("Case #{}:".format(i), end=" ")
    for j in ans:
        print(j, end=" ")
    print()