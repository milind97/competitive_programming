import itertools
import sample

minv = 10000
a = itertools.combinations_with_replacement('ab', 10)
for i, x in enumerate(a):
    if i == 0 or i == 8:
        #print(''.join(x))
        t1 = sample.solve(''.join(x))
        if t1 < minv:
            minv = t1
    else:
        b = itertools.permutations(x)
        for y in b:
            t = ''.join(y)
            #print(t)
            t1 = sample.solve(t)
            if t1 < minv:
                minv = t1
print(minv)