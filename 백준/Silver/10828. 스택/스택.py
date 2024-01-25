from collections import deque
import sys

n = int(sys.stdin.readline().rstrip())

stack = deque()
for _ in range(n):
    prompt = sys.stdin.readline().rstrip()
    if prompt == 'top':
        print(stack[-1] if len(stack) != 0 else -1)
    elif prompt == 'empty':
        print(1 if len(stack) == 0 else 0)
    elif prompt == 'size':
        print(len(stack))
    elif prompt == 'pop':
        print(stack.pop() if len(stack) != 0 else -1)
    else:
        x = int(prompt.split()[-1])
        stack.append(x)
