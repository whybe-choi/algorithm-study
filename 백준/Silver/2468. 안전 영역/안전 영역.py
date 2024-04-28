import sys
sys.setrecursionlimit(100000)

n = int(sys.stdin.readline())

grid = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

def dfs(x, y, k):
    # 하, 우, 상, 좌
    dxs, dys = [0, 1, 0, -1], [-1, 0, 1, 0]

    for dx, dy in zip(dxs, dys):
        new_x, new_y = x + dx, y + dy
        if (new_x >= 0 and new_x < n) and (new_y >= 0 and new_y < n) and grid[new_x][new_y] > k and not visited[new_x][new_y]:
            visited[new_x][new_y] = True
            dfs(new_x, new_y, k)

# k값에 따른 안전 영역의 수
answer = 0

for k in range(101):
    # 가능한 k값마다 visited를 초기화해줘야 함.
    visited = [[False] * n for _ in range(n)]
    # 안전 영역의 수
    count = 0
    for x in range(n):
        for y in range(n):
            if grid[x][y] > k and not visited[x][y]:
                count += 1
                visited[x][y] = True
                dfs(x, y, k)
                
    answer = max(answer, count)

print(answer)
