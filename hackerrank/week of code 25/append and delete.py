s = input().strip()
t = input().strip()
k = int(input())

if len(s) <= len(t):
    temp = len(s)
    for i in range(len(s)):
        if s[i]!=t[i]:
            temp = i
            break
else:
    temp = len(t)
    for i in range(len(t)):
        if s[i]!=t[i]:
            temp = i
            break
if temp == len(t) and temp ==len(s):
    if k >= 2*temp or k%2==0:
        print("Yes")
    else:
        print("No")
else:
    x = (len(t) - temp) + (len(s) - temp)
    if k < x:
        print("No")
    elif x == k or k >= len(s)+len(t):
        print("Yes")
    elif k > x:
        if k >= (x + 2*temp):
            print("Yes")
        else:
            if ((k % x) % 2) == 0:
                print("Yes")
            else:
                print("No")
    else:
        print("No")