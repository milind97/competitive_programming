def generate(m):
    s1 = "RG"*(m//2) + "R"*(m%2)
    s2 = "GR"*(m//2) + "G"*(m%2)
    return s1, s2


for t in range(int(input())):
    n, m = map(int, input().split())
    s1, s2 = generate(m)
    ans1 = ans2 = 0
    for i in range(n):
        for j, val in enumerate(input()):
            if val == 'R':
                if val == s1[j]:
                    ans2 += 5
                else:
                    ans1 += 5
            else:
                if val == s1[j]:
                    ans2 += 3
                else:
                    ans1 += 3
        s1, s2 = s2, s1
    print(min(ans1, ans2))


