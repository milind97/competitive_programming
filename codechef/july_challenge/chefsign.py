t = int(input())
while t:
    t -= 1
    s = input()
    if '='*len(s) == s:
        print(1)
    else:
        longest = 0
        l1 = l2 = 0
        for x in range(len(s)):
            if s[x] == '<':
                l2 = 0
                l1 += 1
                if l1 > longest:
                    longest = l1
            elif s[x] == '>':
                l1 = 0
                l2 += 1
                if l2 > longest:
                    longest = l2
        print(longest+1)

