def left(l, m):
    global mat
    while mat[l][m] != -1:
        mat[l][m] = 1
        m -= 1


def right(l, m):
    global mat
    while mat[l][m] != -1:
        mat[l][m] = 1
        m += 1


def fill_mat(l, m, t, check=0, lat=''):
    global mat
    global flag
    global p
    global b
    if check == 1:
        if (mat[i-1][j] == 1) or (mat[i][j-1] == 1):
            if p == 1 and b == 1:
                flag = 1
                return
    if flag == 0:
        if lat == 'p':
            b = 0
        elif lat == 'b':
            p = 0
    if (mat[l][m-1] == -1) and (mat[l-1][m] == -1):
        mat[l][m] = t
    elif t == 1:
        left(l, m)
        left(l-1, m)
        right(l-1, m)
    elif t == 2 or t == 3:
        if mat[l-1][m] == 2:
            left(l-1, m)
            right(l-1, m)
            mat[l][m] = 2
        elif mat[l-1][m] == 1:
            left(l, m)
        if mat[l][m-1] == 1 or mat[l][m-1] == 2:
            mat[l][m] = mat[l][m-1]
            if mat[l-1][m] != 1 and mat[l-1][m] != -1:
                left(l-1, m)
                right(l-1, m)

test = int(input())
while test:
    test -= 1
    n = int(input())
    a = ['.'*(n+2)]
    for i in range(1, n+1):
        a.append(input())
        a[i] = '.'+a[i]+'.'
    a.append('.'*(n+2))
    mat = [0]*(n+2)
    flag = 0
    temp = p = b = 0
    ans = 1
    for i in range(n+2):
        mat[i] = [0]*(n+2)
        for j in range(n+2):
            if flag == 1:
                break
            if a[i][j] == '.':
                mat[i][j] = -1
            elif a[i][j] == 'G':
                if (a[i][j+1] != '.') or (a[i+1][j] != '.') or (mat[i-1][j] != -1) or (mat[i][j-1] != -1):
                    flag = 1
                    break
            elif a[i][j] == '?':
                if (a[i][j+1] == '.') and (a[i+1][j] == '.'):
                    fill_mat(i, j, 3)
                elif (a[i][j+1] == 'P') or (a[i+1][j] == 'P'):
                    p = 1
                    fill_mat(i, j, 1, 1, 'p')
                elif (a[i][j+1] == 'B') or (a[i+1][j] == 'B'):
                    b = 1
                    fill_mat(i, j, 1, 1, 'b')
                elif (a[i][j+1] == '?') or (a[i+1][j] == '?'):
                    if a[i+1][j] == '?':
                        if a[i][j+1] == 'P':
                            p = 1
                            fill_mat(i, j, 1, 1, 'p')
                        elif a[i][j+1] == 'B':
                            b = 1
                            fill_mat(i, j, 1, 1, 'b')
                        else:
                            fill_mat(i, j, 2)
                    else:
                        if a[i+1][j] == 'P':
                            p = 1
                            fill_mat(i, j, 1, 1, 'p')
                        elif a[i+1][j] == 'B':
                            b = 1
                            fill_mat(i, j, 1, 1, 'b')
                        else:
                            fill_mat(i, j, 2)
            elif a[i][j] == 'B':
                b = 1
                fill_mat(i, j, 1, 1, 'b')
            elif a[i][j] == 'P':
                p = 1
                fill_mat(i, j, 1, 1, 'p')
        else:
            continue
        break
    if flag == 1:
        print(0)
    else:
        for i in range(1, n+1):
            for j in range(1, n+1):
                if (mat[i][j] > 0) and (mat[i][j-1] != mat[i][j]):
                    ans *= mat[i][j]
        print(ans % (10**9 +7))
