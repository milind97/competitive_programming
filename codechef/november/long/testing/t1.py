import itertools

a = itertools.combinations_with_replacement('ab', 8)
for i, x in enumerate(a):
    print(x, i)