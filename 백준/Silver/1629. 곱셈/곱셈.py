import sys

sys.setrecursionlimit(1000000)

a, b, c = map(int, sys.stdin.readline().rstrip().split())

def mod(a, b, c):
    if b == 1:
        return a % c

    val = mod(a, b//2, c)
    val = val * val % c

    if b % 2 == 0:
        return val

    return val * a % c

print(mod(a, b, c))