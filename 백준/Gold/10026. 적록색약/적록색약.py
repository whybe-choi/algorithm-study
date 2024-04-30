from collections import deque

n = int(input())
grid = [[color for color in input()] for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]

def dfs():
    # 하, 우, 상, 좌
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
    
    while queue: 
        x, y = queue.popleft()
        for dx, dy in zip(dxs, dys):
            new_x, new_y = x + dx, y + dy
            if (new_x >= 0 and new_x < n) and (new_y >= 0 and new_y < n) and grid[new_x][new_y] == grid[x][y] and not visited[new_x][new_y]:
                visited[new_x][new_y] = 1
                queue.append((new_x, new_y))

count = 0

# 적록색약 X dfs
for x in range(n):
    for y in range(n):
        if not visited[x][y]:
            queue = deque()
            queue.append((x, y))
            visited[x][y] = 1
            dfs()
            count += 1

# 방문 여부 초기화
visited = [[0 for _ in range(n)] for _ in range(n)]

# 적록색약용 그리드
for x in range(n):
    for y in range(n):
        if grid[x][y] == 'R':
            grid[x][y] = 'G'

# 적록색약 dfs
count_blind = 0
for x in range(n):
    for y in range(n):
        if not visited[x][y]:
            queue = deque()
            queue.append((x, y))
            visited[x][y] = 1
            dfs()
            count_blind += 1

print(count, count_blind)