import sys

m = int(sys.stdin.readline().rstrip())

s = set()
for _ in range(m):
    command = sys.stdin.readline().rstrip()

    if command.startswith("add"):
        x = int(command.split()[-1])
        if x not in s:
            s.add(x)
    elif command.startswith("remove"):
        x = int(command.split()[-1])
        if x in s:
            s.remove(x)
    elif command.startswith("check"):
        x = int(command.split()[-1])
        print(1 if x in s else 0)
    elif command.startswith("toggle"):
        x = int(command.split()[-1])
        if x not in s:
            s.add(x)
        else:
            s.remove(x)
    elif command.startswith("all"):
        s = set([i for i in range(1, 21)])
    else:
        s = set()