from collections import deque

def solution(maps):
    row_len, col_len = len(maps), len(maps[0])
    visited = [[False] * col_len for _ in range(row_len)]
    distance = [[0] * col_len for _ in range(row_len)]
    
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    
    queue = deque([[0, 0]])
    visited[0][0] = True
    distance[0][0] = 1
    
    while queue:
        cur_r, cur_c = queue.popleft()
        for i in range(4):
            next_r = cur_r + dr[i]
            next_c = cur_c + dc[i]
            if 0 <= next_r < row_len and 0 <= next_c < col_len:
                if maps[next_r][next_c] == 1 and not visited[next_r][next_c]:
                    queue.append([next_r, next_c])
                    visited[next_r][next_c] = True
                    distance[next_r][next_c] = distance[cur_r][cur_c] + 1
            
    answer = distance[row_len-1][col_len-1] if distance[row_len-1][col_len-1] != 0 else -1
    
    return answer