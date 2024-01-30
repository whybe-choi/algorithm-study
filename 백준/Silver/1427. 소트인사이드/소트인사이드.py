import sys

num = list(sys.stdin.readline().rstrip())
print(''.join(map(str, sorted(map(int, num), reverse=True))))
