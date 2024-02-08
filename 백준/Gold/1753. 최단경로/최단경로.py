# Dijkstra 알고리즘
import heapq
import sys
from collections import defaultdict

INF = sys.maxsize

V, E = map(int, sys.stdin.readline().rstrip().split())
k = int(sys.stdin.readline().rstrip())
graph = defaultdict(list)

for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().rstrip().split())
    graph[u].append((w, v))
    
def dijkstra(graph, start_v):
    distances = [INF] * (V+1)
    distances[start_v] = 0
    pq = []
    heapq.heappush(pq, [0, start_v])
    
    while pq:
        cur_d, cur_v = heapq.heappop(pq)
        if cur_d > distances[cur_v]:
            continue
            
        for next_cost, next_v in graph[cur_v]:
            next_d = cur_d + next_cost
            if next_d < distances[next_v]:
                distances[next_v] = next_d
                heapq.heappush(pq, [next_d, next_v])
    return distances

distances = dijkstra(graph, k)

for distance in distances[1:]:
    if distance == INF:
        print("INF")
    else:
        print(distance)