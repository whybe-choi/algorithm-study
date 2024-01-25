from collections import deque

# 그래프를 인접 리스트 형태로 표현
n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 각 노드가 방문된 정보를 리스트 형태로 표현
visited = [False] * (n+1)
    
# 1번 노드와 연결된 노드의 수
total = 0

# 큐(Queue) 구현을 위해 deque 라이브러리 사용   
queue = deque([1])
    
# 현재 노드를 방문 처리
visited[1] = True 

# 큐가 빌 때까지 반복
while queue:
    # 큐에서 하나의 원소를 선택
    v = queue.popleft()
    # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
    for i in graph[v]:
        if not visited[i]:
            queue.append(i)
            visited[i] = True
            # 연결된 노드의 수 추가
            total += 1

print(total)