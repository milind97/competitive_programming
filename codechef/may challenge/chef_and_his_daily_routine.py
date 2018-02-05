import re
t = int(input())
while t:
    t -= 1
    s = input()
    pattern = r"(C)*(E)*(S)*"
    if re.fullmatch(pattern, s):
        print("yes")
    else:
        print("no")