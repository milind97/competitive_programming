from sys import stdin


t = int(stdin.readline())
while t:
    t -= 1
    n, m = map(int, stdin.readline().split())
    minsalary = list(map(int, stdin.readline().split()))
    offer = []
    for i in range(m):
        offer.append(tuple(map(int, stdin.readline().split())))
    qual = []
    for i in range(n):
        qual.append(stdin.readline())
    total_salaries = 0
    get_job = 0
    no_cand = set([x for x in range(m)])
    for i in range(n):
        maxsal = 0
        comp = -1
        for j in range(m):
            if qual[i][j] == '1':
                if offer[j][0] >= minsalary[i] and offer[j][0] > maxsal and offer[j][1] > 0:
                    maxsal = offer[j][0]
                    comp = j
        if maxsal != 0:
            total_salaries += maxsal
            offer[comp] = (offer[comp][0], offer[comp][1]-1)
            get_job += 1
            if comp in no_cand:
                no_cand.remove(comp)
    print(get_job, total_salaries, len(no_cand))


