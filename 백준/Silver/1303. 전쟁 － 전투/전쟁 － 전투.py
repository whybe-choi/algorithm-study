import sys
from collections import deque

m, n = map(int, sys.stdin.readline().rstrip().split())
grid = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]

def bfs():
    global count
    # 하, 우, 상, 좌
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

    while queue:
        x, y = queue.popleft()

        for dx, dy in zip(dxs, dys):
            # 새로운 탐색 지점
            new_x, new_y = x+dx, y+dy
            # 1. 해당 지점이 범위 내의 존재
            # 2. 해당 지점에 아군이 존재(이전 지점과 탐색 지점 간의 값이 동일)
            # 3. 아직 방문하지 않음
            if (new_x >= 0 and new_x < n) and (new_y >= 0 and new_y < m) and grid[new_x][new_y] == grid[x][y] and not visited[new_x][new_y]:
                visited[new_x][new_y] = True
                queue.append((new_x, new_y))
                count += 1

solders = {"B" : 0, "W" : 0}

for x in range(n):
    for y in range(m):
        if not visited[x][y]:
            queue = deque([(x, y)])
            visited[x][y] = True
            count = 1
            bfs()
            solders[grid[x][y]] += count ** 2

print(solders["W"], solders["B"])