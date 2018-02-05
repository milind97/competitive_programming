for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = a[::-1]
    count = 0
    for i, val in enumerate(b):
        if val == a[i]:
            j = (i+1) % n
            while j != i:
                if val != b[j] and val != a[j]:
                    b[j], b[i] = b[i], b[j]
                    count += 1
                    break
                j = (j+1) % n
        else:
            count += 1

    print(count)
    for i in b:
        print(i, end=' ')
    print()

