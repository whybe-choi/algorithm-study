import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

grid = [[int(s) for s in sys.stdin.readline().rstrip()] for _ in range(n)]

max_length = min(n, m)

max_square = 1
for i in range(1, max_length):
    for x in range(n-i):
        for y in range(m-i):
            if (grid[x][y] == grid[x+i][y]) and (grid[x][y] == grid[x+i][y+i]) and (grid[x][y] == grid[x][y+i]):
                max_square = i + 1

print(max_square**2)