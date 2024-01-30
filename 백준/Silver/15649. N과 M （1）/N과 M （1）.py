import sys
from itertools import permutations

n, m = map(int, sys.stdin.readline().rstrip().split())
perms = permutations(range(1, n+1), m)

for perm in perms:
    print(' '.join(map(str, perm)))