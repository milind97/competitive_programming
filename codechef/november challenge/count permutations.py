t = int(input())
M = (10**9)+7
while(t):
    x = 2
    result = 1
    t -= 1
    n = int(input())
    if n <= 2:
        print(0)
    else:
        y = n-1
        while(y):
            if y%2 == 1:
                result = (result * x) % M
            y = (y//2)
            x = (x*x) % M
        print(result - 2)


