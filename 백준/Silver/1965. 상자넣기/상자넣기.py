import sys

n = int(sys.stdin.readline().rstrip())
boxes = list(map(int, sys.stdin.readline().rstrip().split()))

dp = [-1 for _ in range(n)]
dp[0] = 1

for i in range(1, n):
    max_vol = 0
    for j in range(i):
        if boxes[i] > boxes[j]:
            max_vol = max(dp[j], max_vol)
    dp[i] = max_vol + 1

print(max(dp))