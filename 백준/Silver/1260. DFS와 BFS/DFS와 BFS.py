import sys
from collections import deque

def dfs(graph, v, visited):
    """
    graph : 인접리스트 방식으로 표현된 그래프.
    v : 현재 방문한 노드.
    visited : 각 노드별로 방문 여부를 저장한 리스트.
    """
    
    # 함수 호출 시 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')
    # 현재 노드의 인접 노드에 대해 재귀적으로 방문
    for i in graph[v]:
        # 방문하지 않은 인접 노드가 있을 경우
        if not visited[i]:
            # 해당 인접 노드에 대해 재귀적으로 함수 호출
            dfs(graph, i, visited)
            
def bfs(graph, start, visited):
    """
    start : 시작 노드
    """
    
    queue = deque([start])
    visited[start] = True
    
    # 큐가 빌 때까지 반복
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        # 현재 노드와 연결된 인접 노드 중 방문하지 않은 인접 노드들을 
        # 큐에 삽입하고 방문 처리
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

for i in range(len(graph)):
    graph[i] = sorted(graph[i])
                
visited_dfs = [False] * (n+1)
visited_bfs = [False] * (n+1)

dfs(graph, v, visited_dfs)
print()
bfs(graph, v, visited_bfs)
    