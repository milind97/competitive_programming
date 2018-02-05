def solve(a, count, m, x, n, i):
    if i >= n:
        return count
    while i < n:
        y = x
        x *= a[i]
        if x > m or x < y or x > 10**18:
            count += pow(2, n-i-1)
        else:
            z = x
            j = i+1
            while j < n:
                z *= a[j]
                if z > m or z > 10**18:
                    break
                j += 1
            if j >= n:
                return count
            count = solve(a, count, m, x, n, i+1)
        x = y
        i += 1
    return count


def main():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    ans = solve(arr, 0, k, 1, n, 0)
    l = pow(2, n) - 1
    l -= ans
    print(l)


if __name__ == "__main__":
    main()