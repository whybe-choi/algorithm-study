import sys
from itertools import combinations

n, m = map(int, sys.stdin.readline().rstrip().split())
combs = combinations(range(1, n+1), m)

for comb in combs:
    print(' '.join(map(str, comb)))