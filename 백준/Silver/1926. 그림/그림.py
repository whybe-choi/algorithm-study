import sys
from collections import deque

dr = [0, -1, 0, 1]
dc = [1, 0, -1, 0]

def bfs(grid, r, c, visited):
    queue = deque([[r, c]])
    visited[r][c] = True
    width = 0

    while queue:
        cur_r, cur_c = queue.popleft()
        width += 1
        for i in range(4):
            next_r = cur_r + dr[i]
            next_c = cur_c + dc[i]
            if 0 <= next_r < n and 0 <= next_c < m:
                if grid[next_r][next_c] == 1 and not visited[next_r][next_c]:
                    queue.append([next_r, next_c])
                    visited[next_r][next_c] = True
    return width

n, m = map(int, input().split())

grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))

visited = [[False for _ in range(m)] for _ in range(n)]
widths = []

count = 0
for r in range(n):
    for c in range(m):
        if grid[r][c] == 1 and not visited[r][c]:
            width = bfs(grid, r, c, visited)
            widths.append(width)
            count += 1

print(count)
print(max(widths) if widths else 0)