def sliding(arr, frame):
    sum = 0
    index = frame-1
    for i in arr[:frame]:
        sum += i
    maxsum = sum
    for i in range(frame, len(arr)):
        sum += arr[i] - arr[i - frame]
        if sum > maxsum:
            index = i
            maxsum = sum
    return maxsum, index


def shift(arr):
    temp = [arr[-1]]
    temp.extend(arr[:-1])
    return temp


def main():
    n, k, p = map(int, input().split())
    a = list(map(int, input().split()))
    q = input()
    ans = sliding(a, k)
    for s in q:
        if s == '?':
            if ans[1] <= n-1:
                print(ans[0])
            else:
                ans = (sliding(a, k))
                print(ans[0])
        else:
            a = shift(a)
            ans = (ans[0], ans[1]+1)


if __name__ == "__main__":
    main()