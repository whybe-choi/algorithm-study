import sys
from collections import deque

queue = deque()
n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    prompt = sys.stdin.readline().rstrip()
    
    if prompt == 'back':
        print(queue[-1] if len(queue) != 0 else -1)
    elif prompt == 'front':
        print(queue[0] if len(queue) != 0 else -1)
    elif prompt == 'empty':
        print(1 if len(queue) == 0 else 0)
    elif prompt == 'size':
        print(len(queue))
    elif prompt == 'pop':
        print(queue.popleft() if len(queue) != 0 else -1)
    else:
        x = int(prompt.split()[-1])
        queue.append(x)
        