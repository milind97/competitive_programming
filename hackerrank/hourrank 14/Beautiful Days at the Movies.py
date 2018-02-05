def reverse(n):
    temp = 0
    while(n>0):
        temp = temp*10 + n%10
        n = n//10
    return temp
a = list(map(int, input().split()))
count = 0
for i in range(a[0],a[1]+1):
    if (i-reverse(i)) % a[2]==0:
        count += 1
print(count)