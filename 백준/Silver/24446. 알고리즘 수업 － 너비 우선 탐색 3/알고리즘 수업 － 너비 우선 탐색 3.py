import sys
from collections import deque

def bfs(graph, start, visited):
    visited[start] = 0
    queue = deque([start])

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if visited[i] == -1:
                queue.append(i)
                # 현재 방문 노드에 연결된 인접 노드의 깊이 =  현재 방문 노드의 깊이 + 1
                visited[i] = visited[v] + 1

n, m, r = map(int, sys.stdin.readline().rstrip().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [-1] * (n+1)
bfs(graph, r, visited)

print(*visited[1:], sep='\n')
    