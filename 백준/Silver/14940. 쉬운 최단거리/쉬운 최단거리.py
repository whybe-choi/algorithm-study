import sys
from collections import deque

n, m = map(int, sys.stdin.readline().rstrip().split())
grid = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
visited = [[-1 for _ in range(m)] for _ in range(n)]

def dfs():
    # 우, 하, 좌, 상
    dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1]

    while queue:
        x, y = queue.popleft()
        for dx, dy in zip(dxs, dys):
            new_x, new_y = x + dx, y + dy
            if (new_x >= 0 and new_x < n) and (new_y >= 0 and new_y < m) and grid[new_x][new_y] and visited[new_x][new_y] == -1:
                queue.append((new_x, new_y))
                visited[new_x][new_y] = visited[x][y] + 1

# 목표 지점 찾기
for x in range(n):
    for y in range(m):
        if grid[x][y] == 2:
            start_x, start_y = x, y

visited[start_x][start_y] = 0
queue = deque([(start_x, start_y)])
dfs()

for i in range(n):
    for j in range(m):
        # 방문하지 않은 지점 중 원래 갈 수 없는 땅이 위치를 0으로 바꿔준다.
        # 원래 갈 수 있는 땅 중 도달할 수 없는 부분은 bfs 과정에서 -1이 된다.
        if visited[i][j] == -1 and grid[i][j] == 0:
            visited[i][j] = 0

for row in visited:
    print(*row)