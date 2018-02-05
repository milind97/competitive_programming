t = int(input())
while t:
    t -= 1
    cnt_a = 1
    cnt_b = 1
    cnt = 1
    a, b = map(int, input().split())
    while True:
        if cnt % 2 != 0:
            temp = cnt_a**2
            if temp > a:
                print("Bob")
                break
            else:
                cnt_a += 1
        else:
            temp = cnt_b**2 + cnt_b
            if temp > b:
                print("Limak")
                break
            else:
                cnt_b += 1
        cnt += 1
