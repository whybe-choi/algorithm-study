import sys

n = int(sys.stdin.readline().rstrip())

print(*list(range(1, n+1)), sep='\n')