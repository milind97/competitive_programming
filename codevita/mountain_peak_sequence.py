from sys import stdin, stdout


def main():
    mod = 10**9 + 7
    n = int(stdin.readline())
    if n == 1:
        stdout.write(str(0) + '\n')
    else:
        y = n-1
        num = 1
        x = 2
        while y > 0:
            if y & 1:
                num = (num*x) % mod
            y >>= 1
            x = (x*x) % mod
        num = num + mod - 2
        num %= mod
        stdout.write(str(num) + '\n')


if __name__ == "__main__":
    main()
