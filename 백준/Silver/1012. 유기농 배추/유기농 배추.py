import sys

sys.setrecursionlimit(10 ** 8)

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def dfs(grid, r, c):
    visited[r][c] = True
    for i in range(4):
        next_r = r + dr[i]
        next_c = c + dc[i]
        if 0 <= next_r < row_len and 0 <= next_c < col_len:
            if grid[next_r][next_c] == 1 and not visited[next_r][next_c]:
                dfs(grid, next_r, next_c)

t = int(input())

for _ in range(t):
    col_len, row_len, k = map(int, sys.stdin.readline().rstrip().split())
    grid = [[0 for _ in range(col_len)] for _ in range(row_len)]
    visited = [[False for _ in range(col_len)] for _ in range(row_len)]

    for _ in range(k):
        c, r = map(int, sys.stdin.readline().rstrip().split())
        grid[r][c] = 1
        
    # 모든 노드(위치)에 대하여 배추흰지렁이 마리 수 구하기
    count = 0
    for i in range(row_len):
        for j in range(col_len):
            if grid[i][j] == 1 and not visited[i][j]:
                dfs(grid, i, j)
                count += 1

    print(count)
        


