import sys

n = int(sys.stdin.readline().rstrip())
nums = set(map(int, sys.stdin.readline().rstrip().split()))
print(' '.join(map(str, sorted(list(nums)))))