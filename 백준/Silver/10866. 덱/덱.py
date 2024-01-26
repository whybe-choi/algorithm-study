import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
deq = deque()

for _ in range(n):
    prompt = sys.stdin.readline().rstrip()
    if prompt == 'back':
        print(deq[-1] if len(deq) != 0 else -1)
    elif prompt == 'front':
        print(deq[0] if len(deq) != 0 else -1)
    elif prompt == 'empty':
        print(1 if len(deq) == 0 else 0)
    elif prompt == 'size':
        print(len(deq))
    elif prompt == 'pop_back':
        print(deq.pop() if len(deq) != 0 else -1)
    elif prompt == 'pop_front':
        print(deq.popleft() if len(deq) != 0 else -1)
    elif prompt.split()[0] == 'push_front':
        x = int(prompt.split()[-1])
        deq.appendleft(x)
    else:
        x = int(prompt.split()[-1])
        deq.append(x)
        