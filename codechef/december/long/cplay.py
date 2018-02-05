from sys import stdin, stdout

#count = 0
while True:
    s = stdin.readline().strip()
    if s == '':
        break
    g1 = g2 = 0
    i = 0
    while i < 20:
        if i % 2 == 0:
            if s[i] == '1':
                g1 += 1
        else:
            if s[i] == '1':
                g2 += 1

        if i == 5 or i == 7 or i == 9:
            if abs(g1-g2) >= 5 - (i//2):
                if g1 > g2:
                    print('TEAM-A', i+1)
                else:
                    print('TEAM-B', i+1)
                break
        elif i == 6 or i == 8:
            if g2 - g1 >= 5 - (i//2) or g1 - g2 >= 5 - (i-1)//2:
                if g1 > g2:
                    print('TEAM-A', i+1)
                else:
                    print('TEAM-B', i + 1)
                break
        elif i > 9 and i % 2 == 1:
            if abs(g1-g2) >= 1:
                if g1 > g2:
                    print('TEAM-A', i+1)
                else:
                    print('TEAM-B', i+1)
                break
        i += 1
    else:
        print("TIE")
    #stdout.write(s + '\n')

#print(count)

