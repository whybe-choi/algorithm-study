import sys

a, b = map(int, sys.stdin.readline().rstrip().split())

if a > b:
    a, b = b, a

print(len(range(a+1, b)))
print(*list(range(a+1, b)), sep=' ')