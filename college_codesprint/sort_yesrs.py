l = int(input())
r = int(input())
count = 0
for x in range(l, r+1):
    ans = set()
    str_x = str(x)
    for y in range(len(str_x)):
        ans.add(int(str_x[y]))
    if len(ans) == len(str_x):
        count += 1
print(count)