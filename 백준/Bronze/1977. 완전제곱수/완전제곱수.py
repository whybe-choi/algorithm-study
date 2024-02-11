import sys

m = int(sys.stdin.readline().rstrip())
n = int(sys.stdin.readline().rstrip())

nums = []
total = 0
for i in range(m, n+1):
    if (i ** 0.5) == int(i ** 0.5):
        nums.append(i)
        total += i
        
if total == 0:
    print(-1)
else:
    print(total)
    print(min(nums))