def solve(arr, i, j, num):
    temp = []
    if arr[i-1][j] < arr[i][j]:
        temp.append((arr[i-1][j], (i-1, j)))
    if arr[i+1][j] < arr[i][j]:
        temp.append((arr[i+1][j], (i+1, j)))
    if arr[i][j+1] < arr[i][j]:
        temp.append((arr[i][j+1], (i, j+1)))
    if arr[i][j-1] < arr[i][j]:
        temp.append((arr[i][j-1], (i, j-1)))
    temp.sort(reverse=True)
    #print("value:", arr[i][j])
    if not temp:
        return num
    j = 0
    count = 1
    fl = True
    while j < len(temp)-1 and fl:
        if temp[j+1][0] == temp[0][0]:
            count += 1
            j += 1
        else:
            fl = False
    maxval = 0
    #print("temp:", temp)
    #print("count:", count)
    for i in range(count):
        t2 = solve(arr, temp[i][1][0], temp[i][1][1], num+1)
        if t2 > maxval:
            maxval = t2
    return maxval



def main():
    m, n = map(int, input().split(','))
    a = [[201]*(n+2)]
    for i in range(m):
        a.append([201] + list(map(int, input().split(','))) + [201])
    a.append([201]*(n+2))
    #print(a)
    x, y = map(int, input().split(','))
    #t1 = set()
    #t1.add((x, y))
    print(solve(a, x, y, 1))



if __name__ == "__main__":
    main()
