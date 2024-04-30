from collections import deque

n = int(input())
grid = [[int(i) for i in input()] for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]


def dfs():
    global count

    # 하, 우, 상, 좌
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
    
    while queue:
        global count
        x, y = queue.popleft()
        for dx, dy in zip(dxs, dys):
            new_x, new_y = x + dx, y + dy
            if (new_x >= 0 and new_x < n) and (new_y >= 0 and new_y < n) and grid[new_x][new_y] and not visited[new_x][new_y]:
                count += 1
                visited[new_x][new_y] = True
                queue.append((new_x, new_y))

houses = []

for x in range(n):
    for y in range(n):
        if grid[x][y] and not visited[x][y]:
            queue = deque()
            queue.append((x, y))
            # 각 단지에 속하는 집의 오름 차수
            count = 1
            visited[x][y] = True
            dfs()
            houses.append(count)

print(len(houses))
for house in sorted(houses):
    print(house)