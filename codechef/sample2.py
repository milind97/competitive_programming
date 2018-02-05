def solve(a, count, m, x, n, i):
    if i >= n:
        return count
    while i < n:
        print("i", i)
        y = x
        x *= a[i]
        print('x now:', x)
        if x > m or x < y:
            count += pow(2, n-i-1)
            print('count', count)
        else:
            z = x
            j = i+1
            while j < n:
                print('inside j<n j:', j)
                z *= a[j]
                if z > m:
                    break
                j += 1
            print('z after loop:', z)
            if j >= n:
                print('returning count:', count)
                return count
            print('solving rec count:', count)
            count = solve(a, count, m, x, n, i+1)
        x = y
        i += 1
    return count


def main():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    print(arr, n, k)
    ans = solve(arr, 0, k, 1, n, 0)
    l = pow(2, n) - 1
    l -= ans
    print(l)


if __name__ == "__main__":
    main()