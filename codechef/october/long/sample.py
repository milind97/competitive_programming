import random
n = random.randint(1, 20)
#print(n)
print(1)
s = ''
for i in range(n):
    s = ''.join([s, random.choice(['a', 'b'])])
print(s)
print(random.randint(1, len(s)), random.randint(1, len(s)))


