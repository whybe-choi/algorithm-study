from collections import deque

n, m = map(int, input().split())
grid = [[int(i) for i in input()] for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]

queue = deque()

def dfs():
    # 하, 우, 상, 좌
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
    
    while queue: 
        x, y = queue.popleft()
        for dx, dy in zip(dxs, dys):
            new_x, new_y = x + dx, y + dy
            if (new_x >= 0 and new_x < n) and (new_y >= 0 and new_y < m) and grid[new_x][new_y] and not visited[new_x][new_y]:
                visited[new_x][new_y] = visited[x][y] + 1
                queue.append((new_x, new_y))


queue.append((0, 0))
visited[0][0] = 1
dfs()
print(visited[n-1][m-1])