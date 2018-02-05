t = int(input())
while t:
     t -= 1
     u, v = map(int, input().split())
     print(((u+v)*(u+v+1)//2) + (u+1))