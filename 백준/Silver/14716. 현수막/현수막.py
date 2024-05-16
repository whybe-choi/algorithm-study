import sys
from collections import deque

m, n = map(int, sys.stdin.readline().rstrip().split())

# m행 n열로 현수막 정보가 주어짐
grid = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(m)]

def bfs(start_x, start_y):
    # 시작 지점을 queue에 넣고 방문 처리
    queue = deque([(start_x, start_y)])
    # 상, 하, 좌, 우, 대각선으로 이동 가능
    dxs, dys = [1, 1, 0, -1, -1, -1, 0, 1], [0, 1, 1, 1, 0, -1, -1, -1]
    # 큐가 비어 있지 않은 동안 반복
    while queue:
        x, y = queue.popleft()
        for dx, dy in zip(dxs, dys):
            new_x, new_y = x+dx, y+dy
            if (0 <= new_x < m) and (0 <= new_y < n) and grid[new_x][new_y] and not visited[new_x][new_y]:
                queue.append((new_x, new_y))
                visited[new_x][new_y] = 1

# 방문 여부 초기화
visited = [[0 for _ in range(n)] for _ in range(m)]
count = 0
# 모든 지점에 대하여 확인
for x in range(m):
    for y in range(n):
        # 아직 방문하지 않았으며 grid 값이 1인 지점만 방문
        # 모든 지점에 대해서 이미 방문한 지점이면 bfs가 호출되지 않도록 함
        if grid[x][y] and not visited[x][y]:
            # 해당 방문 위치의 방문 여부 변경
            visited[x][y] = 1
            bfs(x, y)
            count += 1

print(count)