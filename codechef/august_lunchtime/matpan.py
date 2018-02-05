t = int(input())
d = {'o': 14, 'h': 7, 'w': 22, 'y': 24, 'e': 4, 'v': 21, 'l': 11, 'c': 2, 'f': 5, 'x': 23, 'k': 10, 'b': 1, 'i': 8,
     't': 19, 'g': 6, 'd': 3, 'm': 12, 's': 18, 'z': 25, 'n': 13, 'r': 17, 'a': 0, 'u': 20, 'p': 15, 'q': 16, 'j': 9}

while t:
    t -= 1
    a = list(map(int, input().split()))
    s = input()
    check = [False]*26
    for i in s:
        check[d[i]] = True
    price = 0
    for x, y in enumerate(check):
        if not y:
            price += a[x]
    print(price)



