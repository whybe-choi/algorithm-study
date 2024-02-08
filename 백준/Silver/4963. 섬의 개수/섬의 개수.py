from collections import deque
                    
while True:
    col_len, row_len = map(int, input().split())
    
    # 0, 0이 입력으로 들어온다면 종료
    if col_len == 0 and row_len == 0:
        break
        
    # 상하좌우 + 대각선 탐색을 위한 방향값
    dc = [0, -1, -1, -1, 0, 1, 1, 1]
    dr = [1, 1, 0, -1, -1, -1, 0, 1]

    # BFS
    def dfs(grid, start_r, start_c, visited):
        queue = deque([[start_r, start_c,]])
        visited[start_r][start_c] = True
        while queue:
            cur_r, cur_c = queue.popleft()
            for i in range(8):
                next_r = cur_r + dr[i]
                next_c = cur_c + dc[i]
                if 0 <= next_r < row_len and 0 <= next_c < col_len:
                    if grid[next_r][next_c] == 1 and not visited[next_r][next_c]:
                        queue.append([next_r, next_c])
                        visited[next_r][next_c] = True
 
    # 좌표 생성
    grid = []
    for _ in range(row_len):
        grid.append(list(map(int, input().split())))
        
    # 방문 여부 표현
    visited = [[False for _ in range(col_len)] for _ in range(row_len)]
    
    # 섬의 개수 출력
    count = 0
    for i in range(row_len):
        for j in range(col_len):
            if grid[i][j] == 1 and not visited[i][j]:
                dfs(grid, i, j, visited)
                count += 1
     
    print(count)
     
        
    
    
       
                    
                   