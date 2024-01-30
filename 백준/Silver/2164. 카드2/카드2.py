import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
queue = deque([i for i in range(1, n+1)])
last = 0

while queue:
    last = queue.popleft()
    queue.rotate(-1)
    
print(last)