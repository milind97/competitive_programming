import itertools
s = input()
ans = [''.join(x) for x in itertools.permutations(s)]
[print(s) for s in sorted(ans)]