import sys

n = int(sys.stdin.readline().rstrip())

coordinates = []
for _ in range(n):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    coordinates.append((x, y))

for (x, y) in sorted(coordinates, key = lambda k : (k[1], k[0])):
    print(x, y)