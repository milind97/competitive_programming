(n, l, r) = map(int, input().split())
a = list(map(int, input().split()))
R = list(range(l, r+1))
valid = 0
def search(R, x, y):
    if len(R) == 0:
        return -1
    mid = len(R)//2
    if R[mid] <= x:
        if R[mid] != R[-1]:
            return search(R[mid+1:], x, y)
        else:
            return 0
    elif R[mid] > x:
        if R[mid] < y:
            return R[mid]
        else:
            if len(R) != 1:
                return search(R[:mid], x, y)
            else:
                return 0
for i in range(0,len(a)-1):
    for j in range(i+1, len(a)):
        x = max(a[i]-a[j], a[j]-a[i])
        y = a[i] + a[j]
        if x > R[-1] or y < R[0]:
            continue
        else:
            temp = search(R[:], x, y)
        if temp != 0 and temp != -1:
            R.remove(temp)
            valid += 1
        elif temp == -1:
            break
    else:
        continue
    break
print(valid)
