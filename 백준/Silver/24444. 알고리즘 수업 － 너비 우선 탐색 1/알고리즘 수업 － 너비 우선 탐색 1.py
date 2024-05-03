import sys 
from collections import deque, defaultdict

n, m, r = map(int, sys.stdin.readline().rstrip().split())
grid = defaultdict(list)
visited = [0 for _ in range(n+1)]

for _ in range(m):
    u, v = map(int, sys.stdin.readline().rstrip().split())
    grid[u].append(v)
    grid[v].append(u)

for k, v in grid.items():
    grid[k] = sorted(v)

def dfs(start):
    queue = deque([start])
    order = 1
    visited[start] = order

    while queue:
        curr_v = queue.popleft()
        for next_v in grid[curr_v]:
            if not visited[next_v]:
                order += 1
                visited[next_v] = order
                queue.append(next_v)

dfs(r)

for i in range(1, n+1):
    print(visited[i])