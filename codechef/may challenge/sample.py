def sliding(arr, frame):
    sum = 0
    for i in arr[:frame]:
        sum += i
    fmax = smax = sum
    for i in range(frame, len(arr)):
        sum += arr[i] - arr[i-frame]
        if sum > fmax:
            smax = fmax
            fmax = sum
        else:
            if sum > smax:
                smax = sum
    return fmax, smax


def shift(arr):
    temp = [arr[-1]]
    temp.extend(arr[:-1])
    return temp


def main():
    n, p, k = map(int, input().split())
    a = list(map(int, input().split()))
    q = input()
    for s in q:
        if s == '?':
            print(sliding(a, k))
        else:
            a = shift(a)


if __name__ == "__main__":
    main()