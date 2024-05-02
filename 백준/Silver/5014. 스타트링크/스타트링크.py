from collections import deque, defaultdict
import sys

f, s, g, u, d = map(int, sys.stdin.readline().rstrip().split())
    
visited = [-1 for _ in range(f)]

queue = deque()

def dfs():
    while queue: 
        curr_f = queue.popleft()
        for next_f in [curr_f + u, curr_f - d]:
            if (next_f >= 0 and next_f < f) and visited[next_f] == -1:
                visited[next_f] = visited[curr_f] + 1
                queue.append(next_f)

queue = deque()
queue.append(s-1)
visited[s-1] = 0
dfs()
print(visited[g-1] if visited[g-1] != -1 else "use the stairs")