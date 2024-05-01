import sys

n = int(sys.stdin.readline().rstrip())

stack = []
for _ in range(n):
    command = sys.stdin.readline().rstrip()

    if command.startswith("1"):
        stack.append(int(command.split()[-1]))
    elif command.startswith("2"):
        if len(stack) != 0 :
            print(stack.pop())
        else:
            print(-1)
    elif command.startswith("3"):
        print(len(stack))
    elif command.startswith("4"):
        print(1 if len(stack) == 0 else 0)
    else:
        print(stack[-1] if len(stack) != 0 else -1)