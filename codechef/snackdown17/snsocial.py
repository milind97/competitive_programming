from sys import stdin


def main():
    t = int(stdin.readline())
    while t:
        t -= 1
        n, m = map(int, stdin.readline().split())
        a = []
        maxval = 0
        store = []
        for i in range(n):
            a.append(list(map(int, stdin.readline().split())))
        for i in range(n):
            for j in range(m):
                if a[i][j] > maxval:
                    maxval = a[i][j]
                    store = [(i, j)]
                elif a[i][j] == maxval:
                    store.append((i, j))
        z = max(n, m)
        hr_required = 0
        for i in range(n):
            for j in range(m):
                minhr = z
                if a[i][j] != maxval:
                    for x, y in store:
                        hr = max(abs(i - x), abs(j - y))
                        if hr < minhr:
                            minhr = hr
                    if minhr > hr_required:
                        hr_required = minhr
        print(hr_required)

if __name__ == "__main__":
    main()
