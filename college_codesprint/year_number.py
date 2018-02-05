month = int(input())
day = int(input())
a = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
print(a[month-1] + day)