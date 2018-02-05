from sys import stdin


def main():
    n, q = map(int, stdin.readline().split())
    arr = list(map(int, stdin.readline().split()))
    for i in range(q):
        a, b, c, d = map(int, stdin.readline().split())
        a1 = list(sorted(arr[a-1:b]))
        a2 = list(sorted(arr[c-1:d]))
        l = 0
        r = b-a
        flag = 0
        while r >= l and flag < 2:
            if a1[l] != a2[l]:
                flag += 1
            if a1[r] != a2[r] and l != r:
                flag += 1
            l += 1
            r -= 1
        if flag >= 2:
            print('NO')
        else:
            print('YES')

if __name__ == '__main__':
    t = int(stdin.readline())
    while t:
        t -= 1
        main()
