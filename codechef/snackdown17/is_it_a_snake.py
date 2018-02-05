t = int(input())
while t:
    t -= 1
    n = int(input())
    r1 = input().strip()+'.'
    r2 = input().strip()+'.'
    ans = []
    hashes = 0
    for s in r1:
        if s == '#':
            hashes += 1
    for s in r2:
        if s == '#':
            hashes += 1
    for i in range(2):
        uprow = not i
        count = j = 0
        while j < n:
            if uprow:
                if r1[j] == '#':
                    count += 1
                    if r2[j] == '#':
                        count += 1
                        uprow = False
                    if r1[j+1] == '.':
                        if r2[j+1] == '.':
                            if uprow:
                                uprow = False
                            break
                        else:
                            if r2[j] == '.':
                                uprow = False
                                break
            else:
                if r2[j] == '#':
                    count += 1
                    if r1[j] == "#":
                        count += 1
                        uprow = True
                    if r2[j+1] == '.':
                        if r1[j+1] == '.':
                            break
                        else:
                            if r1[j] == '.':
                                break
            j += 1
        ans.append(count)
    if ans[0] == hashes or ans[1] == hashes:
        print("yes")
    else:
        print("no")