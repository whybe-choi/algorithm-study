import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)
    
def bfs(graph, start, visited):
    queue = deque([[start, 0]])
    visited[start] = True
    count = 0
    while queue:
        v, depth = queue.popleft()
        
        if depth >= 2:
                break
        
        for next_v in graph[v]:
            if not visited[next_v]:
                queue.append([next_v, depth+1])
                visited[next_v] = True
                count += 1
                
    return count

visited = [False] * (n+1)
print(bfs(graph, 1, visited))