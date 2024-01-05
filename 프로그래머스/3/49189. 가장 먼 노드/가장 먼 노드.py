from collections import deque

def solution(n, edge):
    graph = [[] for n in range(n+1)] # 인접 행렬 방식으로 그래프를 표현하기 위해 2차원 리스트 생성
    
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
        
    distance = [0] * (n+1)
    distance[1] = 1
    queue = deque([1])
    
    while queue:
        src = queue.popleft()
        for dest in graph[src]:
            if distance[dest] == 0:
                queue.append(dest)
                distance[dest] = distance[src] + 1

    return distance.count(max(distance))