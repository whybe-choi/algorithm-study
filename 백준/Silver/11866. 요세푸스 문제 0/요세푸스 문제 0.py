import sys
from collections import deque

n, k = map(int, sys.stdin.readline().rstrip().split())
queue = deque([i for i in range(1, n+1)])
order = []

while queue:
    queue.rotate(-k)
    order.append(queue.pop())
    
print(f"<{', '.join(map(str, order))}>")