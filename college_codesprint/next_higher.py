n = input()
i = len(n) - 1
while i != 0 and n[i] <= n[i-1]:
    i -= 1
temp = []
for x in n[i-1]+n[i+1:]:
    temp.append(x)
z = ''.join(y for y in sorted(temp))
if i != 0:
    ans = n[:i-1] + n[i] + z
    print(ans)
else:
    print(n)




