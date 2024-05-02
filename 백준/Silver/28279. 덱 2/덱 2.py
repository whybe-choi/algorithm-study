from collections import deque
import sys

n = int(sys.stdin.readline().rstrip())
d = deque()

for _ in range(n):
    command = sys.stdin.readline().rstrip()

    if command.startswith("1"):
        x = int(command.split()[-1])
        d.appendleft(x)
    elif command.startswith("2"):
        x = int(command.split()[-1])
        d.append(x)
    elif command.startswith("3"):
        if d:
            print(d.popleft())
        else:
            print(-1)
    elif command.startswith("4"):
        if d:
            print(d.pop())
        else:
            print(-1)
    elif command.startswith("5"):
        print(len(d))
    elif command.startswith("6"):
        print(0 if d else 1)
    elif command.startswith("7"):
        if d:
            print(d[0])
        else:
            print(-1)
    else:
        if d:
            print(d[-1])
        else:
            print(-1)