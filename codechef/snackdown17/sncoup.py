t = int(input())
while t:
    t -= 1
    n = int(input())
    r1 = input() + '.'
    r2 = input() + '.'
    arr = [False]*n
    arr[0] = True
    count = 0
    star1 = True
    star2 = True
    for i in range(n):
        if arr[i]:
            first1 = first2 = True
        if r1[i] == '*':
            star1 = False
            if not first1:
                arr[i] = True
                first2 = True
                count += 1
            first1 = False
            if r1[i+1] == '*':
                arr[i+1] = True
                count += 1
        if r2[i] == '*':
            star2 = False
            if not first2:
                arr[i] = True
                if r1[i] != '*' and not first1:
                    first1 = True
                count += 1
            first2 = False
            if r2[i+1] == '*':
                if not arr[i+1]:
                    arr[i+1] = True
                    count += 1
    if star1 or star2:
        print(count)
    else:
        print(count+1)
