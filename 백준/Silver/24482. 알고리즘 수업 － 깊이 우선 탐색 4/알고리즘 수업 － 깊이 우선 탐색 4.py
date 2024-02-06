import sys

sys.setrecursionlimit(10 ** 8)

def dfs(graph, v, visited, depth):
    visited[v] = depth
    
    for i in graph[v]:
        # 인접 노드를 방문할 수록 노드의 깊이는 하나씩 더해짐
        if visited[i] == -1:
            dfs(graph, i, visited, depth+1)

n, m, r = map(int, sys.stdin.readline().rstrip().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

# 인접 정점을 내림차순으로 방문해야하므로 정렬
for i in range(n+1):
    graph[i].sort(reverse=True)
    
visited = [-1] * (n+1)
depth = 0

dfs(graph, r, visited, depth)

print(*visited[1:], sep='\n')