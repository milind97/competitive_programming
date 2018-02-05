from sys import stdin


def search(a, num):
    high = len(a) - 1
    low = 0
    while high >= low:
        mid = (low + high) // 2
        if a[mid] == num:
            return True
        elif num < a[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return False


def same(a, b):
    num = 0
    for x in a:
        if search(b, x):
            num += 1
    return num


def main():
    n, k = map(int, stdin.readline().split())
    l = [0] * n
    sets = []
    for i in range(n):
        a = list(map(int, stdin.readline().split()))
        l[i] = a[0]
        sets.append(list(sorted(a[1:])))
    count = 0
    for i in range(n - 1):
        for j in range(i+1, n):
            if l[i] + l[j] >= k:
                if l[i] < l[j]:
                    temp = same(sets[i], sets[j])
                else:
                    temp = same(sets[j], sets[i])
                if l[i] + l[j] - temp == k:
                    count += 1
    print(count)


if __name__ == "__main__":
    t = int(stdin.readline())
    while t:
        t -= 1
        main()
