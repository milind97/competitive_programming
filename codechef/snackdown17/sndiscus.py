import math


def distance(x, y, a, n):
    sumd = 0
    for i in range(n):
        dx = a[i][0] - x
        dy = a[i][1] - y
        sumd += math.sqrt(dx**2 + dy**2)
    return sumd


def dist(x, y, i, j):
    return math.sqrt((x-i)**2 + (y-j)**2)


def main():
    n = int(input())
    points = []
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    segments = []
    for i in range(n):
        x1, y1, x2, y2 = map(int, input().split())
        segments.append((x1, y1, x2, y2))
        if x1 == x2:
            for j in range(min(y1, y2), max(y1, y2)+1):
                points.append((x1, j))
        else:
            for j in range(min(x1, x2), max(x1, x2)+1):
                points.append((j, y1))
    x = y = 0
    for i in range(len(points)):
        x += points[i][0]
        y += points[i][1]
    x //= n
    y //= n
    d = distance(x, y, points, len(points))
    step = 100.0
    done = 0
    eps = 0.01
    while step > eps:
        done = 0
        for i in range(4):
            nx = x + step * dx[i]
            ny = y + step * dy[i]
            t = distance(nx, ny, points, len(points))
            if t < d:
                d = t
                x = nx
                y = ny
                done = 1
                break
        if not done:
            step /= 2
    maxval = 0
    x = int(x)
    y = int(y)
    points = []
    for i in range(n):
        z1 = dist(segments[i][0], segments[i][1], x, y)
        z2 = dist(segments[i][2], segments[i][3], x, y)
        if z1 <= z2:
            points.append((segments[i][0], segments[i][1]))
        else:
            points.append((segments[i][2], segments[i][3]))
    for point in points:
        curr = max(abs(point[0]-x), abs(point[1]-y))
        if curr > maxval:
            maxval = curr
    print(maxval)

if __name__ == "__main__":
    tc = int(input())
    while tc:
        tc -= 1
        main()

