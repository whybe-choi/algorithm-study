import sys
from collections import deque

n, m = map(int, sys.stdin.readline().rstrip().split())

grid = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
dp = [[0 for _ in range(m)] for _ in range(n)]

def bfs():
    # 인접한 8방향(대각선 포함)
    dxs, dys = [1, 1, 0, -1, -1, -1, 0, 1], [0, 1, 1, 1, 0, -1, -1, -1]
    while queue:
        x, y = queue.popleft()
        for dx, dy in zip(dxs, dys):
            new_x, new_y = x+dx, y+dy
            if (new_x >= 0 and new_x < n) and (new_y >= 0 and new_y < m) and visited[new_x][new_y] == -1:
                if grid[new_x][new_y] == 0:
                    queue.append((new_x, new_y))
                    visited[new_x][new_y] = visited[x][y] + 1
                # 상어가 존재하는 칸에 도달했을 경우 해당 칸까지의 거리 반환
                else:
                    return visited[x][y] + 1

# 상어가 존재하지 않는 모든 위치에 대하여 상어가 존재하는 칸까지의 최소 거리 구하기
for x in range(n):
    for y in range(m):
        if grid[x][y] == 0:
            visited = [[-1 for _ in range(m)] for _ in range(n)]
            queue = deque([(x, y)])
            visited[x][y] = 0
            dp[x][y] = bfs()
            
# DP 테이블에 기록한 상어가 존재하는 칸까지의 최소 거리 중 최댓값 구하기
max_dist = 0
for x in range(n):
    for y in range(m):
        max_dist = max(dp[x][y], max_dist)

print(max_dist)