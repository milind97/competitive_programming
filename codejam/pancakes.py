def consecutive_one(st):
    for k in range(len(st)):
        if st[k] == "0":
            return k
    else:
        return len(st)
def flip(st):
    global ans
    ans += 1
    st = ''.join([str(int(not(int(one)))) for one in st])
    return st

t = int(input())
for i in range(1, t+1):
    s = input()
    ans = 0
    a = ''
    for j in range(len(s)):
        if s[j] == '-':
            a += '0'
        else:
            a += '1'
    while a != "1"*len(a):
        for j in range(len(a)-1, -1, -1):
            if a[j] == '0':
                if a[0] == '0':
                    a = flip(a[j::-1]) + a[j+1:]
                else:
                    x = consecutive_one(a)
                    a = flip(a[x-1::-1]) + a[x:]
                    a = flip(a[j::-1]) + a[j + 1:]
    print("Case #{}: {}".format(i, ans))