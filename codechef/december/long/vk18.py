a = [-1]*2000001
ans = [0]*1000001


def calculate(n):
    global a
    if a[n] == -1:
        e = o = 0
        for i in str(n):
            if int(i) % 2 == 0:
                e += int(i)
            else:
                o += int(i)
        a[n] = abs(e-o)
    return a[n]


number = 3
seq = 2
total = 2
maxn = 1
for t in range(int(input())):
    n = int(input())
    ans[1] = 2
    if n > maxn:
        for i in range(maxn+1, n+1):
            seq = seq - calculate(i) + calculate(number)
            #print('seq', seq)
            total += seq*2 + calculate(i*2)
            seq += calculate(i*2)
            number = i*2 + 1
            ans[i] = total
        maxn = n
        #print(number, seq, total)
        #print('m', maxn)
    print(ans[n])
