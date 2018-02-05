for i in range(int(input())):
    s = input()
    d = {'A': 0, 'B': 0}
    count = 0
    prev = ''
    for j in s:
        if j != '.':
            d[j] += 1
            if j == prev:
                d[j] += count
            count = 0
            prev = j
        else:
            count += 1
    print(d['A'], d['B'])
