import re
r = int(input())
while r:
    r -= 1
    l = int(input())
    s = input().strip()
    reg = r'(\.)*((\.)*H(\.)*T(\.)*)*(\.)*'
    if re.fullmatch(reg, s):
        print('Valid')
    else:
        print('Invalid')