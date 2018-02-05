import random
t = random.randint(1, 10)
print(t)
j = 0
while j < t:
    n = random.randint(1, 10**5)
    print(n)
    r1 = ''.join([random.choice(['.', '*']) for x in range(n)])
    r2 = ''.join([random.choice(['.', '*']) for x in range(n)])
    print(r1)
    print(r2)
    j += 1

