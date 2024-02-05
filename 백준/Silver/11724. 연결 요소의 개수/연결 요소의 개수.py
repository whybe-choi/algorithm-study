import sys
from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


n, m = map(int, sys.stdin.readline().rstrip().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
	
# 인접 리스트 방식으로 그래프를 표현
for i in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

# 연결 요소의 개수
count = 0

# 모든 노드에 대해 해당 노드를 방문하지 않았을 경우 BFS를 실행
# BFS는 연결된 모든 노드를 탐색하는 알고리즘이므로, 각 연결 요소마다 BFS가 호출
# 따라서 연결 요소의 개수는 BFS를 호출한 횟수와 동일
for i in range(1, n+1):
    if not visited[i]:
        bfs(graph, i, visited)
        count += 1

print(count)
    
