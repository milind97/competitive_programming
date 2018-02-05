import random
n = random.randint(1, 100)
print(n)
for i in range(n):
    print(random.randint(2, 10**6), end=" ")
print()
print(10)
for i in range(10):
    print(random.randint(1, n), end=" ")
    print(random.randint(1, n), end=" ")
    print(random.randint(2, 10**6), end=" ")
    print(random.randint(2, 10**6))
