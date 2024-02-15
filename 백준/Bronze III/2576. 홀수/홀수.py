import sys

odds = []

for _ in range(7):
    num = int(sys.stdin.readline().rstrip())
    if num % 2 != 0:
        odds.append(num)
        
if len(odds) == 0:
    print(-1)
else:
    print(sum(odds))
    print(min(odds))
    