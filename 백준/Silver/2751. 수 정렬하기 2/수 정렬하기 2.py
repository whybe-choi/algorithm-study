import sys

n = int(sys.stdin.readline().rstrip())
nums = []

for _ in range(n):
    num = int(sys.stdin.readline().rstrip())
    nums.append(num)
    
print(*sorted(nums), sep='\n')