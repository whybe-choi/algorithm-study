import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
r1, c1, r2, c2 = map(int, sys.stdin.readline().rstrip().split())        

grid = [[0 for _ in range(n)] for _ in range(n)]

def dfs(start_x, start_y):
    queue = deque([(start_x, start_y)])
    visited[start_x][start_y] = 0
    # (r-2, c-1), (r-2, c+1), (r, c-2), (r, c+2), (r+2, c-1), (r+2, c+1)
    dxs, dys = [-2, -2, 0, 0, 2, 2], [-1, 1, -2, 2, -1, 1]
    while queue:
        x, y = queue.popleft()
        for dx, dy in zip(dxs, dys):
            new_x, new_y = x+dx, y+dy
            if 0 <= new_x < n and 0 <= new_y < n and visited[new_x][new_y] == -1:
                visited[new_x][new_y] = visited[x][y] + 1
                queue.append((new_x, new_y))

visited = [[-1 for _ in range(n)] for _ in range(n)]
dfs(r1, c1)
print(visited[r2][c2])