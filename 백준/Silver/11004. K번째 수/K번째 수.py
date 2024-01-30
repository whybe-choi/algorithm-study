import sys

n, k = map(int, sys.stdin.readline().rstrip().split())
nums = list(map(int, sys.stdin.readline().rstrip().split()))

print(sorted(nums)[k-1])