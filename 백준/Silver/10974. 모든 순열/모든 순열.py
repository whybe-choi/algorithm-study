import sys
from itertools import permutations

n = int(sys.stdin.readline().rstrip())

pers = permutations(range(1, n+1), n)

for per in pers:
    print(*per)